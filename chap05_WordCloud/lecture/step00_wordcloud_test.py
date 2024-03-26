# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 16:49:31 2024

@author: itwill
"""

# import test 
from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
import pandas as pd 

# (1) WordCloud 클래스생성자로 객체 생성
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
width=500, height=400,
max_words=100,max_font_size=150,
background_color='white')

# (2) 문단 (Paragraph)
from konlpy.tag import Okt
okt = Okt() 
para  = """"나는 홍길동 입니다. age는 23세 입니다. 
나는 대한민국 사람입니다.
대한민국을 사랑(love)합니다."""
okt.morphs(para) # list 
ex_sent = okt.normalize(para) 
print(ex_sent)
okt.nouns(para)
ex_pos = okt.pos(para) 
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

from collections import Counter # class 
counter = Counter(wc)
top5 = counter.most_common(n=5)
print(top5)

# WordCloud 객체 만들기
wc1 = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',   # 한글 폰트 경로 
          width=500, height=400,                          # 윈도 크기 
          max_words=100,max_font_size=150,                # 최대 빈도수와 폰트크기 
          background_color='white')                       # 배경색 


wc_result = wc1.generate_from_frequencies(dict(top5))

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기
plt.show()
