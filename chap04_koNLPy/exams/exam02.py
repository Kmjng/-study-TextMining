'''
 문2) html02.html 웹 문서를 대상으로 형태소 분석으로 명사를 추출하여 
    출현빈도 Top5에 해당하는 단어와 빈도를 출력하시오. <출력결과> 참고
    
   <출력 결과>
   ----------------
   Top5 단어
   ----------------
   태그   ->   4
   링크   ->   3
   네이버   ->   3
   줄   ->   2
   바꿈   ->   2 
'''

from konlpy.tag import Okt # 형태소분석  
from collections import Counter # TopN 단어 선택  

# 1. file 자료 가져오기 
path = r"C:/ITWILL/3_TextMining/TextMining/data"
file = open(path + '/html02.html', encoding='utf-8')
data = file.read() # 문자열 읽기 
file.close()


print(data) # 형태소분석을 위한 텍스트 자료 


# 2. Okt 객체 생성 
okt = Okt()


# 3. 명사(단어) 추출 
data_nouns = okt.nouns(data)
print(data_nouns)
# 4. 단어 카운트 
counter = Counter(data_nouns)
print(counter)
'''
Counter({'태그': 4, '링크': 3, '네이버': 3, '줄': 2, 
'바꿈': 2, '다음': 2, '선': 1, '형식': 1, 
'속성': 1, '값': 1, '내용': 1, '창': 1})
'''
# 5. TopN 단어 선정
top5 = counter.most_common(n=5)
print(top5)
print('----------------\nTop5 단어\n----------------\n')
for i in top5 : 
    print(i[0],'  ->  ',i[1])

