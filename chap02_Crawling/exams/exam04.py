'''
 문4) 아래 url을 이용하여 어린이날(20220505)에 제공된 뉴스 기사를 
   1~5페이지 크롤링하는 크롤러 함수를 정의하고 크롤링 결과를 확인하시오.    
   
   <조건1> 크롤러 함수 정의
   <조건2> 크롤링 대상  : <a> 태그의 'class=link_txt' 속성을 갖는 내용 
   <조건3> 크롤링 결과 확인  : news 개수와  news 출력  
'''

import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup


# 클로러 함수(페이지수, 검색날짜) 
def crawler_func(pages, date):
    pass # 내용 채우기    





# 클로러 함수 호출 
crawling_news = crawler_func(5, '20220505') # (페이지수, 검색날짜)



