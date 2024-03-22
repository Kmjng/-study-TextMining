# -*- coding: utf-8 -*-
"""
step02_button_click1.py

로케이터(locator) : By 클래스에서 제공되는 요소(element) 찾기 기능 

<작업순서>
1. naver page 이동 
2. login 버튼 클릭 
3. 페이지 이동(뒤로, 앞으로) 
"""

from selenium import webdriver # driver 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자  
from selenium.webdriver.common.by import By # 로케이터(locator) ★★★★
import time # 화면 일시 정지 

# 1. driver 객체 생성 
# 웹드라이버 객체를 생성하면 빈 창이 뜨게 된다. 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. 대상 url 이동 
driver.get('https://www.naver.com/') # url 이동 

# 3. 로그인 버튼 태그(element) 가져오기 : class name으로 가져오기(ppt.13) 
# 로그인 버튼이 a태그 안에 있고, 
# class 속성 이름이 MyView-module__link_login___HpHMW 이면?
'''

find_element() : 1개 요소 반환 
find_elements() : n개 요소들 반환 <list>
★ 웹드라이버 메소드 중 이 둘은 로케이터와 함께 쓰이는 듯 하다 
find_element(By.로케이터)

★ 로케이터 종류 ★
CLASS_NAME - 클래스 이름으로 요소 가져오기 
ID - ID 선택자(유일성)로 요소 가져오기 
NAME - name 속성으로 찾기 
TAG_NAME - 태그명으로 요소 가져오기
LINK_TEXT - a 태그의 텍스트로 찾기
XPATH - 계층구조xpath. 절대경로 or 상대경로로 찾기 
CSS_SELECTOR -  선택자로 찾기 
'''
login_btn = driver.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
#
login_btn.click() # 로그인 버튼 클릭 
time.sleep(2) # 2초 일시 중지 

driver.back() # 현재페이지 -> 뒤로
time.sleep(2) # 2초 일시 중지 
  
driver.forward() # 현재페이지 -> 앞으로 
driver.refresh() # 페이지 새로고침(F5)
time.sleep(2) # 2초 일시 중지 

driver.close() # 현재 창 닫기  


