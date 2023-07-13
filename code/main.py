from flask import Flask,render_template,request
import pymysql

def find_position_name(subject,cursor):
    search1 = "select position_name from resource where subject_name like '%{}%';".format(subject)
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
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'flask_dbd'
app.config['MYSQL_CHARSET'] = 'utf8'
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
        return render_template('index5.html',data1='首页')
    if request.method=='POST':
        buttonA = request.values.get("buttonSearch")
        text = request.values.get("text")
        if (buttonA=='search'):
            if str(text)=="":
                    return render_template("index.html",data2="不能为空")
            else:
                positions = find_position_name(str(text),cursor)
                return render_template("index1.html", data2=positions)
        if (buttonA=='OK'):
            sql="select requirement from resource where position_name like '%{}%';".format(request.form.get('cate_1'))
            position=request.form.get('cate_1')
            cursor.execute(sql)
            lst1 = cursor.fetchall()
            lst2 = []
            x = list(lst1[0])
            y = x[0]
            for i in y:
                if i == "。":
                    y.replace("。","")
            str1 = ""
            for i in range(0,len(y) - 1):
                if y[i].isdigit() == True and y[i + 1] == ".":
                    str1 += "\n"
                    lst2.append(str1)
                    str1 = ""
                str1 += y[i]
            lst2.remove(lst2[0])
            return render_template("index2.html", position1=position,data1=lst2)
        if (buttonA == 'enter'):
            return render_template("index.html",)
        if (buttonA == 'back'):
            return render_template("index.html",)
        if (buttonA== 'share'):
            return render_template("index4.html",)
        if (buttonA=='submit'):
            return render_template("index3.html",)
        if (buttonA=='team'):
            return render_template("index5.html",)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=2222,debug=True)