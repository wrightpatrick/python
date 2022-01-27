from flask_app import app
from flask import render_template, redirect, request, session

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

#
@app.route("/dojos")
def index():
    dojos = Dojo.all_dojos()

    return render_template("index.html", dojos = dojos)

# create dojo method redirect to one dojo page ==================
@app.route("/create_dojo", methods=["POST"])
def create_dojo():
    
    data = {
        "name" : request.form["name"]
    }

    dojo_id = Dojo.create_dojo(data)

    return redirect(f"/dojoshow/{dojo_id}")

# One Dojo page ================================================
@app.route("/dojoshow/<dojo_id>")
def dojoshow(dojo_id):

    data = {
        "dojo_id" : dojo_id
    }
    dojo = Dojo.get_by_id(data)
    ninjas = Ninja.get_ninja_by_id(data)
    
    return render_template("dojoshow.html", ninjas = ninjas, dojo = dojo)