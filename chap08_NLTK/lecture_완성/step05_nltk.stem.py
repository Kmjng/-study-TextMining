# -*- coding: utf-8 -*-
"""
4.nltk.stem: 단어의 표제어 추출(lemmatization)과 어간 추출(stemming)을 통해서 단어의표준화를 제공한다. 
"""

import nltk
from nltk.stem import WordNetLemmatizer # 표제어 추출과 어간 추출
'''
표제어(lemmatization : 라마디제이션)는 단어의 사전적인 기본 형태를 의미
표제어 추출은 단어의 다양한 형태를 하나의 표준 형태로 통합하여 
텍스트 데이터의 일관성을 확보하고 분석의 정확성을 높이는 데 사용된다.
예) is, am, are -> be

어간(stem)은 단어의 핵심 부분으로서 의미를 갖는 최소한의 형태
어간 추출은 단순히 규칙에 기반하여 접사를 제거하는 방식으로 수행된다.

예1) "running", "runs", "ran"과 같은 단어들은 모두 동일한 동사 "run"의 다른 형태
예2)  loved, loving, loves -> love  
'''
from nltk.tokenize import word_tokenize # 단어 토큰 생성 
nltk.download('punkt') # 토큰 생성에 필요한 데이터 
nltk.download('wordnet') # 단어의 의미와 관계에 필요한 데이터 
# 단어의 동의어, 반의어, 상하위어 등과 같은 단어 간의 관계 정의

# WordNetLemmatizer 객체 생성
lemmatizer = WordNetLemmatizer() # object 생성 
dir(lemmatizer)
# lemmatizer.lemmatize(word) 

# 단어 표준화 함수 정의
def word_lemmatization(text):
    # 문장을 단어로 토큰화
    words = word_tokenize(text) # 문장 -> 단어 생성(list)    
    
    # 각 단어의 표준화 수행 : 동사 어간 처리 
    lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in words]
    '''
    pos 파라미터 : 품사(part-of-speech) 태그 지정
    'a': 형용사 (Adjective)
    'n': 명사 (Noun)
    'v': 동사 (Verb)
    'r': 부사 (Adverb)
    pos 생략 시 기본값은 ='n' : 명사
    '''
        
    return ' '.join(lemmatized_words) # 표준화된 단어들 문장 반환

# 예시 문장
sentence = "I am running and eating food"

# 단어 표준화 적용
standardized_sentence = word_lemmatization(sentence)

standardized_sentence # 'I be run and eat food'












