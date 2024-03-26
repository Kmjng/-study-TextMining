# -*- coding: utf-8 -*-
"""
1. csv file 읽기
2. 칼럼 선택  
3. 문장 추출 : Okt
4. 명사 추출 : Okt
5. 단어 전처리 : 단어 길이 제한 
6. TopN 단어 선정
7. Word Cloud
"""

import pandas as pd 
from konlpy.tag import Okt  
from wordcloud import WordCloud 


# 1. csv file 읽기
path = r'C:/ITWILL/3_TextMining/TextMining/data'
daum_news = pd.read_csv(path + '/daum_news.csv')


# 2. 칼럼 선택
daum_news.info()
news = daum_news.news # news 칼럼
type(news) # >> pandas.core.series.Series # 1차원
print(news)
okt = Okt() # Okt 객체 생성 : 형태소 분석기  


# 3. 문장 추출 : 문자열 변환 
# series 요소들 하나씩 보기
# series 모든 요소들이 str이 아니기 때문에, str 해주고 표준화한다.  
sents = [okt.normalize(new) for new in news ]


# 4. 명사 추출 : Okt 클래스 이용 
nouns = [] 
for sent in sents :
    for noun in okt.nouns(sent): 
        nouns.append(noun) 
        
print(nouns)

# 5. 단어 전처리 : (2음절 이상 단어 선정) 
final_nouns = [] # 선정 단어  

for noun in nouns :
    if len(noun) > 1 :
        final_nouns.append(noun)
        
print(final_nouns)

# 6. Top50 word  
from collections import Counter # class 

word_count = Counter(final_nouns)
top50_word = word_count.most_common(50) # top50 
print(top50_word)


# 7. word cloud 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')


wc_result = wc.generate_from_frequencies(dict(top50_word))

import matplotlib.pyplot as plt 

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()
