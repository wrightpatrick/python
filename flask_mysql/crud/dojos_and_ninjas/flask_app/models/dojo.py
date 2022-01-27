from flask_app.config.mysqlconnection import connectToMySQL
#from flask import flash 

#EMAIL_REGEX = re.compile(r'')

class Dojo:
    def __init__(self, data):
        self.id = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# Create new Dojo Location ================================================
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return results


# List Dojo Locations ================================================
    @classmethod
    def all_dojos( cls ):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        
        return results

        dojos = []

        for dojo in results:
            dojos.append( cls(dojo) )

        return dojos


# Get one Dojos Location ================================================
    @classmethod
    def get_by_id( cls, data ):
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])

        
