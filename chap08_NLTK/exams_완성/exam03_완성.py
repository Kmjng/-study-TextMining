# -*- coding: utf-8 -*-
"""
문3) movies_metadata.csv 파일의 'overview' 칼럼을 대상으로 단계3에서 '단어 토큰화'한 words를 대상으로 
     단계4에서 '품사 태깅'하고, 단계5에서 '필요한 품사'만 선택하여 단어를 선정하시오.
"""
import pandas as pd

# 단계1 : csv file load 
review_data = pd.read_csv(r'C:\ITWILL\3_TextMining\data\movies_metadata.csv')

# overview 칼럼 선택 
overview = review_data['overview'].to_list()
overview # 영문 텍스트 



# 단계2 : 품사 태깅 생성기 및 데이터 다운로드 
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

import nltk
nltk.download('punkt') # 토큰 생성에 필요한 데이터
nltk.download('averaged_perceptron_tagger') # 품사 태깅 관련 데이터 

len(overview) # 45,466 : 전체 문장 개수 

# 단계3 : 단어 토큰화 : 예외처리 
words = []

for row in overview :
    try :
        words.extend(word_tokenize(row)) # 단어 토큰화 과저에서 예외발생 
    except :
        pass

len(words) # 2,783,017 : 전체 단어 개수 

#########################[ 이후 부터 작업 ]#############################

# 단계4 : 품사 태깅 
pos_words = pos_tag(words)
pos_words[:5] # 단어 5개 확인 
# [('Led', 'VBN'), ('by', 'IN'), ('Woody', 'NNP'), (',', ','), ('Andy', 'NNP')]
pos_words[-5:]
# [('in', 'IN'), ('the', 'DT'), ('20th', 'JJ'), ('century', 'NN'), ('.', '.')]


# 단계5 : 단어 선택 : 명사(NN, NNS, NNP), 동사(기본형, 3인칭), 형용사 선택(기본형, 3인칭)
'''
VB: Verb, Base Form (동사, 기본형)
VBP: Verb, Non-3rd Person Singular Present (동사, 3인칭 단수형이 아닌 현재형)
VBZ: Verb, 3rd Person Singular Present (동사, 3인칭 단수형 현재형)
JJ: Adjective (형용사)
'''

final_words = [] 

for word, wclass in pos_words : # ('John', 'NNP')
    if wclass == 'NNP' or wclass == 'NNS' or wclass == 'NN' \
       or wclass == 'VB' or wclass == 'VBZ' or wclass == 'VBP' \
       or wclass == 'JJ'    :
        final_words.append(word)

len(final_words) # 1,262,986    
    
2783017 - 1262986 # 1,520,031 정제된 단어   
    
print(final_words[:5]) # ['Woody', 'Andy', 'toys', 'live', 'room']   
print(final_words[-5:]) # ['gay', 'men', 'women', '20th', 'century']   
    
    
    
    
    
    
    
    
    












