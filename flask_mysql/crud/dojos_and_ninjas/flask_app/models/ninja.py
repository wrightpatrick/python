from flask_app.config.mysqlconnection import connectToMySQL
#from flask import flash 
#from flask_app import bcrypt

#EMAIL_REGEX = re.compile(r' ')

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo.id']
        
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# Create a Ninja =============================================================
    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"

        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        return results


# Get all Ninjas =============================================================
    @classmethod
    def all_ninjas( cls ):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        
        return results

        ninjas = []

        for ninja in results:
            ninjas.append( cls(ninja) )

        return ninjas

# Get one Ninja ==============================================================
    @classmethod
    def get_ninja_by_id( cls, data ):
        query = "SELECT * FROM ninjas LEFT JOIN dojos on dojos.id = dojos_id WHERE dojos.id = %(dojo_id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        
        ninjas = []

        for ninjas in results:
            ninjas.append( cls(ninjas) )

        return ninjas