from flask import request, jsonify
from app.models import Category, db
from .schemas import category_schema, categories_schema
from marshmallow import ValidationError
from . import categories_bp

# login

# create category
@categories_bp.route('', methods=['POST'])
def create_category():
  # Load validate the request data
  try:
    data = category_schema.load(request.json)
  except ValidationError as e:
    return jsonify(e.messages), 400
  
  new_category = Category(**data) 
  db.session.add(new_category)
  db.session.commit()

  return category_schema.jsonify(new_category), 201

  #send a response 
  return jsonify({
    "message": "Category creation is Successful",
    "category": categories_schema.dump(new_category)
  }), 201


#  view category 
@categories_bp.route('/<int:id>', methods=['GET'])
def get_category(id):
    category = db.session.get(Category, id)

    if category:
        return category_schema.jsonify(category), 200

    return jsonify({"error": "Category not found"}), 404


# update Profile
@categories_bp.route('/<int:category_id>', methods=['PUT'])
def update_category(category_id):
  category= db.session.get(Category, category_id)

  if not category:
    return jsonify({'error':'Invalid Category Id'}), 404
  
  try:
    data = category_schema.load(request.json)
  except ValidationError as e:
    return jsonify(e.messages), 400
  

  
  for key, value in data.items():
    setattr(category, key, value)

  db.session.commit()
  return jsonify({
    "message": "Succesfully updated category",
    "category": category_schema.dump(category)
  }), 200



#delete Profile
@categories_bp.route('/<int:category_id>',methods=['DELETE'])
def delete_category(category_id):
  category = db.session.get(Category, category_id)
  if category:
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Succesfully deleted category."}), 200
  return jsonify({"error": "Invalid category id"}), 404