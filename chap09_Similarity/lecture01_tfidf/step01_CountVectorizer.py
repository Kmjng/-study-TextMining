# -*- coding: utf-8 -*-
"""
단어 출현빈도수(TF : Term Frequence)

TF 단어 생성기 : CountVectorizer  
  1. 단어 생성기(word tokenizer) & 단어 사전(word dictionary) 
  2. 문서단어행렬(DTM) : 단어 출현 빈도수에 의해서 가중치 적용 행렬 
     예) TF(Term Frequence) 가중치 : 단어출현빈도수  
"""

import string # texts 전처리 
from sklearn.feature_extraction.text import CountVectorizer # DTM (TF 가중치) 


# 1. texts 전처리
texts = ["우리나라    대한민국, 우리나라 만세", "비아그라 500GRAM 정력 최고!",
         "나는 대한민국 우리나라 사람", "보험료 15000원에 평생 보장 마감 임박",
         "나는 홍길동"]


print(string.punctuation) #문장부호 판단 
'''
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''
type(string.punctuation) # >> class 'str'

# texts 전처리 함수 
def text_prepro(texts):
    # Lower case 
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers 
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts


final_texts = text_prepro(texts)
print(final_texts)
'''
['우리나라 대한민국 우리나라 만세', '비아그라 gram 정력 최고',
 '나는 대한민국 우리나라 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''
# text 파일로 저장하기 ★
path = r'C:/ITWILL/3_TextMining/TextMining/data'
file = open(path+'/final_texts.txt', mode = 'w')

for i in final_texts:
    file.write(i)
    file.write('\n')
file.close()
'''
['우리나라 대한민국 우리나라 만세\n', '비아그라 gram 정력 최고\n', 
 '나는 대한민국 우리나라 사람\n', '보험료 원에 평생 보장 마감 임박\n', '나는 홍길동\n']
'''


# 2. 단어 생성기 
dir(obj)
dir(fit)
'''
vocabulary 
vocabulary_ 
'''
obj = CountVectorizer() # 단어 생성기 객체 생성 
fit = obj.fit(final_texts) # 원문 객체 반영 (벡터 생성) # 인자는 리스트
voca = fit.vocabulary_ # 단어 사전형태로 저장 (dict)


help(obj.fit)

print(voca) # {'단어':고유숫자} # ★주의: 출연횟수가 아니라 고유번호 붙인거임★★★
'''
{'우리나라': 9, '대한민국': 2, '만세': 4, '비아그라': 7, 
 'gram': 0, '정력': 12, '최고': 13, '나는': 1, '사람': 8, 
 '보험료': 6, '원에': 10, '평생': 14, '보장': 5, 
 '마감': 3, '임박': 11, '홍길동': 15}
'''
len(voca) # >> 16 

# 문서 수 5 vs 단어 수 16 
# 문서 수는 행 갯수 

# 3. 문서단어행렬(DTM)  
# fit_transform() 메소드
# 원문 객체 반영 & 변형 
DTM = obj.fit_transform(final_texts) 
print(DTM)
'''
(행,열) 가중치(TF)
(0, 9)	2  => 1행 10열에 들어감/ 첫번째 문서에서 9번 단어가 두번 등장 ('우리나라')
(0, 2)	1  => 1행 3열 '대한민국'
(0, 4)	1
(1, 7)	1
(1, 0)	1
(1, 12)	1
(1, 13)	1
(2, 9)	1
(2, 2)	1
(2, 1)	1
(2, 8)	1
(3, 6)	1
(3, 10)	1
(3, 14)	1
(3, 5)	1
(3, 3)	1
(3, 11)	1
(4, 1)	1
(4, 15)	1
'''

# numpy array 변형 

DTM_arr = DTM.toarray() 
print(DTM_arr)
'''
[[0 0 1 0 1 0 0 0 0 2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0]
 [0 1 1 0 0 0 0 0 1 1 0 0 0 0 0 0]
 [0 0 0 1 0 1 1 0 0 0 1 1 0 0 1 0]
 [0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1]]
'''