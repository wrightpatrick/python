from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

#from flask_app import b_crypt

@app.route("/ninjas")
def ninjas(): 
    dojos = Dojo.all_dojos()

    return render_template("ninjas.html", dojos = dojos)

@app.route("/create_ninja", methods=["POST"])
def create_ninja():

    data = {

        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]

    }

    Ninja.create_ninja(data)
    # dojos = Dojo.get_by_id(data)
    return redirect(f"/dojoshow/{session['dojo_id']}")

