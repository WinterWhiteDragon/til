from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index(name=None):
	return render_template("index.html", name=name)
	# index함수를 호출하면 render_template이 () 안에 있는 파일을 보여주게 만드는 것이다.

@app.route('/about')
def about(name=None):
	return render_template("about.html", name=name)


if __name__ == "__main__":
	app.run(host = '127.0.0.1')

# 웹 개발은 간단하다. 요청이 들어오면 응답을 하면 된다.