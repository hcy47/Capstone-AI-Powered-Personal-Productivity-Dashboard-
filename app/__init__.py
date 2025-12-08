# where I create the create_app() function
from flask import  Flask
from .models import db
from .extensions import ma
from .blueprints.users import users_bp
from .blueprints.categories import categories_bp
from .blueprints.tasks import tasks_bp
from .blueprints.ai_recommendations import ai_recommendations_bp
from .blueprints.task_histories import task_histories_bp
from .blueprints.dashboard.routes import dashboard_bp
from .blueprints.widgets.routes import widgets_bp

#create the application factory
def create_app(config_name):

  #initialize  blank app
  app = Flask(__name__)
  #configure the app
  app.config.from_object(f'config.{config_name}')

  # initialize extentions on app
  db.init_app(app)
  ma.init_app(app)

  # import models to reguster them with SQLAlchemy
  from app import models


  # plug in blueprints
  app.register_blueprint(users_bp, url_prefix='/users')
  app.register_blueprint(categories_bp, url_prefix='/categories')
  app.register_blueprint(tasks_bp, url_prefix='/tasks')
  app.register_blueprint(ai_recommendations_bp, url_prefix='/ai-recommendations')
  app.register_blueprint(task_histories_bp, url_prefix='/task-histories')
  app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
  app.register_blueprint(widgets_bp, url_prefix='/widgets')


  #register Blureprint when created
  return app

