# -*- coding: utf-8 -*-

# konlpy 설치 확인하기 
import konlpy 

dir(konlpy) # 모듈확인 : tag
dir(konlpy.tag)
"""
konlpy : 한글 형태소 분석을 제공하는 패키지 
 - 형태소 : 문장을 품사 단위로 쪼개는 과정 

주요 형태소 분석기
 'Hannanum': 한나눔(Hannanum)은 KAIST에서 개발한 한글 형태소 분석기, 복합명사 분해, 어근추출, 명사추출 등의 기능(java구현)
 'Kkma'    : 꼬꼬마(Kkma) -  서울대학교 연구실에서 개발한 형태소 분석기, 비교적 정확한 분석 결과를 제공(java구현)
 'Komoran' : 코모란(Komoran): Shineware에서 개발한 형태소 분석기, 대용량 말뭉치에서 학습된 모델을 사용하여 형태소 분석(java 구현)
 'Okt'     : Okt(Open Korean Text) - 형태소 분석 및 품사 태깅 기능을 제공(python 구현)
"""


from konlpy.tag import Hannanum


# Hannanum 형태소 분석기 생성
# (1) 객체 만들기  
hanna = Hannanum() #생성자 
dir(hanna)
'''
...'analyze', -> 복합어 명사 분해
'morphs', -> 형태소
'nouns', -> 문단/문장에서 명사로 추출
'pos',... -> (형태소, 품사)
'''

# 분석할 한글 문장
text = "한나눔 형태소 분석기를 사용해보는 예제입니다. 실습하자"


# 1) 명사 추출
nouns = hanna.nouns(text)
print("명사 추출 결과:", nouns) 


# 2) 형태소 분석  
morphs = hanna.morphs(text)
print("형태소 분석 결과:", morphs)


# 3) 형태소의 품사 태깅 (형태소, 품사)
pos_tags = hanna.pos(text)
print("품사 태깅 결과:", pos_tags)
'''
N: Noun (명사)
J: Josa (조사)
X: Josa appended to adjective stems (형용사에 붙이는 조사)
E: Eomi (어미)
P: PreEomi (선어말어미)
S: Symbol (기호)
'''

# 4) 문장의 구문 분석 
# 복합어 분해 -> 정보검색이나 자연어 처리시 

analyze = hanna.analyze(phrase=text) 
print(analyze)  
'''
ncn: Common noun (일반 명사)
nqq: Other proper noun (기타 고유 명사)
ncpa: Noun phrase (명사구)
jco: Conjunction (접속 조사)
xsva: Verb stem (동사 어간)
ecx: Case-marking particle (격 조사)
px: PreEomi (선어말어미)
etm: Ending particle (선어말어미)
jp: Josa Particle (조사 어미)
ef: Sentence-final ending (마침표)
sf: Final punctuation (문장 부호)
sy: Other punctuation (기타 부호)
''' 