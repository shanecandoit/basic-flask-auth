
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)


@app.route('/')
def index():
    #return 'Index'
    return render_template('index.html')


@app.route('/profile')
def profile():
    #return 'Profile'
    return render_template('profile.html')


@app.route('/login')
def login():
    #return 'Login'
    return render_template('login.html')


@app.route('/logout')
def logout():
    #return 'Login'
    return render_template('index.html')

@app.route('/signup')
def signup():
    #return 'Signup'
    return render_template('signup.html')


if __name__ == '__main__':

    
    app.run(port=5000, debug=True)