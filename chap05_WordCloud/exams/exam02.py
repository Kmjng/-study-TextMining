# -*- coding: utf-8 -*-
"""
문2) review_data.csv 파일의 'review2' 칼럼을 대상으로 다음과 같이 
    단계별로 단어의 빈도수를 구하고, 단어 구름으로 시각화하시오.
"""
import pandas as pd
from konlpy.tag import Okt
from wordcloud import WordCloud 

# 1. file load 
path = r'C:/ITWILL/3_TextMining/TextMining/data'
review_data = pd.read_csv(path + '/review_data.csv', encoding='utf-8')

review_data.info()
'''
RangeIndex: 34525 entries, 0 to 34524
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   id       34525 non-null  int64 
 1   review   34525 non-null  object
 2   label    34525 non-null  int64 
 3   review2  34525 non-null  object  -> 선택할 칼럼 
''' 

# 2. review2 칼럼 선택 # Series 
review2 = review_data.review2
print(review2)

# 3. 문장 추출 :  Okt 클래스 이용
okt = Okt()
sents_r = [okt.normalize(str(i)) for i in review2] 
print(sents_r)

# 4. 명사 추출 : Okt 클래스 이용 
nouns_r =[]
for sent in sents_r : 
    nouns_r.extend(okt.nouns(sent))

print(nouns_r)
# 5. 전처리 : 2음절~5음절 단어 선정  
nouns=[]
for noun in nouns_r : 
    if len(noun) >=2 and len(noun) <=5 : 
        nouns.append(noun)



# 6. Top100 word 선정  
top100_word = []
from collections import Counter 
counter = Counter(nouns) 
top100_word = counter.most_common(100)
print(top100_word)

# 7. 단어 구름 시각화 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')


wc_result = wc.generate_from_frequencies(dict(top100_word))

import matplotlib.pyplot as plt 

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()
