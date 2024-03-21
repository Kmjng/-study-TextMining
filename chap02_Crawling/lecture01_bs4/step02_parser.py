# -*- coding: utf-8 -*-
"""
웹문서 파싱(parsing)
"""

# 웹문서가 파일에 있으므로 urllib 모듈이 필요가 없음

from bs4 import BeautifulSoup # texts -> html or xml 변환 (구문 분석하기 위해)


path = r'C:/ITWILL/3_TextMining/TextMining/data' # 파일 경로 


# 1. HTML 문서 파싱 

# 1) 로컬 파일 읽기 
file = open(path + '/html_sample.html', mode='r', encoding='utf-8')
html_doc = file.read() 
file.close()

print(html_doc)
type(html_doc) # >> class 'str' (str으로 읽음) 

# 2) html 파싱
html = BeautifulSoup(html_doc, 'html.parser')
print(html)


# a 태그 전체 찾기 
a_tags = html.find_all('a')
print(a_tags) # list

    
# 2. XML(Extensible Markup Language) 문서 파싱     
file = open(path + '/xml_sample.xml', mode='r', encoding='utf-8')
xml_doc = file.read() 
print(xml_doc)    
    
