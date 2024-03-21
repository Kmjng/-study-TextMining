'''
 문2) urls 객체의 url을 대상으로 다음 조건에 맞게 웹 문서의 자료를 수집하시오.
    조건1> https://으로 시작하는 url만을 대상으로 한다.
    조건2> url에 해당하는 웹 문서를 대상으로 <a> 태그(tag)의 내용만 출력한다.
    <> _result_ </>
    조건3> <a> 태그 내용이 없는(None) 경우는 출력하지 않는다.

    <출력 결과 예시>
    a tag 내용 :  OTTOGI
    a tag 내용 :  NONGSHIM
       중간 생략
    a tag 내용 :  네이버 정책
    a tag 내용 :  고객센터
    a tag 내용 :  ⓒ NAVER Corp.
'''

from urllib.request import urlopen # 함수 : 원격 서버 url 요청 
from bs4 import BeautifulSoup # 클래스 : html 파싱
import re # 정규표현식

urls = ['https://www.daum.net', 'www.duam.net', 'https://www.naver.com']

# 단계1 : url 정제
compile1 = re.compile('^https://')
urls_real = []

for i in urls:
    ele_pat = compile1.match(i)
    if ele_pat : 
        urls_real.append(i) 



# 단계2 : url에서 a 태그 내용 수집 & 출력

for i in urls_real: 
    req = urlopen(i) # 서버 요청해서 텍스트 가져오기 
    data = req.read() # 가져온 텍스트 읽기 
    ele = BeautifulSoup(data, 'html.parser') # 파싱
    links = ele.find_all('a')  # 파싱(구문 분석) 내용 중 a 태그 요소들 찾기 
    for j in links:     # 요소내용을 추출하기 전에는 html형식
        print('a tag 내용:',j.text)   
        
# print(urls_real)


# 방법 2 

# 단계1 : url 정제
pat = re.compile('^https://')

new_urls = []

for url in urls :
    result = pat.match(url)
    if result :
        new_urls.append(url)
        
print(new_urls) # ['https://www.daum.net', 'https://www.naver.com']

# 단계2 : url에서 a 태그 내용 수집 & 출력
for url in new_urls : 
    # 1. url 요청
    print('url :', url)
    req = urlopen(url)
    data = req.read()
    
    # 2. html 파싱 
    src = data.decode('utf-8')
    html = BeautifulSoup(src, 'html.parser')
    
    # 3. a 태그 찾기 & 내용 
    a_all = html.find_all('a') # 앵커 태그 전체 찾기 
    print('a 태그 전체 개수 :', len(a_all)) # a 태그 전체 개수 : 414
    
    for a in a_all :         
        if a.text != None : 
            print(a.text) # tag 내용 출력


# 크롤러 함수 
def crawler(url) :
    # 1. url 요청
    print('url :', url)
    req = urlopen(url)
    data = req.read()
    
    # 2. html 파싱 
    src = data.decode('utf-8')
    html = BeautifulSoup(src, 'html.parser')
    
    # 3. a 태그 찾기 & 내용 
    a_all = html.find_all('a') # 앵커 태그 전체 찾기 
    
    conts = []
    for a in a_all :         
        if a.text != None : 
            conts.append(a.text) # tag 내용 저장
            
    return conts


# 크롤러 함수 호출 
conts = [crawler(url) for url in new_urls]
print(conts) # [[daum 자료], [naver 자료]]








