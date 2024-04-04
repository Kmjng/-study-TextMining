# -*- coding: utf-8 -*-
"""
jinja2 표현식 
 - 템플릿에서 python 객체 표현식 
"""

from flask import Flask, render_template # 템플릿 페이지 호출 

# 1. app 객체 생성 
app = Flask(__name__) 


# 2. 서버 요청 & 응답
@app.route("/") 
def index() :  
    return render_template('/step02/index.html') 


@app.route("/goodsInfo")
def info() :
    userName = "홍길동"  
    goodsList = ["배", "사과", "복숭아"]  
    return render_template('/step02/goodsInfo.html',
               userName=userName, goodsList=goodsList) 


# ★★★ 추가 템플릿에서 전송한 파라미터(객체) 받기 
@app.route("/userInfo/<userName>") # <파라미터명> 
# http://127.0.0.1/userInfo/홍길동
def userInfo(userName): 
    return render_template('/step02/userinfo.html', name = userName)

# 프로그램 시작점 
if __name__ == '__main__' :
    app.run(port=80) # app 실행  
    