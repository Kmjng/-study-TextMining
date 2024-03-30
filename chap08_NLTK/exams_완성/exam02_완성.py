# -*- coding: utf-8 -*-
"""
문2) 아래 경로의 피클(pickle) 파일을 로드하여 text 전처리 함수를 이용하여 단어를 전처리한 후 
    불용어를 제거한다. 이후 2~8음절 사이의 단어만 대상으로 Top50 단어를 단어구름으로 시각화하시오.
     
     조건> 파일경로 및 파일명 : 'C:\ITWILL\3_TextMining\data\brown_words.pkl'
"""

import pickle # pickle.dump(object, file) 
import nltk # 자연어 처리 

path = r'C:\ITWILL\3_TextMining\data'


# 단계1. pickle 파일 로드  
file = open(path + '/brown_words.pkl', mode='rb')
brown_words = pickle.load(file)
len(brown_words) # 22,491개 
brown_words

# 단계2 : 단어 전처리 : text 전처리 함수 이용 

# text 전처리 함수
def clean_text(texts) : 
    from re import sub # 함수 임포트

    # 단계1 : 소문자 변경
    texts_re = [st.lower() for st in texts] # list -> string 추출 


    # 단계2 : 특정 문자나 문장부호(기호) 제거     
    texts_re2 = [sub(r'[^\w\d\s]', '', st) for st in texts_re]
    
    #단계3 : 숫자 제거 : 변수 = [실행문(method/func) for 변수 in 열거형객체]
    texts_re3 = [sub('[0-9]', '', st) for st in texts_re2]
    
       
    # 단계4 : 공백(white space) 제거 : ''단어 제거(공백 아님)  
    texts_re4 = [st for st in texts_re3 if st != '' ]

    return texts_re4


# text 전처리 함수 호출 : 1차 정제 
clean_words = clean_text(brown_words) 
len(clean_words) # 19,817
len(brown_words) # 22491
22491 - 19817 # 2674


# 단계3 : 불용어 제거(단어 전처리) : 2차 정제  
from nltk.corpus import stopwords
nltk.download('stopwords')
stopwords = stopwords.words('english') 

'''
new_words = [] # 불용어 제거 단어 
for word in clean_words : 
    if word not in stopwords : 
        new_words.append(word)
'''

new_words = [word for word in clean_words if word not in stopwords]  
len(new_words) # 11,380


# 2~8음절 단어 선정
final_words = []

for word in new_words :  
    if len(word) > 1 and len(word) < 9 :
        final_words.append(word)

len(final_words) # 8938


# 단계4 : TopN 단어 선정   
from collections import Counter 

counter = Counter(final_words)

top50_word = counter.most_common(n=50) # Top50 단어 선정 


# 단계5 : 단어구름 시각화
from wordcloud import WordCloud # 단어 구름 시각화 

wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')


wc_result = wc.generate_from_frequencies(dict(top50_word))

import matplotlib.pyplot as plt 

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()
