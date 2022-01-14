from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo"


# @app.route('/<name>')
# def index(name):
#     return render_template('index.html', name = name)


# @app.route('/advanced')
# def advanced():

#     account_info = [
#         {'name' : 'Patrick', 'age' : 35}
#     ]
    
#     return "advanced rendering"
#     return render_template('index.html', name = name)



if __name__=="__main__":
    app.run(debug=True)