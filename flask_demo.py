from flask import Flask, request, Response, jsonify, make_response, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid 
import jwt
import datetime
from functools import wraps
import json
import numpy as np
import requests
from string import Template
import threading

import sys
import signal
# for control-c capture
def handler(signal, frame):
  print('CTRL-C pressed!', file=sys.stdout)
  sys.exit(0)

signal.signal(signal.SIGINT, handler)

# Create the Flask object for the application
app = Flask(__name__)
# password in users table is encrypted 
app.config['SECRET_KEY']='Gdou@2021'
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite://///home/pzs/pzs/webcam/users.db' 
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://pzs:pzspzsPzs0!@localhost/blog?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)   
# we define the ORM model in the flask__sqlalchemy way, not sqlalchemy way
class Blog(db.Model):  
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.String(50))  
  name = db.Column(db.String(50))
  text = db.Column(db.String(255))

class Users(db.Model):
  public_id = db.Column(db.Integer, primary_key=True)
  password = db.Column(db.String(50))  
  name = db.Column(db.String(50))

@app.route("/")
def root_page(current_user):
    # if video_capture is None:
    #   print(f're-create video_capture')
    #   video_capture = cv2.VideoCapture(GSTREAMER_PIPELINE, cv2.CAP_GSTREAMER)
    return render_template('index.html',  user=current_user)

@app.route('/login', methods=['POST'])
def login_user(): 

#  auth = request.authorization   
   name = request.form['username']
   password = request.form['password']
  
#   if not auth or not auth.username or not auth.password:  
#      return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})    

   user = Users.query.filter_by(name=name).first()   
   if user is None:
      return render_template('login.html')
   if password == user.password:
      print(f'user={user.name}')
      token_str = {'public_id': user.public_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=60*24*2)}
      token = jwt.encode(token_str, app.config['SECRET_KEY']) 

      session['token'] = token
      return render_template('index.html',  user=user)
   else:
      return render_template('login.html')
#    return redirect('/start')

@app.route('/start', methods=['GET'])
def start_proc():
   return render_template('index.html')


def thread_proc():
    return
    
# check to see if this is the main thread of execution
if __name__ == '__main__':

    # Create a thread and attach the method that captures the image frames, to it
    process_thread = threading.Thread(target=thread_proc)
    isOpened = True
    process_thread.daemon = True

    # Start the thread
    process_thread.start()
    
    # start the Flask Web Application
    # While it can be run on any feasible IP, IP = 0.0.0.0 renders the web app on
    # the host machine's localhost and is discoverable by other machines on the same network 
    app.run("0.0.0.0", port="8000")

