from flask import Flask,request,render_template


app = Flask(__name__)



@app.route("/")
def home():
    print("hi")
    return '<h1>hi</h1>'


    

 
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8080,debug=True)