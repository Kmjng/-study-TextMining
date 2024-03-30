# -*- coding: utf-8 -*-
"""
nltk.corpus 모듈은 다음과 같은 경우에 사용된다.
말뭉치(corpus) : 자연어 분석 작업을 위해 만든 샘플 문서 집합을 말한다. 
단순히 소설, 신문 등의 문서를 모아놓은 것도 있지만 품사. 형태소, 등의 보조적 의미를 추가하고 쉬운 분석을 
위해 구조적인 형태로 정리해 놓은 것을 포함한다. 
주의 : 말뭉치 자료는 설치시에 제공되지 않고 download 명령으로 사용자가 다운로드 받아야 사용할 수 있다.

<< 활용 분야 >> 
1.예제 데이터 : nltk.corpus 모듈은 자연어 처리와 텍스트 분석에 대한 예제 코드 및 실습에 사용될 수 있는 다양한 말뭉치 데이터를 제공한다.
2.텍스트 분석 및 자연어 처리 연구: 말뭉치 데이터는 자연어 처리 모델의 학습 및 평가에 사용. 다양한 언어와 주제에 대한 말뭉치 데이터를 쉽게 액세스할 수 있다.
3.텍스트 분류 및 정보 검색 시스템: 말뭉치 데이터는 텍스트 분류 및 정보 검색 시스템의 개발과 평가에 사용. 훈련 데이터나 테스트 데이터로 말뭉치를 로드하고, 텍스트 분류기나 검색 모델을 구축하는 데 활용할 수 있다.
4.언어 모델링 및 통계적 분석: 말뭉치 데이터는 언어 모델링과 통계적 분석에 사용. 대량의 텍스트 데이터를 수집하고, 통계적 특성 및 패턴을 탐색하여 언어 모델을 개발하고 텍스트 데이터의 통계적 특성을 이해할 수 있다.
"""

import nltk # anaconda 제공 패키지 

# 주요 모듈 확인 
dir(nltk)
'''
corpus : 말뭉치 
stem : 어근 처리 
tag : 형태소 태깅 
tokenize : 토큰 생성 
'''

import nltk.corpus # 패키지.모듈 

# 주요 말뭉치
nltk.corpus
dir(nltk.corpus)
'''
brown : 브라운대학교 
gutenberg : 구텐베르크 전자책(eBooks) 
movie_reviews : 영화리뷰 
stopwords : 불용어 
words : 영어 단어 사전 
'''


### 1. 영화 리뷰 말뭉치(Movie Reviews Corpus) 로드

# 단계1 : 영화 리뷰 말뭉치 가져오기  
from nltk.corpus import movie_reviews # 객체(object)


# 단계2 : 영화 리뷰 말뭉치 데이터 다운로드
nltk.download('movie_reviews') 
#[nltk_data] Downloading package movie_reviews to
#[nltk_data]     C:\Users\Administrator\AppData\Roaming\nltk_data...
#[nltk_data]   Package movie_reviews is already up-to-date!


dir(movie_reviews)
'''
fileids() : 문서 파일 가져오기 
raw() : 원문(자연어) 가져오기
paras() : 문단 가져오기(토큰) 
sents() : 문장 가져오기(토큰)
words() : 단어 가져오기(토큰)
'''

# 단계3 : 영화 리뷰 말뭉치 내용 확인 

# 1) 말뭉치에서 문서 파일 가져오기   
fileids = movie_reviews.fileids() # 전체 문서 파일 로드 
len(fileids) # 2,000 : 전체 문장을 구성하는 개별 문서 파일
fileids[:5]
'''
['neg/cv000_29416.txt',
 'neg/cv001_19502.txt',
 'neg/cv002_17424.txt',
 'neg/cv003_12683.txt',
 'neg/cv004_12641.txt']
'''
fileids[-5:]
'''
['pos/cv995_21821.txt',
 'pos/cv996_11592.txt',
 'pos/cv997_5046.txt',
 'pos/cv998_14111.txt',
 'pos/cv999_13106.txt']
'''

# 긍정 or 부정 문서파일 가져오기 
pos_files = movie_reviews.fileids('pos') # 긍정 문서 파일 로드 
len(pos_files) # 1000
neg_files = movie_reviews.fileids('neg') # 부정 문서 파일 로드 
len(neg_files) # 1000


