# -*- coding: utf-8 -*-
"""
numpy & pandas 응용 : 문서단어 행렬(DTM) 만들기 
"""

'''
1.원문(doc)
대한민국은 나의 조국입니다. 
나는 홍길동 입니다.
        
2.문서단어행렬(DTM)
   나  대한민국 조국 홍길동
1  1       1      1    0
2  1       0      0    1 


3.단어문서행렬(TDM)
           1       2 
나         1       1    
대한민국   1       0     
조국       1       0   
홍길동     0       1    
'''


# 원문 텍스트 
"""
대한민국은 나의 조국입니다. 
나는 홍길동 입니다.
"""


# 형태소 분석 후 문장 
texts = """대한민국 나 조국 
나 홍길동"""



# 1. 문장 만들기
sent_nouns = [] 

for sent in texts.split(sep='\n') :
    sent_nouns.append(sent.split()) # 중첩list 

print(sent_nouns)

# 2. 유일한 단어집 만들기  

# 1) 단어집 만들기 : 단어 수집  
nouns = []
for sent in sent_nouns :
    nouns.extend(sent) # 단일 list 

# 2) 유일한 단어 
unique_nouns = list(set(nouns))
unique_nouns 

# 3) 단어 정렬 
unique_nouns = sorted(unique_nouns) 
unique_nouns 


# 3. 영(zeros) 행렬 만들기 
import numpy as np 

zeros = np.zeros(shape = (2, 4))


# 4. 문서단어행렬(DTM) 만들기 
import pandas as pd 

dtm = pd.DataFrame(zeros, columns = unique_nouns) # 열이름=단어 
print(dtm)
'''
     나  대한민국   조국  홍길동
0  0.0   0.0  0.0  0.0
1  0.0   0.0  0.0  0.0
'''

# 문서 단위 단어 카운트 
# enumerate() ★★★★
# 색인과 값을 한번에 묶어서 제공
lst = [2,3,4,5,6]
for idx, value in enumerate(lst):
    print(idx, value)
'''
    print(idx, value)
0 2
1 3
2 4
3 5
4 6
'''

for doc, term in enumerate(sent_nouns): # (doc 색인, term 값)
    print(doc, term)
'''
0 ['대한민국', '나', '조국']
1 ['나', '홍길동']
'''
for doc, terms in enumerate(sent_nouns): # (doc 색인, terms 값)
    for term in terms:
        dtm.loc[doc,term] += 1 

print(dtm)
'''
     나  대한민국   조국  홍길동
0  1.0   1.0  1.0  0.0
1  1.0   0.0  0.0  1.0
'''
dtm.sum(axis=0) # 열 내에서 계산
'''
나       2.0
대한민국    1.0
조국      1.0
홍길동     1.0
dtype: float64
'''