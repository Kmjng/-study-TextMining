# -*- coding: utf-8 -*-
"""
(base) pip install selenium #라이브러리 설치 
    - 조작을 자동화하는 프로그램을 구현하는데 용이한 도구를 제공
(base) pip install webdriver_manager #웹드라이버 설치 
    - 웹드라이버로 제어
    
"""

from selenium import webdriver # 드라이버 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자  
import time # 화면 일시 정지


# 1. driver 객체 생성 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
dir(driver)
'''
★ 웹드라이버 메소드 ★
get(url) : url 이동 
forward(): 다음화면 
back() : 이전화면 
close() : 브라우저 창 닫기 

'''



# 2. 대상 url 이동 
driver.get('https://www.naver.com/') # url 이동 

# 3. 일시 중지 & driver 종료 
time.sleep(3) # 3초 일시 중지 
driver.close() # 현재 창 닫기  