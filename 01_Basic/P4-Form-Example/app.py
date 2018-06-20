
from flask import Flask, request, render_template, url_for
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def signup():
    check = -1
    if request.method == 'POST':
        username = request.values['username']
        firstname = request.values['firstname']
        lastname = request.values['lastname']
        password = request.values['password']
        
        check = validation(username, firstname, lastname, password)

    return render_template('index.html', validcode=check)

def validation(username, firstname, lastname, password):

    if username == '' or firstname == '' or lastname == '' or password == '':
        return 1
    m = re.match(r'^[A-Za-z0-9]+$', username)
    if m is None:
        return 2
    m = re.match(r'^[A-Za-z-]+$', firstname)
    if m is None:
        return 3
    m = re.match(r'^[A-Za-z-]+$', lastname)
    if m is None:
        return 4
    if len(password) < 6:
        return 5

    return 0



if __name__ == "__main__":
    app.debug = True
    app.run()