from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.dojo import Dojo

@app.route("/dojos")
def index():
    return render_template("index.html")

@app.route("/create_dojo", methods=["POST"])
def create_dojo():

    data = {
        "name" : request.form["name"]
    }

    # if not Name.validate_name(data):
    #     return redirect("/")

    #new_user_id = Name.create_name(data)
    Dojo.create_dojo(data)

    return redirect("/dojos")
