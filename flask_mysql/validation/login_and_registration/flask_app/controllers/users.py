from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


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

	if not User.validate_user(data):
		return redirect("/")

	pw_hash = bcrypt.generate_password_hash(request.form["password"])
	data["password"] = pw_hash

	user_in_db = User.register_user(data)

	session["user_id"] = user_in_db
	
	return redirect("/dashboard")


# dashboard landing page ========================================================
@app.route("/dashboard")
def dashboard():
	if session == []:
		return redirect("/")
	
	data = {
		"user_id" : session["user_id"]
	}

	user = User.get_user_by_id(data)
	return render_template("dashboard.html", user = user)


# login form post ===============================================================
@app.route("/login", methods=["POST"])
def login():
	data = {
		"email" : request.form["email"],
		"password" : request.form["password"]
	}
	user_in_db = User.get_by_email(data)
	if not User.validate_login(data):
		return redirect("/")

	session['user_id'] = user_in_db.id
	return redirect("/dashboard")


# logout and clear session ======================================================
@app.route("/logout")
def logout():
	session.clear()
	return redirect("/")