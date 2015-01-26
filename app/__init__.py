from flask import Flask, render_template, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth

import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pylync:12#$QWer@127.0.0.1/flask_skeleton'
db = SQLAlchemy(app)
auth = HTTPBasicAuth()


from app.users.api import mod as usersRestModule
app.register_blueprint(usersRestModule)


import views

db.create_all()