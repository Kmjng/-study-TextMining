# -*- coding: utf-8 -*-
"""
1. text file 읽기 
2. 문장 추출
3. 명사 추출 : Okt
4. 단어 전처리 : 단어 길이 제한, 숫자 제외 
5. TopN 단어 선정
6. 단어구름 시각화(Word Cloud) 
"""

from konlpy.tag import Okt 
okt = Okt()

from wordcloud import WordCloud 

# 1. text file 읽기 
path = r"C:/ITWILL/3_TextMining/TextMining/data"

file = open(path + '/text_data.txt', mode='r', encoding='utf-8')
data = file.read()

print(data)
# 2. 문단(str) -> 텍스트 정규화  
ex_sents = okt.normalize(data)

print(ex_sents)
# 3. 명사 추출 
nouns = okt.nouns(ex_sents) 
print(nouns)


# 4. 단어 카운트 & 전처리 : 단어 길이 제한
nouns_count = {} # 단어 카운터 

for noun in nouns : 
    if len(noun) > 1 :
        nouns_count[noun] = nouns_count.get(noun, 0) + 1
print(nouns_count)        


# 5. TopN 단어 선정  
from collections import Counter # class 

word_count = Counter(nouns_count)
top5_word = word_count.most_common(5) # list형 (list 안에 튜플)


# 6. 단어 구름 시각화(word cloud) 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',   # 한글 폰트 경로 
          width=500, height=400,                          # 윈도 크기 
          max_words=100,max_font_size=150,                # 최대 빈도수와 폰트크기 
          background_color='white')                       # 배경색 
dir(wc)
'''
generate_from_frequencies(dict명('단어':빈도수))
generate_from_text(텍스트)
'''

# 단어구름 이미지 ★★★

# wordCloud와 의존관계의 Pillow 버전이 10 이상이면 버전 충돌돼서 
# 10미만으로 설치해주기 
wc_result = wc.generate_from_frequencies(dict(top5_word)) 

# 단어구름 시각화  
import matplotlib.pyplot as plt 

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()
