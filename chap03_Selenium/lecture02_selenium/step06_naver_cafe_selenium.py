# -*- coding: utf-8 -*-
"""
NAVER 카페 > 인기글 수집 
"""

from selenium import webdriver # 드라이버 
from selenium.webdriver.chrome.service import Service # Chrom 서비스
from webdriver_manager.chrome import ChromeDriverManager # 크롬드라이버 관리자 
from selenium.webdriver.common.by import By
import time # 화면 일시 정지


# 1. driver 객체 생성 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. 대상 url 이동 : NAVER 카페 홈   
driver.get('https://section.cafe.naver.com/ca-fe/home')
url = driver.current_url
print('접속한 url =', url)
# 인기글 클릭하기 
# <a href="/ca-fe/home/cafe-hots" class="btn_gnb">....
# //*[@id="gnbMenu"]/a[4]


driver.implicitly_wait(2) # 2초 대기(자원 loading)


# 3. NAVER 카페 > [인기글] 링크 클릭
element = driver.find_element(By.XPATH, '//*[@id="gnbMenu"]/a[4]')
element.click()

driver.implicitly_wait(2) # 2초 대기(자원 loading)

'''
  
# ------------ 화면 스크롤바 내림 ------------------------------------------------------ 
last_height = driver.execute_script("return document.body.scrollHeight") #현재 스크롤 높이 계산

while True: # 무한반복
    # 브라우저 끝까지 스크롤바 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
    
    time.sleep(2) # 2초 대기 - 화면 스크롤 확인

    # 화면 갱신된 화면의 스크롤 높이 계산
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 새로 계산한 스크롤 높이와 같으면 stop
    if new_height == last_height: 
        break
    last_height = new_height # 새로 계산한 스크롤 높이로 대체 
#-------------------------------------------------------------------------
'''



# 4. 인기글 요소(Element) 수집  
# 인기글 목록에 인기글 타이틀들은 strong 태그에 있음.
strongs = []   
                
for i in range(2, 52) : # 인기글 50개 수집  
    try :  
        strong = driver.find_element(By.XPATH, f'//*[@id="mainContainer"]/div[2]/div/div[2]/div[{i}]/div/a/div[1]/strong')
        strongs.append(strong) 
    except :
          print('xpath 오류')
       

print('수집 element 개수 =', len(strongs))

     
driver.close() # 창 닫기

print(strongs)
type(strongs[0]) # >> selenium.webdriver.remote.webelement.WebElement

# strong 태그요소에서 텍스트 가져오기 
# 좋은 방법은 아닌듯 
# 웹 요소의 텍스트를 직접 가져오자 
texts =[strong.text for strong in strongs] # 인기글 제목 저장 
print(texts)
