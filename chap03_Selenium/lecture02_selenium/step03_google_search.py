# -*- coding: utf-8 -*-
"""
step03_goole_search.py

검색어 입력 및 검색 페이지 이동 : ppt.13 참고 
"""

from selenium import webdriver # driver 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자  
from selenium.webdriver.common.by import By # 요소 선택 
from selenium.webdriver.common.keys import Keys # 엔터키 역할
import time # 화면 일시 정지 
 
# 1. driver 객체 생성 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# 2. url 이동 : 구글 페이지 이동 
driver.get("https://www.google.com/") # 구글 페이지 이동

# 3. 입력상자 가져오기  
# <tag name='q'>내용</tag>
'''
name 속성 - form 컨트롤 요소의 값(value)을 서버로 전송하기 위해 필요한 속성
'''
elem = driver.find_element(By.NAME, "q") # 입력상자 element 수집

# 4. 검색어 입력 -> 엔터 
# send_keys() 메소드가 제공된다.
elem.send_keys("셀레리움 크롤링") # 검색어 입력 
elem.send_keys(Keys.ENTER) # 엔터 키  

# ★ 동작 중간에 실행속도를 맞추기 위해 sleep을 해줘라~~~
time.sleep(4)

# class 이름으로 요소 선택하기
# class="LC20lb MBeuO DKV0Md" >> 셋 중 하나 사용하면 됨 ★★★ 공백은 OR 
heads = driver.find_elements(By.CLASS_NAME, "LC20lb")
print('수집 head 개수 =', len(heads)) 
    

# 6. head 텍스트 출력  
head_text = []
for head in heads :        
    head_text.append(head.text) 


driver.close() # 창 닫기 

print(head_text)
