from flask import Flask, render_template, request
from datetime import datetime
from waitress import serve
app = Flask(__name__)

@app.route("/")
def index():
	homepage = "<h1>楊子青Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/alex>顯示日期時間</a><br>"
    homepage += "<a href=/account?nick=Alex>傳送使用者暱稱</a><br>"
    homepage += "<a href=/about>子青簡介網頁</a><br>"
    return homepage

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