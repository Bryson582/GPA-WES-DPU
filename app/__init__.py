from flask import Flask
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
bcrypt = Bcrypt(app)
bootstrap = Bootstrap(app)
# db = SQLAlchemy(app) #实例化
app.config.from_object(Config)

from app.routes import *
