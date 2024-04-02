# -*- coding: utf-8 -*-
"""
문2) 한국영화 후기(review_data.csv) 파일을 대상으로 아래와 같은 조건으로
     키워드를 입력하여 관련 영화 후기를 검색하는 함수를 정의하시오.   

 <조건1> 사용할 칼럼 : review2 
 <조건2> 사용할 문서 개수 : 1번째 ~ 5000번째   
 <조건3> 코사인 유사도 적용 - 영화 후기 검색 함수
         -> 검색 키워드와 가장 유사도가 높은 상위 3개 review 검색  
 <조건4> 검색 키워드 : 액션영화, 시나리오, 중국영화 
        -> 위 검색 키워드를 하나씩 입력하여 관련 후기 검색   
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. dataset load 
path = r'C:/ITWILL/3_TextMining/TextMining/data'
data = pd.read_csv(path + "/review_data.csv")
data.info() 
'''
 0   id       34525 non-null  int64 
 1   review   34525 non-null  object
 2   label    34525 non-null  int64 
 3   review2  34525 non-null  object -> 사용할 칼럼 (34525개의 문서) (정제 돼있음..)
'''
print(data.head())
print(data.iloc[1:4:2])

# 사용할 문서 5,000개 제한  
review = data.review2[:5000] # 1번째 ~ 5000번째 문서 
tfidf = TfidfVectorizer(stop_words='english')
dtm = tfidf.fit_transform(review)
dtm_arr = dtm.toarray()
dtm_arr.shape # >> (5000, 19361) 

# 2. sparse matrix 생성 : overview 칼럼 대상 
review = data.review

# 3. cosine 유사도 : 영화 후기 검색 함수  
def review_search(query) : 
    query = [query]
    dtm_q = tfidf.transform(query) 
    dtm_q_arr = dtm_q.toarray()
    
    sim= cosine_similarity(dtm_arr, dtm_q_arr) 
    sim = sim.reshape(5000)
    sim_idx = sim.argsort()[::-1]
    global review 
    
    for idx in sim_idx[:5]: 
        print(f'유사도: {sim[idx]}\nreview: {review[idx]}\n')

# 4. 검색 키워드 : 액션영화, 시나리오, 중국영화   
review_search(input('검색할 키워드 입력 : '))

'''
검색할 키워드 입력 : 공포
유사도: 0.4842152464317632
review: 내가 본 공포 영화 중 유일하게 무서웠음

유사도: 0.37621859918281114
review: 이게 공포 영화냐, 코미디 영화냐

유사도: 0.3232136647270204
review: 너무 쓰레기 취급을 받네. 은근히 무서운데 ㅋ 일본 최고의 공포

유사도: 0.3112328646324184
review: 스릴, 공포, 반전 모두 그냥 그런 수준 2시간 안 넘는게 참 다행

유사도: 0.30807465530447475
review: 이거 왜 계속 만드는거야.. 제작비가 남아도나 18.. 유치 찬란한 초딩 공포 영화 18
'''