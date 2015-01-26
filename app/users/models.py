from flask import Flask,abort, g,Blueprint, jsonify, request, json, session, make_response
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.restful import Resource, Api,reqparse, fields, marshal_with, marshal
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
import datetime
from app import db, app, auth



class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(256))
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120))


    username = db.Column(db.String(100), unique=True)
    api_key = db.Column(db.String(255))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __init__(self, last_name = '', first_name = '', email ='', password_hash ='', username = ''):
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.password_hash = password_hash


    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        self.api_key =   str(s.dumps({'id': self.id}))
        db.session.commit()
        return s.dumps({'id': self.id})


    @staticmethod
    def verify_auth_token(token):
        print 'run'
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = db.session.query(User).get(data['id'])
        return user






@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    print 'token'
    print username_or_token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = db.session.query(User).filter_by(email=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
