from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe


# default landing page ========================================================
@app.route("/recipe/new")
def recipe():
	return render_template("recipe_create.html")


# create new recipe ===========================================================
@app.route("/recipe/create", methods=["POST"])
def create_recipe():
	data = {
		"recipe_name" : request.form["recipe_name"],
		"description" : request.form["description"],
		"instructions" : request.form["instructions"],
		"date_made" : request.form["date_made"],
		"under_30" : request.form["under_30"],
		"user_id" : session["user_id"]
	}
	if not Recipe.validate_recipe(data):
		return redirect("/recipe/new")

	Recipe.create_recipe(data)

	return redirect("/dashboard")

# view 1 recipe ===============================================================
@app.route("/recipe/<int:recipe_id>")
def view_recipe(recipe_id):
	if "user_id" not in session:
		flash("Please login to access the dashboard.")
		return redirect("/")
	data = {
		"recipe_id" : recipe_id
	}
	recipe = Recipe.get_recipe(data)
	return render_template("instructions.html", recipe = recipe)


# edit recipe =================================================================
@app.route("/recipe/edit/<int:recipe_id>")
def edit_recipe(recipe_id):
	data = {
		"recipe_id" : recipe_id
	}
	recipe = Recipe.get_recipe(data)
	return render_template("edit_recipe.html", recipe = recipe)


# delete recipe ===============================================================
@app.route("/recipe/delete/<int:recipe_id>")
def delete_recipe(recipe_id):
	data = {
		"recipe_id" : recipe_id
	}
	recipe = Recipe.delete_recipe(data)
	return redirect("/dashboard")


# update recipe =================================================================
@app.route("/recipe/update/<int:recipe_id>", methods=["post"])
def update_recipe(recipe_id):
	data = {
		"recipe_name" : request.form["recipe_name"],
		"description" : request.form["description"],
		"instructions" : request.form["instructions"],
		"date_made" : request.form["date_made"],
		"under_30" : request.form["under_30"],
		"recipe_id" : recipe_id
	}
	if not Recipe.validate_recipe(data):
		return redirect(f"/recipe/edit/{recipe_id}")

	return redirect("/dashboard")