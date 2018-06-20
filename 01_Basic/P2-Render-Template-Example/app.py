
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Append a username in the URL'

@app.route('/<username>')
def user(username):
   return render_template('template.html', username=username)

if __name__ == "__main__":
    app.debug = True
    app.run()