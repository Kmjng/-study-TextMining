'''
tag 속성값 가져오기

element : <시작태그 속성 ='값'> 내용 </종료태그>

'''

from bs4 import BeautifulSoup

path = r'C:/ITWILL/3_TextMining/TextMining/data' # 파일 경로 

# 1. html source 가져오기 
file = open(path + '/html02.html', mode='r', encoding='utf-8')
src = file.read()

# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)

# 3. 태그 속성과 내용 가져오기 
links = html.find_all('a') # list
print(links)
# [<a href="www.naver.com">네이버</a>,...<a href="http://www.duam.net">다음</a>]

print(links[0].get('href')) #href라는 속성의 값을 가져옴
type(links[0].get('href')) # >> class 'str'
'''
element.get('속성') : 속성 값 반환 
element.text or .string :  내용 반환 
 .string : None(공백) 도 string이어서 같이 반환함. ★★★
 .text : None은 text가 아니어서 반환 안함 ★★★

참고 
object.member() : member()는 메소드 
object.member : member는 필드
'''
urls =[] 
for i in links: 
    url=i.get('href')
    urls.append(url)
    print(i.get('target'))

# 4. 정규표현식으로 정상 url 선별 
import re 

url_pat = re.compile('^http://www') # 접두어가 ^이하로 오는 것 객체화  
print(url_pat)

new_urls =[] 
for i in urls: 
    result = url_pat.match(i)  
    if result : 
        new_urls.append(i)

print(new_urls)
'''
['http://www.duam.net', 'http://www.duam.net', 'http://www.duam.net']
'''