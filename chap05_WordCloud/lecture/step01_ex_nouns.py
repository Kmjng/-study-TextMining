# -*- coding: utf-8 -*-
'''
<작업순서> 
1. text file 읽기 
2. 문장 추출
3. 명사 추출 : Kkma
4. 단어 전처리 : 단어 길이 제한, 숫자 제외 
5. 단어, 단어빈도수 준비 
6. 단어 시각화 : 막대와 선 그래프 이용
'''

from konlpy.tag import Kkma # class - 형태소 
kkma = Kkma() # Kkma 객체 생성 

import matplotlib.pyplot as plt # 별칭 : 그래프 시각화  

# 1. text file 읽기 
path = r'C:/ITWILL/3_TextMining/TextMining/data'

file = open(path + '/text_data.txt', mode='r', encoding='utf-8')
data = file.read()
print(data)
type(data) # >> str



# 2. 문장 추출 : 문단(str) -> 문장(list) 
ex_sent = kkma.sentences(data)
print(ex_sent)


'''
['형태소 분석을 시작합니다.', '나는 데이터 분석을 좋아합니다.',
 '직업은 데이터 분석 전문가 입니다.', 
 'Text mining 기법은 2000대 초반에 개발된 기술이다.']
'''


# 3. 명사 추출 : 문장 -> 명사 
nouns = kkma.nouns(data)  
print(nouns)
'''
['형태소', '분석', '나', '데이터', '직업', '전문가', '기법',
 '2000', '2000대', '대', '초반', '개발', '기술']
'''
# 근데 kkma라이브러리는 중복명사 제외하므로 전부 빈도수 1일 것
# 따라서 다음과 같이 해준다.
nouns_1=[]
for sent in ex_sent:
    for noun in kkma.nouns(sent):
        nouns_1.append(noun)

print(nouns_1)


# 4. 단어 전처리 


from re import match # 숫자 제외하기 위해 
nouns_count = {} # 단어 카운터 

for noun in nouns_1 : 
    if len(noun) > 1 and not(match('^[0-9]', noun)) : # 두 글자 이상 그리고 숫자 제외
        nouns_count[noun] = nouns_count.get(noun, 0) + 1
        
print(nouns_count)
# 5. 단어와 단어빈도수 준비         
words = []
count = []
for i, j in nouns_count.items(): 
    words.append(i)
    count.append(j)

print(words)
print(count)


# 6. 단어 시각화 : 그래프 이용 

# 한글 지원 ★★★★
plt.rcParams['font.family'] = 'Malgun Gothic'

# 막대그래프
plt.bar(words, count, color='blue') 
plt.title('텍스트 빈도 분석')
plt.xticks(rotation=90)
plt.show()



