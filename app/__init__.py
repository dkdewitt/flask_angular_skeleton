from flask import Flask, render_template, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth

import os

app = Flask(__name__)
db = SQLAlchemy(app)
auth = HTTPBasicAuth()


from app.users.api import mod as usersRestModule
app.register_blueprint(usersRestModule)