from flask import Flask, render_template, request
from datetime import datetime
from waitress import serve
app = Flask(__name__)

@app.route("/")
def index():
	X = "作著 : 黃植達 <br>"
	X += "<a href = /mis>课程网页</a> <br>"
	X += "<a href = /alex?nick=Alex>个人介绍</a> <br>"
	X += "<a href = /account>表单传值</a><br>"
	return X

@app.route("/mis")
def course():
	return "<a href = https://drive.google.com/drive/folders/1JGHLQWpzT2QxSVPUwLxrIdYowijWy4h1><h1>資料庫管理</h1></a>"

@app.route("/alex", methods=["GET", "POST"])
def alex():
	user = request.values.get("nick")
	now = datetime.now()
	return render_template ("Alex.html",datetime = str(now), name = user)

@app.route("/account", methods=["GET", "POST"])
def account():
	if request.method == "POST":
		user = request.form["user"]
		pwd = request.form["pwd"]
		result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd
		return result
	else:
		return render_template("Account.html")

if __name__ == "__main__":
	#app.run()
	serve(app, host='0.0.0.0', port=8080)