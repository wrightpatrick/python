from flask_app.config.mysqlconnection import connectToMySQL
#from flask import flash 

#EMAIL_REGEX = re.compile(r'')

class Dojo:
    def __init__(self, data):
        self.id = data['name']
        self.id = data['created_at']
        self.id = data['updated_at']
        
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
        query = """INSERT INTO users (name, created_at, updated_at,) VALUES (%(name)s, NOW(), NOW()"""
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return result