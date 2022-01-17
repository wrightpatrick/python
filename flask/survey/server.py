from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'a;sdhahw;thds'

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    print(session)
    
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')


@app.route('/result')
def result():
    return render_template('result.html')




if __name__=="__main__":
    app.run(debug=True)