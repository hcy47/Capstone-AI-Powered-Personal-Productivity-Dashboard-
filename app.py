

from app import create_app
from app.models import db
from app.blueprints.categories.routes import seed_default_categories

app = create_app('DevelopmentConfig')

with app.app_context():
  # db.drop_all()
  db.create_all() # creating our table from our DB models
  seed_default_categories()
  

app.run()
