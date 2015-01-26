from flask import make_response
from app import app

@app.route('/')

@app.route('/entities/')
@app.route('/entity/')
@app.route('/entity/<entity_id>')
@app.route('/contacts')
@app.route('/groups/')
@app.route('/register/')
@app.route('/login/')

def index(entity_id=''):
    #if session['user_id'] is None:

    return make_response(open('app/templates/base.html').read())