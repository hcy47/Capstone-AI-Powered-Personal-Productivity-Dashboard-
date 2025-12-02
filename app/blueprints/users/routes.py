from flask import request, jsonify
from app.models import User, db
from .schemas import user_schema, users_schema
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from . import users_bp

# login

# Register/create user
@users_bp.route('', methods=['POST'])
def create_user():
  # Load validate the request data
  try:
    data = user_schema.load(request.json)
  except ValidationError as e:
    return jsonify(e.messages), 400
  
  data['password'] = generate_password_hash(data['password']) # reassigning the password to the hashed version of the passswrd

  user = db.session.query(User).where(User.email == data['email']).first() # Checking if a user exist in my db who has the same password as the one passed in

  if user:
    return jsonify({'error': 'Email already exist. Please log in!'}), 400
  
  new_user = User(**data) # creating a new user if user does not exist in data.
  db.session.add(new_user) # adding new user to the db
  db.session.commit() # committing the userto db

  #send a response 
  return jsonify({
    "message": "User creation is Successful",
    "user": user_schema.dump(new_user)
  }), 201


#  view profile - token auth eventually
@users_bp.route('/<int:user_id>' , methods=['GET'])
def get_user(user_id):
  user = db.session.get (User, user_id)
  if user:
    return user_schema.jsonify(user), 200
  return jsonify({"error": "Invalid user id"}), 400


# update Profile
@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
  user= db.session.get(User, user_id)

  if not user:
    return jsonify({'error':'Invalid User Id'}), 404
  
  try:
    data = user_schema.load(request.json)
  except ValidationError as e:
    return jsonify(e.messages), 400
  
  data['password'] = generate_password_hash(data['password'])

  existing = db.session.query(User).where(User.email == data['email']).first()
  if existing:
    return jsonify({'error': "Email already taken"})
  
  for key, value in data.items():
    setattr(user, key, value)

  db.session.commit()
  return jsonify({
    "message": "Succesfully updated account",
    "user": user_schema.dump(user)
  }), 200



#delete Profile
@users_bp.route('/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
  user = db.session.get(User, user_id)
  if user:
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Succesfully deleted user."}), 200
  return jsonify({"error": "Invalid user id"}), 404