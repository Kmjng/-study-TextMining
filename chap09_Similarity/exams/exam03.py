# -*- coding: utf-8 -*-
"""
문3) 주어진 파일의 자료를 이용하여 다음과 같이 word2vec 모델을
     생성하고 키워드를 입력하여 가장 유사한 단어 5개를 출력하는 
     함수를 정의하시오.   

 <조건1> 사용할 칼럼 : review 
 <조건2> word2vec 모델 파라미터 : window=5, min_count=1, sg=1  
 <조건3> 검색 키워드 : action, people, society 
"""

from gensim.models import Word2Vec # model 
from nltk.tokenize import word_tokenize # sentence -> work token
import pandas as pd # csv file


# 1. dataset load 
path = r'C:/ITWILL/3_TextMining/TextMining/data'
data = pd.read_csv(path + '/movie_reviews.csv')
print(data.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1492 entries, 0 to 1491
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   reviews  1492 non-null   object : 영화후기 
 1   title    1492 non-null   object : 영화제목  
 2   label    1492 non-null   int64  : 긍정/부정 
'''

data.isnull().sum() # 결측값 없음

# 2. token 생성 
reviews = data.reviews
# 1) reviews 단어 벡터 생성 (리스트화) 
reviews = reviews.tolist()

# 2) 문장 -> 단어 (토큰화)
# 주의: 리스트니까 string 하나씩 보면서 단어로 토큰화 한다. 
sentences = [word_tokenize(i) for i in reviews] 

# word2vector 객체 생성 
model = Word2Vec(sentences=sentences, window=5, min_count=1, sg=1 )

# 3. 함수 구현 
def word_search(word) :
    ws = model.wv.most_similar([word]) # ws는 (유사단어, 유사도) 
    return ws[:5]

print("Top5 유사단어: \n", word_search(input('키워드를 입력하세요: ')))





# 함수 호출 : 검색 단어 : action, people, society   
word_search(input('검색 단어 입력 : ')) 
'''
[('thrilling', 0.8083575963973999),
 ('slapstick', 0.8048508167266846),
 ('gory', 0.8038803935050964),
 ('exciting', 0.7957875728607178),
 ('courtroom', 0.7945571541786194)]
'''

