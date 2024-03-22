# -*- coding: utf-8 -*-
"""
step04_css_selector.py
"""

from selenium import webdriver # driver 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자  
from selenium.webdriver.common.by import By
import time # 화면 일시 정지 


# 태그 수집 함수 
def keyword_search(keyword) :
    # 1. driver 객체 생성 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    
    # 2. url 이동 : naver news 검색 페이지 이동
    url = f'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyword}'
    driver.get(url) 
    time.sleep(3)
    
    
    # 3. 선택자 지정 
    links = driver.find_elements(By.CSS_SELECTOR, 'a.news_tit') 
    print('수집 a_tags 개수 =', len(links))
    
    # 4. urls ,텍스트 내용 추출 
    urls = []
    texts =[]
    for a in links :        
        urls.append(a.get_attribute('href')) 
        # ★★ BeautifulSoup에서는 .get(속성명)으로 속성값 가져왔었음
        texts.append(a.text)
    driver.close() # 창 닫기 
    
    return urls, texts


# 함수 호출 
keyword = input('검색어 입력 : ') # 파이썬, 크롤링  
urls, texts = keyword_search(keyword)
print('-'*50)
print(urls) 
print(texts)   