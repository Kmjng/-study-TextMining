'''
url query 이용 뉴스 자료 수집 

   <작업절차> 
  1. http://media.daum.net -> 시작페이지 
  2. https://news.daum.net/newsbox -> 배열이력 클릭  
'''

import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup
import pandas as pd # 날짜 생성 
import re # 정규표현식 

# 1. 수집 기간 날짜 생성  
dates = pd.date_range("2023-03-07", "2024-03-07") # 12개월
print(dates)

# 날짜에서 하이픈(-) 제거
kdates = [re.sub('-', '', str(date)[0:10]) for date in  dates]
print(kdates) 


# 2. Crawler 함수(페이지, 검색날짜) 
def crawler_func(date, pages=5):  
    day_news = []
    
    for page in range(1, pages+1) : 
        
        # 1) url 구성 
        url = f"https://news.daum.net/newsbox?regDate={date}&page={page}"
        
        # 2) url 요청          
        res = req.urlopen(url)
        data = res.read()
        
        # 3) html 파싱
        src = data.decode('utf-8') 
        html = BeautifulSoup(src, 'html.parser')
        
        # 4) a 태그 수집                  
        links = html.select('ul[class="list_arrange"] > li > strong > a[class="link_txt"]') # 1) list tag 수집
            
        page_news = [] # 1 페이지 news 저장

        for a in links :
            news = str(a.text).strip() # 문장 끝 불용어 제거 
            page_news.append(news)  
        
        day_news.extend(page_news) 
        
    return day_news
    

# 3. 클로러 함수 호출 
crawling_news = [crawler_func(date) for date in kdates]


# 4. file save 
import pickle # binary file save  

path = r'C:\ITWILL\3_TextMining\data'

file = open(path + '/news_data.pkl', mode='wb')
pickle.dump(crawling_news, file)
file.close()

# file load 
file = open(path + '/news_data.pkl', mode='rb')
news_data = pickle.load(file)
print(news_data)