# 2) 문서 파일에서 원문 가져오기 
all_texts = movie_reviews.raw() # 전체 문서 파일에서 원문 가져오기 

first_text = movie_reviews.raw(fileids[0]) # 'neg/cv000_29416.txt' : 첫번째 문서 파일  

last_text = movie_reviews.raw(fileids[-1]) # 'pos/cv999_13106.txt' : 마지막 문서 파일  


# 토큰 생성에 필요한 말뭉치 데이터 다운로드 
nltk.download('punkt')

# 3) 문서 파일에서 문단 가져오기 : 문단별 단어(토큰)   
paras = movie_reviews.paras()
len(paras) #  2,000 : 2000개 문서파일에서 문단 가져오기 
paras # [ 문단1[[문장1],[문장2]], .... 문단n[[문장1],[문장2]] ]


# 4) 문서 파일에서 문장 가져오기 : 문장별 단어(토큰)     
sentences = movie_reviews.sents()
len(sentences) #  71,532 : 2000개 문서파일에서 문장 가져오기 

# 첫번째 문장의 단어(토큰화)
sentences[0]

# 마지막 문장의 단어 
sentences[-1]


# 5) 문서 파일에서 단어(토큰) 가져오기 
words = movie_reviews.words()
len(words) # 1,583,820 : 2000개 문서파일에서 단어 가져오기 
words


### 2. 구텐베르크(Project Gutenberg) 문서 로드

# 단계1 : 구텐베르크 말뭉치 가져오기 
from nltk.corpus import gutenberg # 객체 
 
dir(gutenberg)

# 단계2 : 구텐베르크 말뭉치 데이터 다운로드  
nltk.download('gutenberg')


# 단계3 : 말뭉치에 문서 파일 가져오기  
fileids = gutenberg.fileids()
print(fileids)
len(fileids) # 18개 

files = fileids[:5] # 5개의 문서파일 출력


# 단계4 : 문서파일에서 원문 가져오기
texts = gutenberg.raw(files) # 5개 문서파일에서 원문 가져오기  
print(texts)


# 단계5 : 문서파일에서 문단 가져오기   
paras = gutenberg.paras(files) # 5개 문서파일에서 문단 가져오기
print(paras) # 3중 list : [문단1[[문장1],[문장2]],...문단n[[문장1],[문장2]]] 
len(paras) # 문단 개수 : 30,157


# 단계6 : 문서파일에서 문장 가져오기  
sentences = gutenberg.sents(files) # 5개 문서파일에서 문장 가져오기
print(sentences)  # 2중 list
len(sentences) # 문장 개수 : 47,039
    
# 단계7 : 문서파일에서 단어 가져오기
guten_words = gutenberg.words(files) # 5개 문서파일에서 단어(토큰) 가져오기
print(guten_words) # 단일 list
len(guten_words) # 단어 길이 : 1,451,182



### 3. 영어 단어 말뭉치 로드 

# 단계1 : 단어 말뭉치 가져오기 
from nltk.corpus import words

# 단계2 : 단어 말뭉치 데이터 다운로드  
nltk.download('words')

# 단계3 : 말뭉치에서 단어 가져오기 
eng_words = words.words()
print(eng_words[:10])  # 처음 10개의 단어 출력
print(eng_words[-10:]) # 마지막 10개의 단어 출력
len(eng_words) # 236,736
   

    
### 4. 불용어(stopwords) 말뭉치 로드

# 단계1 : 단어 말뭉치 가져오기 
from nltk.corpus import stopwords

# 단계2 : 단어 말뭉치 데이터 다운로드  
nltk.download('stopwords')


# 단계3 : 말뭉치에서 불용어 가져오기  
stopwords = stopwords.words('english')
print(stopwords) # 인칭대명사, 접속사(and), 부사(about), 형용사(each), 조동사(should)
len(stopwords) # 179


# 단어 정제 : 불용어 제거 
new_words = [] 

for word in guten_words : 
    if word not in stopwords :
        new_words.append(word)

len(new_words) # 887,128
len(guten_words) # 1,451,182

1451182 - 887128 # 564054

# 미완성 불용어 : 대문자 불용어, 문장부호, 특수문자 제거 안됨  
    
    
    
    
    
    
    
    
    


