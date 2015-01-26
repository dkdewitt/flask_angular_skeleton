
from flask import Flask, Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify, json
from flask.ext.restful import Resource, Api,reqparse, fields, marshal_with, marshal
from app import db, app
#api = Blueprint('api', __name__)

from werkzeug import check_password_hash, generate_password_hash

api = Api(app)
mod = Blueprint('usersrest', __name__, url_prefix='/')


class LoginResource(Resource):
    def __init__(self):
        
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('password', type=str, location='json')
        self.parser.add_argument('email', type=str, location='json')
        self.parser.add_argument('api_key', type=str, location='json')
        self.parser.add_argument('first_name', type=str, location='json')      
            
    resource_fields = {
                       'username'  : fields.String,
                       'email' : fields.String,                            
                       }
    

    def post(self):
        args = self.parser.parse_args()
        email = args['email']
        password = args['password']
        user =  db.session.query(User).filter(User.email == email).first()
        if user and verify_password(email, password):
            session['user_id'] = user.id  
            user.api_key = user.generate_auth_token()
            db.session.commit()
            p = {'api_key' :user.api_key, 'first_name' : user.first_name}
            #login_user(user)
            return p
        else:
            return ''

api.add_resource(LoginResource,  '/api/users/',  '/api/users/<user_id>')



class RegisterResource(Resource):
    def __init__(self):     
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('user_id', type=str, location='json')
        self.parser.add_argument('api_key', type=str, location='json')
        self.parser.add_argument('firstname', type=str, location='json')
        self.parser.add_argument('lastname', type=str, location='json')
        self.parser.add_argument('password', type=str, location='json')
        self.parser.add_argument('email', type=str, location='json')
        
    resource_fields = {
                       'user_id'  : fields.String,
                       'api_key' : fields.String,
                      
          
                       }
    

    
    @marshal_with(resource_fields)
    def get(self, user_id = None):
        if user_id is None:
            user_id = 1    
        user =  db.session.query(User).filter(User.id == user_id).first()
        p = {'api_key' :user.api_key}          
        return p
   
    
    def post(self):
        args = self.parser.parse_args()
        firstname =  args['firstname']
        lastname =  args['firstname']
        email = args['email']
        password = args['password']
        print email
        is_user = User.query.filter_by(email=email).first()
        if is_user is not None:
            flash('User already exists!')
            return redirect('/#/register/')
        user = User(first_name=firstname, last_name=lastname, email=email, password_hash='', username=email)
        user.hash_password(password)

        failed = False
        try:
            db.session.commit()

            user.api_key = user.generate_auth_token()

            login_user(user)
        except Exception as e:
            flash('failed %s' % user)
            db.session.flush()  # for resetting non-commited .add()
            return redirect('/#/register/')
        session.pop('user_id', None)
        session['user_id'] = user.id
        user = {'api_key' : user.api_key}
        return user

api.add_resource(RegisterResource,  '/api/register/')