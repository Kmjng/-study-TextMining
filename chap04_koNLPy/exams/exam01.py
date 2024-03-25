'''
 문1) html01.html 웹 문서를 대상으로 다음 조건에 맞게 형태소 분석으로 단어를 추출하시오. <출력결과> 참고
      <조건1> 추출 단어 품사 : NNG(일반 명사), NNP(고유 명사), OL(영문)
      <조건2> 2음절~5음절 사이의 길이를 갖는 단어 선정
      <조건3> 중복 단어 제외 & 단어와 단어 길이 출력 
    
   <출력 결과>
   ['광고', 'html', '정보', 'UTF-8', '제목', 'nav', 'li', '작성자', '저작권', 'title', 
    '보호', 'head', 'ul', '구분', '태그', '부여', 'meta', '개인', '로그', '머리말', '보조', 
    'body', '꼬리말', 'aside', '시멘', '게이', '문서', '주요', '내용', '의미', '사이트', '메뉴', '소개']

  단어 길이 : 33
'''

from konlpy.tag import Kkma # 형태소분석  


# 1. file 자료 가져오기 
path = r"C:/ITWILL/3_TextMining/TextMining/data"
file = open(path + '/html01.html', encoding='utf-8')
data = file.read() # 문자열 읽기 
file.close()


print(data) # 형태소분석을 위한 텍스트 자료 
type(data) # >> class 'str'

# 2. Okt 객체 생성 
kkma = Kkma()


# 3. 명사(단어) 추출 
nouns = [] # 명사 저장 
data_pos = kkma.pos(data)
print(data_pos)
for i, j in data_pos : 
    if j == 'NNG' or j =='NNP' or j== 'OL':
        nouns.append(i)
print(nouns)

# 4. 2음절~5음절 길이 단어 선정  
final_nouns = []

for i in nouns: 
    if len(i)>=2 and len(i)<=5 : 
        final_nouns.append(i)
print(final_nouns)


# 5. 중복 단어 제거 & 단어와 단어길이 출력
# 방법 (1) # 왜 결과 다르지????
wc = {} 
final_nouns1=[]
for i in final_nouns: 
    wc[i]=wc.get(i,0)+1
for i,j in wc.items():
    if j == 1: 
        final_nouns1.append(i)
print(final_nouns1)

print(len(final_nouns1))

# 방법 (2) 
# gpt - 튜플은 무작위 중복제거로 부정확함...
# 실제로, 
'''
아래의 단어들은 중복된 단어인데 final_nouns2에 들어가 있음.
['태그', '문서', 'title', '시멘', 
 'head', 'html', 'ul', 'body', '의미', 'li']
'''
final_nouns2 = list(set(final_nouns))
print(final_nouns2)
print(len(final_nouns2))


lst=[]
for i in final_nouns2: 
    if i not in final_nouns1:
        lst.append(i)

print(lst)
