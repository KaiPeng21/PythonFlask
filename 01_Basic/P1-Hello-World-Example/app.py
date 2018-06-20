
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

# P1-4 Debug:
# Command out the first return statement and uncommand the second return statement.
# This will cause an error because value is a type of int.
# The browser will display the traceback error if 'app.debug' is True
# and only shows "Internal Server Error" if 'app.debug' is False
# app.debug should not be True for the final end product.
@app.route('/example3/<int:value>')
def example3(value):
    return 'This statement will not cause an error ' + str(value)
    #return 'This statement will cause an error because I did not perform a str typecast ' + value
    
if __name__ == '__main__':
    # P1-4 Debug:
    app.debug = True
    app.run()