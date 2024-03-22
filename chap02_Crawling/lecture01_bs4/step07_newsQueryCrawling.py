'''
url query 이용 뉴스 자료 수집 

   <작업절차> 
  1. http://media.daum.net -> 시작페이지 
     페이지 들어가서 맨밑에 '배열이력'이 있고, 과거 내용이력들을 볼 수 있음.
  2. https://news.daum.net/newsbox -> 배열이력 클릭  
  3. https://news.daum.net/newsbox?regDate=20230307
     날짜 배너를 선택하면, url에 쿼리문이 포함됨
  4. https://news.daum.net/newsbox?regDate=20230307&tab_cate=NE&page=2
     2페이지 
     
  1년 뉴스 수집 
  - 년도: 2023-03-07 ~ 2024-03-07
  - 1일 뉴스 : 5페이지 분량 
'''

import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup
import pandas as pd # 날짜 생성 
import re # 정규표현식 

# 1. 수집 기간 날짜 생성
# (1) 날짜 객체 만들기
# pd.date_range() 메소드
dates = pd.date_range("2023-03-07", "2024-03-07") # 12개월
print(dates)

# 쿼리에서 사용되는 날짜형태와 맞게 (YYYYMMDD)
# (2) 날짜에서 하이픈(-) 제거
kdates = [re.sub('-', '', str(date)[0:10]) for date in  dates]
print(kdates) 
len(kdates)


# 2. Crawler 함수(페이지, 검색날짜) 
# 367일짜리를 해야하므로 해당 검색날짜들에 대해서는 함수 말고 
# 밑에 for문 명령어로 따로 수행
def crawler_func(date, pages=5):  # 하루 5페이지
    day_news = [] # 1일 뉴스 저장 
    
    for page in range(1, pages+1) : 
        
        # 1) url 구성 
        url = f"https://news.daum.net/newsbox?regDate={date}&tab_cate=NE&page={pages}"
        
        # 2) url 요청          
        res = req.urlopen(url)
        data = res.read()
        
        # 3) html 파싱
        src = data.decode('utf-8') 
        html = BeautifulSoup(src, 'html.parser')
        
        # 4) a 태그 수집 # list tag 수집                 
        links = html.select('ul[class="list_arrange"] > li > strong > a[class="link_txt"]') 
        
        
        # 1 페이지 news 저장
        page_news = [] 
        for a in links :
            news = str(a.text).strip() # 문장 끝 불용어 제거 
            # html형태니까 str으로 변환해서 strip() 써야 한다. ★★★
            page_news.append(news)  
        
        day_news.extend(page_news) 
        
    return day_news
    

# 3. 클로러 함수 호출 
crawling_news = [crawler_func(date) for date in kdates]

print(crawling_news) # [[day1뉴스],[day2뉴스],....[day367뉴스]]



# 4. file save 
import pickle # binary file save  

path = r'C:/ITWILL/3_TextMining/TextMining/data'

file = open(path + '/news_data.pkl', mode='wb')
pickle.dump(crawling_news, file)
file.close()

# file load 
file = open(path + '/news_data.pkl', mode='rb')
news_data = pickle.load(file)
print(news_data)
