import flask
from flask import Flask,render_template,request
import pymysql

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='GET':
        return render_template('index.html',data='no')
    if request.method=='POST':
        buttonA = request.values.get("buttonSearch")
        text = request.values.get("text")
        if (buttonA=='search'):
            return render_template("index.html",data=text)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=2222,debug=True)
