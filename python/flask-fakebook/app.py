from flask import Flask, render_template, request
import sqlite3 as lite


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    if request.method == 'POST':
    	try:
    		name = request.form['name']
    			# signup.html에서 name을 입력하면 그 값을 여기에 저장한다
    		age = request.form['age']
    		email = request.form['email']

    		with lite.connect('C:/Users/tdbes/Documents/FASTCAMPUS Comp.Sci. School/최우영 강사 (github.com ulgoon)/flask-fakebook/fakebook_users.db') as conn:
    			# 여기서 db 파일을 사용하기 위해, sqlite3를 사용하여 connect한다
    			# 일반적으로 '='로 해도 되지만, 그러면 끝낼 때 disconnect를 해야한다. 이렇게하면 disconnect할 필요 없이 끝내면 된다.
    				# File I/O할 때처럼, file을 open하면 close해야 하는데, close를 쓰는 것을 피하기위해서 as in을 쓴다.
    			cur = conn.cursor
    				# fakebook_users.db 안에 cursor를 생성한다
    			cur.execute('INSERT INTO user(name, age, email) VALUES(?,?,?)', (name, age, email))
    				# ?은 문법... INSERT INTO & VALUES는 apostrophe로, str형태로 묶여있다. python에서 %s 쓰는 것과 비슷하다.
    			conn.commit()
    				# commit()은 명령할 것을 다 했고, 이제 내 명령을 반영하라는 뜻
    			msg = "signup complete"
# msg는 signup.html에 있고, 거기에 출력되는 것이다.
    	
    	except:
    		conn.rollback()
    			# db는 실패했을 때 rollback을 시켜야지, 아니면 부정접근이라고 판단하고 lockdown에 들어간다
    		msg = "signup failed"

    	finally:
    		return render_template("signup.html", msg = msg)
    			# 첫번째 msg는 signup.html 안의 msg를 의미, 두번째 msg는 여기 함수의 msg를 의미한다.
    		conn.close() 

# fakebook_users.db의 내용을 출력한다.
@app.route('/users')
def users():
	conn = lite.connect('C:/Users/tdbes/Documents/FASTCAMPUS Comp.Sci. School/최우영 강사 (github.com ulgoon)/flask-fakebook/fakebook_users.db')
	conn.row_factory = lite.Row

	cur = conn.cursor()
	cur.execute('SELECT * FROM user')

	rows = cur.fetchall()
	conn.close()

	return render_template("users.html", rows = rows)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='7070')
