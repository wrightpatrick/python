from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_user", methods=["POST"])
def create_user():

    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "email" : request.form["email"]
        }

    # if not Name.validate_name(data):
    #     return redirect("/")

    User.create_user(data)

    return redirect("/")