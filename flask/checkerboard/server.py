from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
session =[]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<num1>/<num2>')
def custom(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return render_template('index.html', num1= num1, num2= num2)



if __name__=="__main__":
    app.run(debug=True)