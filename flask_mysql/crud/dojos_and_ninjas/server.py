from flask_app import app
#controllers
from flask_app.controllers import dojos, ninjas

if __name__== "__main__":
	app.run(debug=True)
