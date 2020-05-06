"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField, TextAreaField
#from wtforms.validators import DataRequired, Email
from flask import Flask, request, current_app, make_response, render_template
import webbrowser
#from flask_script import Manager
#from jinja2 import Template
#from MyForms import MyForm

app = Flask(__name__)
#app.debug = True

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def index():
    """Renders a sample page."""
    webbrowser.open('http://fp.crc.ru', new=2)
    return render_template('index.html', name='Jerry')

@app.route('/career/')
def career():
    return 'Career Page'

@app.route('/feedback/')
def feedback():
    return 'Feedback'

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)

@app.route('/books/<genre>/')
def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

@app.route('/req')
def requestdata():
    return "Hello! Your IP is {} and you are using {}: ".format(request.remote_addr,  
                                                                request.user_agent)

@app.route('/app')
def appinfo():
    return "Hello! {} ".format(current_app.name)

@app.route('/set-cookie')
def set_cookie():
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "skyblue")
    res.set_cookie("favorite-font", "sans-serif")
    return res

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
