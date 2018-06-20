
from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.values:
        return 'Hello ' + request.values['username']
    
    return render_template('template.html')

if __name__ == "__main__":
    app.debug = True
    app.run()