from flask import Flask


app = Flask(__name__)

@app.route('/')
	# 마지막에 /가 있는 이유는 "http://127.0.0.1:5000/"에서 마지막에 /를 넣으라는 뜻
		# 127.0.0.1은 host IP고 5000은 server에서 제공하는 port
		# 만약 이 뒤에 /만 넣으면 index()를 실행하고, /about을 넣으면 about()를 실행하라는 뜻
def index():
	return "Hello Flask!!!"

@app.route('/about')
def about():
	return "This is about : "


if __name__ == "__main__":
	app.run(host = '127.0.0.1')

# 웹 개발은 간단하다. 요청이 들어오면 응답을 하면 된다.