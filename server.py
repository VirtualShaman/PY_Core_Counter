from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'temp'


@app.route('/')
def index():

    if 'count' in session:
        session['count'] += 1
    else:    
        session['count'] = 0

    return render_template('index.html')

@app.route('/reset')
def reset():

    session.pop('count')

    return redirect('/')

@app.route('/change')
def change():

    if 'count' in session:
        session['count'] += 2
    else:    
        session['count'] = 0

    return redirect('/')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)