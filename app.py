from flask import Flask, render_template
import pymongo

app = Flask(__name__)


#Database
client = pymongo.MongoClient('localhost',27017)
db = client.user_login_system

#Routes
from user import routes

from user.models import User

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/user/signup', methods=['POST'])
def signup():
    print("hiiiiiiii")
    return User().signup()



if __name__ == "__main__":
    app.run(debug=True)