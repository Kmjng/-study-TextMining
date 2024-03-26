# -*- coding: utf-8 -*-
"""
문1) 2022년도 5월 5일 뉴스 기사를 수집한 텍스트 파일(news_texts.txt)를 
    대상으로 다음과 같은 단계별로 단어의 빈도수를 구하고 단어 구름으로 시각화하시오.
"""

from konlpy.tag import Kkma # 형태소 분석기 
from wordcloud import WordCloud # 단어구름 시각화 
from re import match # 단어 전처리 
from collections import Counter # TopN 단어 선정 

# 1. text file read 
path = r'C:/ITWILL/3_TextMining/TextMining/data'
file = open(path + '/news_texts.txt', mode='r', encoding="utf-8")
texts = file.read()
file.close()
print(texts)

kkma = Kkma() # 형태소 분석기


# 2. 문장 추출  
sents = [] 
for i in texts.split(sep='\w'):
    sents.append(i)
print(sents)    

# 3. 단어(명사) 추출  
nouns = [] # 중복 명사 저장
for sent in sents: 
    for noun in kkma.nouns(sent):
        nouns.append(noun)

print(nouns)

# 4. 단어 빈도수 & 전처리(단어 길이 1음절 제외, 서수로 시작하는 단어 제외)
nouns_count = {} # 단어 카운터 
for i in nouns: 
    if len(i)>1 and not(match('^[0-9]',i)):
        nouns_count[i]=nouns_count.get(i,0) +1 



print(nouns_count)
# 5. Top10 word 선정  
# dict인 nouns_count를 카운팅 
counter = Counter(nouns_count)
top10_word = counter.most_common(n=10)

print(top10_word)



# 6. 단어 구름 시각화 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')


wc_result = wc.generate_from_frequencies(dict(top10_word))

import matplotlib.pyplot as plt 

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()



