'''
1. tag 계층구조 찾기
2. find('tag')함수 찾기 
'''

from bs4 import BeautifulSoup

path = r'C:/ITWILL/3_TextMining/TextMining/data' # 파일 경로 

# 1. 로컬 파일 읽기 
file = open(path + '/html01.html', mode='r', encoding='utf-8')
text_data = file.read() 
print(text_data)

# 2. html 파싱
html = BeautifulSoup(text_data, 'html.parser') # 파싱객체 
print(html)


# 3. 태그 내용 수집 

# 방법 1) tag 계층구조 찾기
h1_element = html.html.body.h1 # DOM 구조 node 접근 ★★★★
    # 요소객체이름.html.body.h1 
print('h1 : ', h1_element.string) #>> h1 :   시멘틱 태그 ?
type(h1_element) # >> bs4.element.Tag

# 방법 2) find()함수 : 태그 찾기 
h2 = html.find('h2')
print('h2 : ', h2.string) #>> h2 :   주요 시멘틱 태그

# 3) find_all() 함수 : 전체 태그 찾기 
lis = html.find_all('li') # li요소를 모두 찾아 요소 list 반환 (type: bs4.element.ResultSet)
len(lis)
print(lis) # >> class 'bs4.element.ResultSet'


# 요소 내용들을 리스트 저장 
li_conts =[i.string  for i in lis]
print(li_conts)
'''
element.string : 요소 내용 추출 
element.text : 요소 내용 추출 (동일)
string 메소드는 해당 태그에 [내용]만 있는 경우 
text 메소드는 해당 태그 내에 [내용+다른 태그★]가 함께 포함되어 있을 때
태그들을 무시하고 내용들만 가져온다~
'''

# string vs text 
src = "<div> 이순신 <p> 홍길동 </p> <a> 링크 </a> </div>"
src_element = BeautifulSoup(src, 'html.parser')

src_element.string # >> - 
src_element.text # >> ' 이순신  홍길동   링크  '

