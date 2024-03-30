# -*- coding: utf-8 -*-
'''
단어 전처리 : 특수문자 및 영문 불용어 단어 제거 
'''

import nltk # Anaconda3 기본 설치됨 


# 1. 구텐베르크(Project Gutenberg) 문서 로드

# 단계1 : 구텐베르크 말뭉치 가져오기 
from nltk.corpus import gutenberg


# 단계2 : 구텐베르크 말뭉치 데이터 다운로드 : 1회만   
nltk.download('gutenberg')


# 단계3 : 말뭉치에 문서 파일 가져오기  
fileids = gutenberg.fileids()
len(fileids) # 18개 

files = fileids[:5] # 5개의 문서파일 출력

  
# 단계4 : 말뭉치(5개 문서파일)에서 단어 가져오기
guten_words = gutenberg.words(files)
print(guten_words)
len(guten_words) # 1,451,182


    
# 2. 불용어(stopwords) 말뭉치 로드

# 단계1 : 단어 말뭉치 가져오기 
from nltk.corpus import stopwords

# 단계2 : 단어 말뭉치 데이터 다운로드  
nltk.download('stopwords')


# 단계3 : 말뭉치에서 불용어 가져오기  
stopwords = stopwords.words('english')
print(stopwords) 
len(stopwords) # 179



# 3. 구텐베르크 단어에서 불용어 제거 후 단어 추출 

# 1) text 전처리 함수
def clean_text(texts) : 
    from re import sub # 함수 임포트

    # 단계1 : 소문자 변경
    texts_re = [st.lower() for st in texts] # list -> string 추출 

    # 단계2 : 특수 문자나 문장부호(기호) 제거     
    texts_re2 = [sub(r'[^\w\d\s]', '', st) for st in texts_re]
    
    #단계3 : 숫자 제거 : 변수 = [실행문(method/func) for 변수 in 열거형객체]
    texts_re3 = [sub('[0-9]', '', st) for st in texts_re2]
       
    # 단계4 : 공백(white space) 제거
    texts_re4 = [st for st in texts_re3 if st !='']
    
    return texts_re4


# text 전처리 함수 호출 
clean_words = clean_text(guten_words) # 1차 정제  
clean_words
len(clean_words) # 1,165,611

1451182 - 1165611 # 285571


# 2) 영문 불용어 제거 : 2차 정제  
new_words = []

for word in clean_words :  
    if word not in stopwords :
        new_words.append(word)
        
len(new_words) # 544,603 
    
1451182 - 544603 # 906,579
    
   
    
   
    
   
    
   
    