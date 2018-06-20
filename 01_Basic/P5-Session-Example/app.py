
from flask import Flask, request, session, redirect, url_for, escape
import os

app = Flask(__name__)

@app.route('/')
def home():
    if 'username' in session:
        return "You are logged in as %s" % escape(session['username']) + '''<br>
        <a href="logout">Logout here</a>
        '''
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session['username'] = request.values['username']
        return redirect(url_for('home'))

    return '''
        <h1>Login Form </h1>
        <form method="POST">
            <input type="text" name="username" placeholder="Enter your username"><br>
            <button type="submit" name="submit">Login</button>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "A Secret Key"
    app.run()