from flask import Flask 
from app import create_app
from app.models import db
from app.blueprints.categories.routes import seed_default_categories
from flasgger import Swagger

app = create_app('ProductionConfig')
Swagger(app, template_file='static/swagger.yaml')

with app.app_context():
  # db.drop_all()
  db.create_all() # creating our table from our DB models
  seed_default_categories()

@app.route('/')
def index():
    return "API is running!", 200
  

#app.run() # because of the gunicorn to run my app i do not need app.run() funcntion here anymore

#gunicorn flask_app:app