# where I create the create_app() function
from flask import  Flask
from .models import db

#create the application factory
def create_app(config_name):

  #initialize  blank app
  app = Flask(__name__)
  #configure the app
  app.config.from_object(f'config.{config_name}')

  # initialize extentions oon app
  db.init_app(app)
  # ma.init_app(app)
  # limiter.init_app(app)
  # cache.init_app(app)


  #register Blureprint when created
  return app

