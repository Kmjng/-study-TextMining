"""
선택자(selector) 이용 자료 수집 
 - 웹문서 디자인용으로 사용   

~ 특정 선택자를 포함하는 태그요소 가져오기 ~
 .select("선택자") - 보통 class 선택자에서 사용됨 - 리스트로 반환
 .select_one("선택자") - 보통 id 선택자에서 사용됨 
 
태그1, 태그2 (예시: ol, ul) => ol태그와 ul태그 
태그1태그2 (예시: ul li) => ul태그 내의 li 태그 

<div class ='class1'...</div> 일때,
div요소의 클래스를 선택하고 싶다? => div.class1 

<div id = 'id1' ....</div> 일때,
div요소의 아이디를 선택하고 싶다? =? div#id1

"""

from bs4 import BeautifulSoup # html 파싱 

path = r'C:/ITWILL/3_TextMining/TextMining/data' # 파일 경로 

# 1. html source 가져오기 
file = open(path + '/html03.html', mode='r', encoding='utf-8')
src = file.read()
print(src)

# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)
type(html) # >> class 'bs4.BeautifulSoup'


# 3. 선택자 이용 태그 내용 가져오기 

# 1) id 선택자
print('>> table 선택자 <<') 
table = html.select_one('#tab') # 1개 tag 수집 (id값이 tab인 태그 수집)
# ★★★ id 선택자는 중복이 없으므로 select_one()메소드 사용 
print(table)  # <table>....</table>

'''
<table border="1" id="tab">
<tr> <!-- 1행 -->
<!-- 제목 열 : th -->
<th id="id"> 학번 </th>
<th id="name"> 이름 </th>
<th id="major"> 학과 </th>
<th id="email"> 이메일 </th>
</tr>
<tr> <!-- 2행 -->
...
</tr>
<tr class="odd"> <!-- 5행 -->
<td> 201604 </td>
<td> 유관순 </td>
<td> 유아교육 </td>
<td> you@naver.com </td>
</tr>
</table>
'''
type(table) # >> class 'bs4.element.Tag'
    
# 2) class 선택자 : tr tag class='odd'
trs = html.select(".odd")  # 홀수 행 : id > class
# ★★★ class 선택자는 중복이 있을 수 있으므로 select()메소드 사용 
# 그리고 select()는 리스트로 반환 
print(trs) # class명이 odd인 태그요소들을 담고 있음 
'''
[<tr class="odd"> <!-- 3행(홀수) -->
<td> 201602 </td>
<td> 이순신 </td>
<td> 해양학과 </td>
<td> lee@naver.com </td>
</tr>, <tr class="odd"> <!-- 5행 -->
<td> 201604 </td>
<td> 유관순 </td>
<td> 유아교육 </td>
<td> you@naver.com </td>
</tr>]
'''

for tr in trs: 
    tds = tr.find_all('td') # list 
    for td in tds:
        print(td.text)
'''
 201602 
 이순신 
 해양학과 
 lee@naver.com 
 201604 
 유관순 
 유아교육 
 you@naver.com 
'''

# 계층적 선택자 : 부모 > 자식 > 자식 

# 예시 html에서 <table id='tab'> 요소 하위에 <tr> 이 5개 있음 
print(html.select('#tab'))
ths = html.select('#tab>tr>th') 
# id가 tab인 요소 하위 tr 하위 th인 요소들 # list 
print(ths) 
'''
[<th id="id"> 학번 </th>, 
 <th id="name"> 이름 </th>, 
 <th id="major"> 학과 </th>, 
 <th id="email"> 이메일 </th>]
'''
ids = [] 
conts = [] 
for th in ths: 
    ids.append(th.get('id')) # 속성 값 추출 
    conts.append(th.string)
print(ids) # >> ['id', 'name', 'major', 'email']
print(conts) # >> [' 학번 ', ' 이름 ', ' 학과 ', ' 이메일 ']


# select() 사용방법 2 
# select('tag명[속성="값"]')
html.select('tr[class="odd"]')
