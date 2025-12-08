from flask import request, jsonify
from app.models import Category, db
from .schemas import category_schema, categories_schema
from marshmallow import ValidationError
from . import categories_bp



def seed_default_categories():
  default_categories = [
    {"name": "Work", "icon": "💼", "color": "blue"},
    {"name": "Personal", "icon": "🏠", "color": "purple"},
    {"name": "Health", "icon": "🏋️", "color": "green"},
    {"name": "Education", "icon": "📚", "color": "yellow"},
    {"name": "Finance", "icon": "💰", "color": "orange"},
  ]
  for cat in default_categories:
    exists = db.session.query(Category).filter_by(name=cat['name']).first()
    if not exists:
      new_category = Category(**cat)
      db.session.add(new_category)
  db.session.commit()
  print("Category set succesfully")


#get route
@categories_bp.route('', methods=['GET'])
def get_all_categories():
    all_categories = db.session.query(Category).all()
    return categories_schema.jsonify(all_categories), 200



