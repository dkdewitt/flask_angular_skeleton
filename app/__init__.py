from flask import Flask, render_template, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth

import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ''

db = SQLAlchemy(app)
auth = HTTPBasicAuth()


app.config.from_object(__name__)
app.config.from_envvar('settings', silent=True)
import views

from app.users.api import mod as usersRestModule
app.register_blueprint(usersRestModule)