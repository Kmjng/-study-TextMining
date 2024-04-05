from flask import Flask, render_template, request

app = Flask(__name__) # App 생성 


@app.route('/')  
def index() :
    return render_template('/step04/index.html') # 메뉴 선택

    

@app.route('/service1') # Service1. 문서 유사도분석
def service1(): 
    return render_template('/step04/service1_main.html') 


@app.route("/service1_result", methods =['GET'])
def service1_result():
    genre = request.args.get('genre') # genre 를 get !
    e = '영화 장르가 선택되지 않았습니다.'
    if genre == 'none' : # 장르 선택되지 않았다면
        return render_template('/step04/error.html',err =e )
    else:
            
        # 유사도분류 모델 import 
        # 우리가 만든 모듈임~~
        from service.similarity_recommend import movie_search       
        
        
        sim_result, movie_title = movie_search(genre)
        # genre가 쿼리 역할 
        sim_title = zip(sim_result, movie_title)
        
        return render_template('/step04/service1_result.html',
                               sim_title= sim_title, genre = genre)


@app.route('/service2') # Service2. 문서분류(ML, AI) 
def service2(): 
    return render_template('/step04/service2_main.html') 


@app.route("/service2_result", methods =['POST'])
def service2_result():
    texts = request.form['texts']      
    
    # 텍스트분류 모델 import 
    from service.simple_classifier import classifier 
    y_pred_result = classifier(texts)  
    
    return render_template('/step04/service2_result.html',
                           texts=texts, y_pred_result=y_pred_result)    
            

if __name__ == '__main__':
    app.run(port=80)







