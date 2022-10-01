from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.secret_key = '413c2f9b2a2c84c8073240c7b57ab2ee115da3d90c76d9db17ad98290a469f81'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/plus2')
def plus2():
    session['count'] += 1
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)