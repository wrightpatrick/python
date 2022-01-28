from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User



# default landing page ========================================================
@app.route("/")
def index():
	return render_template("index.html")


# register new user form post =================================================
@app.route("/register_user", methods=["POST"])
def register_user():
	data = {
		"first_name" : request.form["first_name"],
		"last_name" : request.form["last_name"],
		"email" : request.form["email"],
		"password" : request.form["password"]
	}

	User.register_user(data)
	
	return redirect("/dashboard")


# dashboard landing page ========================================================
@app.route("/dashboard")
def dashboard():
	return render_template("index.html")
