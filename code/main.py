import flask
from flask import Flask,render_template,request
import pymysql

def find_position_name(subject,cursor):
    search1 = "select position_name from resource where subject_name = '%s';"%(subject)
    cursor.execute(search1)
    lst1 = cursor.fetchall()
    lst2 = []
    lst3 = []
    for i in lst1:
        x = list(i)
        lst2.append(x)
    for i in lst2:
        for j in i:
            lst3.append(j)
    return lst3
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'flask_db'
app.config['MYSQL_CHARSET'] = 'utf8mb4'
@app.route('/',methods=['POST','GET'])
def index():
    mysql = pymysql.connect(host=app.config['MYSQL_HOST'],
                            port=app.config['MYSQL_PORT'],
                            user=app.config['MYSQL_USER'],
                            password=app.config['MYSQL_PASSWORD'],
                            db=app.config['MYSQL_DB'],
                            charset=app.config['MYSQL_CHARSET'])
    cursor = mysql.cursor()
    if request.method=='GET':
        return render_template('index.html',data1='no')
    if request.method=='POST':
        buttonA = request.values.get("buttonSearch")
        text = request.values.get("text")
        if (buttonA=='search'):
            if str(text)=="":
                    return render_template("index.html",data2="不能为空")
            sql = "SELECT `text` FROM `resource` WHERE `key` like '%"
            sql=sql+str(text)+"%'"
            cursor.execute(sql)
            result = cursor.fetchall()
            return render_template("index.html",data2=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=2222,debug=True)