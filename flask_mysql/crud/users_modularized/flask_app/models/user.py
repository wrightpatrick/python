from flask_app.config.mysqlconnection import connectToMySQL
#from flask import flash 

#EMAIL_REGEX = re.compile(r'')

class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # @staticmethod
    # def is_valid(data)
    #     is_valid = True
    #     if len(data["username"]) < 3:
    #         flash("Username must be at least 3 chars long")
    #         is_valid = False
    #     if not EMAIL_REGEX.match(data["email"[):
    #     return is_valid
        
        
        
    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, age, email, created_at, updated_at) VALUES (%(first_name)s , %(last_name)s , %(age)s , %(email)s , NOW() , NOW() )"""
        result = connectToMySQL("users_schema").query_db(query, data)
        return result

