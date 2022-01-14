from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo"


@app.route('/michael')
def michael():
    return "Michael"


@app.route('/say/<name>')
def say_hi(name):
    return f"Hello {name}"

@app.route('/repeat/<int:number>/<phrase>')
def repeat(number, phrase):
    return render_template('index.html', name=phrase, number=number)
    



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