
# Run this python script
# Enter localhost:5000 in your browser to view the result

from flask import Flask

app = Flask(__name__)

# P1-1 Route:
# Use @app.route() to define your route
# You should see "Hello World!" text in the root of localhost:5000
@app.route('/')
def index():
   return "<h1>Hello World!</h1>"

# P1-2 Passing value from URL:
# You should see "Hello <username>!" given "localhost:5000/user/<username>" 
@app.route('/user/<username>')
def user(username):
    return "<h1>Hello " + username + "!</h1>"
# Another example
@app.route('/age/<int:age>')
def age(age):
    return "I am " + str(age) + " years old."


# P1-3 URL for:
# You should see "This is example2. The url for example1 is /example1" given "http://localhost:5000/example2"
from flask import url_for

@app.route('/example1')
def example1():
    return "This is example1"
@app.route('/example2')
def example2():
    return "This is example2. The url for example1 is " + url_for('example1')


if __name__ == '__main__':
    app.debug = True
    app.run()