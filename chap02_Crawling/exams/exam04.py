'''
 문4) 아래 url을 이용하여 어린이날(20220505)에 제공된 뉴스 기사를 
   1~5페이지 크롤링하는 크롤러 함수를 정의하고 크롤링 결과를 확인하시오.    
   
   <조건1> 크롤러 함수 정의
   <조건2> 크롤링 대상  : <a> 태그의 'class=link_txt' 속성을 갖는 내용 
   <조건3> 크롤링 결과 확인  : news 개수와  news 출력  
'''

from urllib.request import urlopen  # url 가져오기 
from bs4 import BeautifulSoup




# 크롤러 함수(페이지수, 검색날짜) 
def crawler_func(pages, date):
    news_list =[]
    for page in range(1,pages+1): # 1~ 5
        url = f'https://news.daum.net/newsbox?regDate={date}&tab_cate=NE&page={page}'
        req = urlopen(url) 
        read_req = req.read()  # txt 로 읽어오기
    
        decod_req = read_req.decode('utf-8')
        
        html = BeautifulSoup(decod_req,'html.parser')
        lis = html.select('ul.list_arrange > li') # li 태그 요소들
        #lis = html.select('ul[class="list_arrange"] > li > strong > a[class="link_txt"]') 
        
        
        for li in lis:
            a = li.find('a')
            b = str(a.text).strip() 
            # text로 요소들만 반환
            news_list.append(b)
    return news_list





# 클로러 함수 호출 
crawling_news = crawler_func(5, '20220505') # (페이지수, 검색날짜)
print(crawling_news)
print(len(crawling_news)) # 200

'''
['아이들, 가장 많이 다친 장소 어딜까?', 
 '"횡단보도도 없이 등교"..어린이가 위험하다', 
 '"반갑다! 마스크 없는 어린이날"..동심 모처럼 활짝',....]
'''

# 단어들 담기 (불용어 처리 preprocessing해보자 )
import re
words =[] 
for conts in crawling_news:
    conts = re.sub('[^\s\d\w]','',conts)
    for word in conts.split():
        words.append(word)

print(words)

# 단어들 카운트 
wc ={} 
for i in words:
    wc[i]=wc.get(i,0)+1

wc= sorted(wc.items(), key = lambda x: x[1], reverse = True) # value(빈도수) 내림차순 정렬 
print(wc)
'''
[('어린이날', 12), ('러', 8), ('美', 7), ('만에', 7), 
 ('코로나', 7), ('우크라', 6), ('마스크', 5), ....]
'''

