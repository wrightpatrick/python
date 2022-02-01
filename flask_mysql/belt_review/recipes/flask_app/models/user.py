from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# create new user =============================================================
class User:
	def __init__(self, data):
		self.id = data['id']
		
		self.first_name = data['first_name']
		self.last_name = data['last_name']
		self.email = data['email']
		self.password = data['password']
		
		self.created_at = data['created_at']
		self.updated_at = data['updated_at']

		self.recipes = []

# validate new user ============================================================
	@staticmethod
	def validate_user(data):
		is_valid = True
		if len(data['first_name']) < 2:
			flash("First name must be at least 2 characters.")
			is_valid = False
		if len(data['last_name']) < 2:
			flash("Last name must be at least 2 characters.")
			is_valid = False
		if not EMAIL_REGEX.match(data['email']):
			flash("Email must be correct format.")
			is_valid = False
		if len(data['password']) < 5:
			flash("Password must be at least 3 characters long.")
			is_valid = False
		return is_valid

# validate login ==============================================================
	@staticmethod
	def validate_login(data):
		is_valid = True
		user_in_db = User.get_by_email(data)
		if not user_in_db:
			flash("Invalid Email/Password.")
			is_valid = False
		elif not bcrypt.check_password_hash(user_in_db.password, data['password']):
			flash("Invalid Email/Password.")
			is_valid = False
		return is_valid

# create new user =============================================================
	@classmethod
	def register_user(cls, data):
		query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
		results = connectToMySQL("recipes").query_db(query, data)
		return results

# validate existing email ======================================================
	@classmethod
	def get_by_email(cls, data):
		query = "SELECT * FROM users WHERE email = %(email)s;"
		result = connectToMySQL("recipes").query_db(query, data)
		if len(result) < 1:
			return False
		return cls(result[0])

# validate existing email ======================================================
	@classmethod
	def get_user_by_id(cls, data):
		query = "SELECT * FROM users WHERE id = %(user_id)s;"
		result = connectToMySQL("recipes").query_db(query, data)
		if len(result) < 1:
			return False
		return cls(result[0])