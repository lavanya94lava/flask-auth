from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)

app.secret_key = "xcvbnm=9655e45rvtbhjkl,,mijhu"


#Database
client = pymongo.MongoClient('localhost',27017)
db = client.user_login_system

#Routes
from user import routes

from user.models import User

#Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/user/signup', methods=['POST'])
def signup():
    print("hiiiiiiii")
    return User().signup()

@app.route('/user/signout')
def signout():
    return User().signout()



if __name__ == "__main__":
    app.run(debug=True) 