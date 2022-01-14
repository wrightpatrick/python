from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"




@app.route('/') # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!' # Return the string 'Hello World!' as a response


@app.route('/<name>') # The "@" decorator associates this route with the function immediately following
def hello(name):
    return f'Hello {name}!' # Return the string 'Hello World!' as a response


@app.route('/users/<username>/<id>') # passing 2 parameters
def show_user_profile(username, id):
    print(username)
    print(id)
    return f'Hello fellow traveler. Username: {username}. ID: {id}'


@app.route('/success') # testing other routes
def success():
    return "success"












if __name__=="__main__": # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) # Run the app in debug mode.

