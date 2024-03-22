# -*- coding: utf-8 -*-
"""
step05_xpath_attribute.py

<작업순서> 
google -> 입력상자 -> 검색어 입력 -> [검색 페이지 이동] -> element 수집 
"""

from selenium import webdriver # driver 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자
from selenium.webdriver.common.by import By # By.NAME,  By.TAG_NAME
from selenium.webdriver.common.keys import Keys # 엔터키 역할 


# 1. driver 객체 생성 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    
# 2. 대상 url 이동 
driver.get('https://www.google.com/') # url 이동   
    

# 3. 검색어 입력상자 : name 속성으로 가져오기     
input_text = driver.find_element(By.NAME, 'q') # 1개 element 
    

# 4. 검색어 입력 -> 엔터 
input_text.send_keys('파이썬') # keyword
input_text.send_keys(Keys.ENTER) # 엔터키 누름 -> 검색 페이지 이동 
driver.implicitly_wait(3) # 3초 대기(자원 loading)
    
# 5. 검색 페이지 element 수집 : tag 이름으로 가져오기 
urls = []   
           
for i in range(1, 6) :  
    a = driver.find_element(By.XPATH, f'//*[@id="rso"]/div[2]/div[{i}]/div/div/div/div[1]/div/div/span/a')
    urls.append(a.get_attribute('href'))           
        
print('수집 urls 개수 =', len(urls)) # 수집 urls 개수 = 5
driver.close() # 창 닫기 
'''    
//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a -> 제외 
//*[@id="rso"]/div[2]/div[1]/div/div/div/div[1]/div/div/span/a
//*[@id="rso"]/div[2]/div[2]/div/div/div/div[1]/div/div/span/a
//*[@id="rso"]/div[2]/div[5]/div/div/div/div[1]/div/div/span/a
'''
print(urls)
