import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup # html 파싱 도구 

url = "https://section.cafe.naver.com/ca-fe/home/cafe-hots" # NEVER 카페 > 인기글 

# 1. url 요청 
res = req.urlopen(url)
data = res.read() # 소스 읽기  


# 2. 한글 디코딩 & html 파싱
src = data.decode('utf-8') # 디코딩  

html = BeautifulSoup(src, 'html.parser')  # html 파싱 
print(html) # html문서에 인기글 텍스트가 없음 
        
# 정적 페이지 방식으로 텍스트 수집 불가 
        
    
    
    
    
    
    
    
    