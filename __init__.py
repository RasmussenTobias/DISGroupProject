from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '7d6971fd680e400cab2bc5dc9d947f57'

db = "dbname='arbBet' user='postgres' host='127.0.0.1' password=''"
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'