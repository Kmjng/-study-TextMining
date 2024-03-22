import urllib.request as req  # url 가져오기 
from bs4 import BeautifulSoup

url = "https://news.daum.net/" # 다음 뉴스제공 사이트 

# 1. url 요청 
res = req.urlopen(url)
data = res.read() # 한글 깨짐 

help(data.decode)
# 2. 한글 디코딩 & html 파싱
src = data.decode('utf-8') 
html = BeautifulSoup(src, 'html.parser') 
        

# 3. news 관련 url 수집  
# 뉴스페이지 목록에 게시글마다 url이 지정되어 있다. 
# url 정보들을 가져오고 들어가서 내용물을 찾는다. 

# 1) list tag 수집 
lis = html.select('ul[class="list_newsissue"] > li') 
len(lis)
lis[0]

# 2) url 추출 (여기서 url은 href속성의 값임★)
urls = [] # url 저장 
for li in lis : #li 태그 요소들의 요소
    a = li.select_one('a[class="link_txt"]') # a 태그 추출 
    urls.append(a.get('href')) # href 속성 값 : url 출력    

print(urls)

# 목록들 url에 일일히 들어가서 제목 확인하기 
# 4. crawler 함수 정의
def crawler_fn(url): # 페이지 고정
    print('url :', url)
    try :
        # 1. url 요청 
        res = req.urlopen(url)
        data = res.read()  
        
        # 2. html 파싱
        src = data.decode('utf-8') 
        html = BeautifulSoup(src, 'html.parser')        
        
        # 3. 제목 수집  (★★★ url 의 html 정보에 대해서 써야함 ★★★)
        title = str(html.select_one('h3[class="tit_view"]').text).strip()
        
        # 4. 내용 수집  
        article = html.select('div.news_view > div.article_view > section > p')
        
        # 여러개 문단(p 태그) -> 한 개의 변수로 텍스트 누적 
        conts = ""
        for p in article :
            text = str(p.text).strip()
            conts += text # 텍스트 누적
    except Exception as e:  
        print('예외 발생 :', e) 
        
    return title, conts 

titles=[] # 뉴스 제목 
contents = [] # 뉴스 내용 

for url in urls: 
    titl, content = crawler_fn(url)   # 크롤러 함수 호출 
    titles.append(titl)
    contents.append(content)


len(titles) # >> 20 
len(contents) # >> 20 

print(titles)
print(contents)


# 2024-03-22 

# 데이터프레임으로 파일저장하기
import pandas as pd 
'''
[제목] [내용]
'''
daum_news = pd.DataFrame({'title':titles, 'news':contents})

print(daum_news)

path = r'C:/ITWILL/3_TextMining/TextMining/data'
daum_news.to_csv(path+'/daum_news.csv', index=False)
