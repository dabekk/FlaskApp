from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/hello")
def hello():
	return "<h1>This is a separate hello page :)</h1>"

@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "POST":
		user = request.form["nm"]
		return redirect(url_for("user", usr=user))
	else:
		return render_template("login.html")

@app.route("/<usr>")
def user(usr):
	return "<h1>Hello member</h1>"

if __name__ == "__main__":
	app.run(debug=True)
