# -*- coding: utf-8 -*-
"""
step03_konlpy_Kkma.py
"""

# 꼬꼬마(Kkma) -  서울대학교 연구실에서 개발한 형태소 분석기, 비교적 정확한 분석 결과를 제공(java구현)
from konlpy.tag import Kkma


##########################
### Kkma
##########################
kkma = Kkma() # 객체 생성 
dir(kkma)
'''
 'morphs',  -> 형태소
 'nouns     -> 명사추출(중복 명사 제외, 수사 포함) 단, 한글만 됨
 'pos',     
 'sentences', -> ★★ 문장으로 반환 
 'tagset']
'''
# 문단(Paragraph) : 3개 문장 
para  = "나는 나는 홍길동 입니다. age는 23세 입니다. 나는 대한민국 사람입니다."

# 문단 -> 문장
ex_sent = kkma.sentences(para)  
print(ex_sent)

# 문단 -> 명사(단어)
# nouns()
ex_nouns = kkma.nouns(para) # 복합어 분해, 중복명사는 제외 ★★★
print(ex_nouns) 

# 문장 -> 명사(단어) # 문장으로 추출하면 중복명사도 추출가능
# 방법 (1) 
nouns_0=[]
for sent in ex_sent: 
    nouns = kkma.nouns(sent)
    nouns_0.append(nouns)
print(nouns_0)
'''
[['나', '홍길동'], ['23', '23세', '세'], 
 ['나', '대한', '대한민국', '민국', '사람']]
'''
# 방법 (2) 
nouns_01=[]
for sent in ex_sent: 
    nouns = kkma.nouns(sent)
    nouns_01.extend(nouns) # 중첩리스트 말고
print(nouns_01)
'''
['나', '홍길동', '23', '23세', '세', 
 '나', '대한', '대한민국', '민국', '사람']
'''


# 문단 -> 품사(형태소)
ex_pos = kkma.pos(para)
print(ex_pos)  

nouns=[] # 단어를 명사와 영문만 담고자 할때 

for word, wclass in ex_pos: 
    if wclass =='NP' or wclass =='NNG' or wclass =='NNM' or wclass =='OL' :
        nouns.append(word)
print(nouns)
'''
['나', '홍길동', 'age', '세', '나', '대한민국', '사람']
'''

# 형태소 반환 
ex_morphs = kkma.morphs(para)
print(ex_morphs)
