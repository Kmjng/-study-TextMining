# -*- coding: utf-8 -*-
"""
1. pickle file 읽기 : news(12개월)
2. 문장 추출 : Okt
3. 명사 추출 : Okt
4. 전처리 : 단어 길이 제한, 숫자 제외 
5. TopN 단어 선정
6. 단어구름 시각화 : Word Cloud 
"""

from konlpy.tag import Okt # 형태소분석기  
okt = Okt() # object

import pickle # pickle file 읽기 
from wordcloud import WordCloud # 단어 구름 시각화 


# 1. pickle file load
path = r'C:/ITWILL/3_TextMining/TextMining/data'

# file load  # pickle.load(file)
file = open(path + '/news_data.pkl', mode='rb')
news_data = pickle.load(file)
file.close()

print(news_data)
type(news_data) # >> class 'list'
len(news_data)

# 2. 명사 추출 
nouns_word = [] # 명사 저장 

for sent in news_data : 
    for row in sent :       
        nouns_word.extend(okt.nouns(row))


# 3. 단어 전처리 : 단어 음절 길이 제한
final_nouns = [] 

for noun in nouns_word : 
    if len(noun) > 1 :
        final_nouns.append(noun)        

print(final_nouns)

# 4. TopN 단어 선정   
from collections import Counter 

word_count = Counter(final_nouns) 

print(word_count) # {'단어' : 빈도수} dict 

# '종합' 단어 삭제  
del word_count['종합']
del word_count['대통령']
del word_count['공개']
del word_count['한국']
del word_count['경찰']
del word_count['사망']
del word_count['속보']

top100_word = word_count.most_common(100) 
print(top100_word)



# 5. 단어구름 시각화
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')


wc_result = wc.generate_from_frequencies(dict(top100_word))

import matplotlib.pyplot as plt 

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()
