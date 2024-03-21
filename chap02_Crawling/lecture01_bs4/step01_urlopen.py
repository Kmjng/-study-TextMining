"""
url 요청과 html 파싱
"""
# 파싱*이란? 구문 분석이다. 

from urllib.request import urlopen  # urllib모듈 (texts로 받아옴)
from bs4 import BeautifulSoup  # texts -> html 변환 (구문 분석하기 위해)
# 클래스는 낙타체

'''
urllib.request (urllib.request의 urllib의 request는 하위 모듈)
데이터를 보낼 때 인코딩하여 바이너리 형태로 보낸다
없는 페이지를 요청해도 에러를 띄운다
'''

dir(BeautifulSoup)
'''
find('tag명') - ★★★최초 발견 1개의 tag 반환 
findAll() - find_all의 이전 버전임 !
find_all('tag명') - 모든 tag 반환 ★★★★  
select(선택자명) 

주의 
BeautifulSoup의 find_all() 메서드: 이 메서드는 
BeautifulSoup 객체에서 특정 조건을 만족하는 모든 태그를 찾아 리스트로 반환 
re 모듈의 findall() 함수: 이 함수는 정규 표현식을 사용하여 
문자열에서 패턴에 일치하는 모든 부분 문자열을 찾아 리스트로 반환

'''
url = "http://www.naver.com/index.html"
 
# 1. 원격 서버 url 요청 
req = urlopen(url)  # url 요청 -> 응답 
byte_data = req.read()  # text 읽기 (일단 아스키코드로 읽어옴.. 
# 근데 한글은 2바이트라 1바이트로 읽으면 깨짐현상 있음 -> 밑에 디코딩 잘해야함 )

print(byte_data) # ...<head> <meta charset="utf-8">...★★★★

# 2. html 파싱 (디코딩하고 파싱을 해준다!!)
text_data = byte_data.decode("utf-8") # 디코딩  
html = BeautifulSoup(text_data, 'html.parser') # html source 파싱
# BeautifulSoup(텍스트, 파싱도구)
# 파싱도구 = 파서(parser)
'''
parser 종류 
주요사용되는 Python 내장 HTML 파서 : html.parser
c언어로 작성된 html 파서 : lxml
html5 구문 분석시 사용되는 파서 : html5ib 
'''

# 3. a 태그 수집 
a = html.find('a') #요소 (element) 최소발견된 한개의 요소 반환
print('a tag : ', a) 
'''
a tag :  <a href="#topAsideButton"><span>상단영역 바로가기</span></a>
'''

# 4. 요소 속성 또는 내용 string으로 추출: string 메소드 
a.string # >> '상단영역 바로가기'

# 5. a 태그 전체 수집 
aa = html.find_all('a')
len(aa) 
print(aa) # 리스트 ( 내용물이 string이 아님 )
print(type(aa[0])) # <class 'bs4.element.Tag'>

contents =[] 
for i in aa: 
    contents.append(i.string) # 요소에서 내용추출(string)해서 append()  
print(contents)
# 6. a 태그 중 class 속성 값 중 하나인 link_view 수집 
a_link = html.find_all('a','link_view')
print(a_link)
