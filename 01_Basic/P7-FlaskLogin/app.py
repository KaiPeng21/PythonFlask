
from flask import Flask, request, url_for, redirect, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_bcrypt import Bcrypt

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s/%s' % (config.db_username, config.db_password, config.db_host, config.db_name)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = config.flask_secret

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(60))

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':

        return '''
        <form method="POST">
            <input type="text" name="username" placeholder="Enter Username">
            <input type="password" name="password" placeholder="Enter Password">
            <button type="submit">Login</button>
        </form>
        <a href="/signup">signup here</a>
        '''

    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()

    if user is not None and bcrypt.check_password_hash(user.password, password):
        login_user(user)

        if current_user.is_active:
            return render_template_string('''
                <h1>You logged in as {{ current_user.username }}</h1>
                <a href="/logout">Logout</a>
            ''', current_user=current_user)
    
    return '''
        <h1>Bad login</h1>
        <form method="POST">
            <input type="text" name="username" placeholder="Enter Username">
            <input type="password" name="password" placeholder="Enter Password">
            <button type="submit">Login</button>
        </form>
        <a href="/signup">signup here</a>
    '''
    

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == "GET":
        return '''
        <h1>Signup Form</h1>
        <form method="POST">
            <input type="text" name="username" placeholder="Enter username" />
            <input type="password" name="password" placeholder="Enter password" />
            <button type="submit">Sign Up</button>
        </form>
        '''

    username = request.form.get('username')
    password = request.form.get('password')
    encryptedPassword = bcrypt.generate_password_hash(password)

    signature = User(username=username, password=encryptedPassword)
    db.session.add(signature)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/protected')
@login_required
def protected():
    return '<h1>You can only access this page because you have logged in!</h1>'

if __name__ == "__main__":
    app.run(debug=True)


