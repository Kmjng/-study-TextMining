# -*- coding: utf-8 -*-
"""
step04_konlpy_Okt.py

Kkma vs Okt 
 - 공통점 : 형태소 분석기 
 - Kkma : 상세한 품사 정보 제공, 중복단어 제외, 복합어 분해 기능 
 - Okt : 최소한의 일반 품사 제공, 중복단어 추출, 서수는 명사에서 제외, 복합어 분해x


"""

# Okt(Open Korean Text) : 형태소 분석 및 품사 태깅 기능을 제공(python 구현)
from konlpy.tag import Okt 


##############################
### Okt
##############################
okt = Okt() # 객체 생성 
dir(okt)
'''
 'morphs',    -> 형태소
 'normalize', -> ★★ 문단을 문장으로 추출 (okt에 적합한 문장으로 변환)
 'nouns',     -> 명사 추출 (영문도 명사 추출가능), 중복가능
 'phrases',   -> 구 추출 (2개 이상의 절)
 'pos',       -> 품사 태깅 (형태소, 품사)
'''

# 문단(Paragraph) : 3개 문장 
para  = """"나는 홍길동 입니다. age는 23세 입니다. 
나는 대한민국 사람입니다.
대한민국을 사랑(love)합니다."""

# 형태소 추출 
okt.morphs(para) # list 


# 문단 -> 문장  (okt에 적합한 문자열로 반환★)
# 오타가 섞인 문장을 정규화해 처리하는데 좋다.
ex_sent = okt.normalize(para) 
print(ex_sent)

help(okt.normalize)

# 명사 추출  
okt.nouns(para) # 중복된 단어도 가져옴 ★★★
# 단, 수사x, 복합어 분해x 
'''
['나', '홍길동', '세', '나', '대한민국', '사람', '대한민국', '사랑']
'''

# 품사 부착(단어, 품사) 
ex_pos = okt.pos(para) 
'''
[('나', 'Noun'),
 ('는', 'Josa'),
 ('홍길동', 'Noun'),
 ('입니다', 'Adjective'),
 ('.', 'Punctuation'),
 ('age', 'Alpha'),......]
'''
'''
'Noun' : 명사 
'Josa' : 조사 
'Adjective' : 형용사 
'Punctuation' : 문장부호 
'Alpha' : 영문 
'Verb' : 동사 
'Number' : 숫자 
'''

# 단어 추출: 명사(Noun), 영문(Alpha)
words =[] 
for wor, wclass in ex_pos: 
    if wclass =='Noun' or wclass =='Alpha':
        words.append(wor)

print(words)

# 단어 카운트 
wc ={} 
for i in words:
    wc[i]=wc.get(i,0) +1 

print(wc)

# TopN 단어 선정 
# collections 모듈의 
# Counter 클래스 사용하자 ★★★★
# 기존에 sorted 대신 사용 가능
from collections import Counter # class 
counter = Counter(wc)
dir(counter)
'''
...'most_common',... #TopN 
'''
# most_common메소드
# dict의 key, value를 튜플로 감싸서 리스트 반환 ★★
top5 = counter.most_common(n=5)
print(top5)
'''
[('나', 2), ('대한민국', 2), ('홍길동', 1), ('age', 1), ('세', 1)]
'''
