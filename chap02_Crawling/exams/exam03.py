'''
 문3) css_example.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오.

   <조건1> class="odd" 선택자를 이용하여 3행과 5행의 <td> 전체 내용 출력 

   <출력 결과>     
    201602 
    이순신 
    해양학과 
    lee@naver.com 
    201604 
    유관순 
    유아교육 
    you@naver.com
    
    <조건2> id="tab" 선택자를 이용하여 하위 태그 전체를 가져온 후 <th> 전체 내용 출력
    
   <출력 결과>
    학번 
    이름 
    학과 
    이메일
'''

from bs4 import BeautifulSoup

path = r'C:/ITWILL/3_TextMining/TextMining/data'

# 1. 파일 읽기 
file = open(path + "/css_example.html", mode='r', encoding='utf-8')
source = file.read()
file.close()


# 2. html 파싱
html = BeautifulSoup(source, 'html.parser')
print(html)

# 3. 선택자 이용 태그 내용 가져오기 
odds = html.select('.odd>td')
print(odds)
odd_ele=[]
for i in odds: 
    odd_ele.append(i.text)

print('\n'.join(odd_ele))

# < 조건 2> 
ths = html.select('#tab>tr>th')
print(ths)
ths_ele = [] 
for i in ths:
    ths_ele.append(i.text)
print('\n'.join(ths_ele))
