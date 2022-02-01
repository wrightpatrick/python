from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Recipe:
	def __init__(self, data):
		self.id = data['id']
		
		self.recipe_name = data['recipe_name']
		self.descrption = data['description']
		self.instructions = data['instructions']
		self.date_made = data['date_made']
		self.under_30 = data['under_30']
		
		self.created_at = data['created_at']
		self.updated_at = data['updated_at']
		self.user_id = data['user_id']


# validate new recipe =========================================================
	@staticmethod
	def validate_recipe(data):
		is_valid = True
		if len(data['recipe_name']) < 3:
			flash("Name must be at least 3 characters.")
			is_valid = False
		if len(data['description']) < 3:
			flash("Description must be at least 3 characters.")
			is_valid = False
		if len(data['instructions']) < 3:
			flash("Instructions must be at least 3 characters long.")
			is_valid = False
		if (data['date_made'] == 0):
			flash("Must fill in date made field.")
			is_valid = False
		if len(data['under_30']) < 1:
			flash("Must fill in under 30 field.")
			is_valid = False
		return is_valid

# create new recipe ===========================================================
	@classmethod
	def create_recipe(cls, data):
		query = "INSERT INTO recipes (recipe_name, description, instructions, date_made, under_30, created_at, updated_at, user_id) VALUES (%(recipe_name)s, %(description)s, %(instructions)s, %(date_made)s, %(under_30)s, NOW(), NOW(), %(user_id)s);"
		results = connectToMySQL("recipes").query_db(query, data)
		return results

# list all recipes ============================================================
	@classmethod
	def list_recipes(cls, data):
		query = "SELECT * FROM recipes LEFT JOIN users on recipes.user_id = user_id;"
		results = connectToMySQL("recipes").query_db(query)

		recipes = []
		for row in results:
			recipe = cls(row)
			data = {
			"recipe_name" : row["recipe_name"],
			"description" : row["description"],
			"instructions" : row["instructions"],
			"date_made" : row["date_made"],
			"under_30" : row["under_30"],
			"user_id" : row["user_id"]
			}
			recipes.append(recipe)
		return recipes

# get one recipe ==============================================================
	@classmethod
	def get_recipe(cls, data):
		query = "SELECT * FROM recipes WHERE id = %(recipe_id)s;"
		result = connectToMySQL("recipes").query_db(query, data)
		if len(result) < 1:
			return False
		return cls(result[0])

# update one recipe ===========================================================
	@classmethod
	def update_recipe(cls, data):
		query = "UPDATE recipes SET recipe_name = %(recipe_name)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s, under_30 = %(under_30)s, updated_at = NOW() WHERE id = %(recipe_id)s"
		results = connectToMySQL("recipes").query_db(query, data)
		return

# delete recipe ===============================================================
	@classmethod
	def delete_recipe(cls, data):
		query = "DELETE FROM recipes WHERE id = %(recipe_id)s"
		results = connectToMySQL("recipes").query_db(query, data)
		return