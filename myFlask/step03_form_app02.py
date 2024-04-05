'''
템플릿 페이지에서 GET/POST 전송 자료 받기

<<작업순서>>
 1. 시작 페이지 : 사용자 정보 입력 & post 방식 전송   
 2. Flask 앱 : post 방식의 파라미터 받고 & 브라우저에 출력 
'''

from flask import Flask, render_template, request # request : 파라미터 받기 

app = Flask(__name__)


@app.route('/') # 시작 페이지
def index() :
    return render_template('/step03/post_method.html') # 시작 페이지


@app.route('/login', methods=['POST']) # 전송방식 
def login() :  
    userid = request.form['uid']
    passwd = request.form['pwd']
    # print(userid, passwd)
    return f'유저아이디:{userid}, 비번:{passwd}'

'''
http://127.0.0.1/login 화면에
유저아이디:hong, 비번:1234 가 출력됨
'''

if __name__ == '__main__':
    app.run(port=80)

