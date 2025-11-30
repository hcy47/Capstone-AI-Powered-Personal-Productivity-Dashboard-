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

  user = db.session.query(User).filter_by(User.email == data['email']).first() # Checking if a user exist in my db who has the same password as the one passed in

  if user:
    return jsonify({'error': 'Email already exist. Please log in!'}), 400
  
  new_user = User(**data) # creating a new user if user does not exist in data.
  db.session.add(new_user) # adding new user to the db
  db.session.commit() # committing the userto db

  #send a response 
  return jsonify({
    "message": "User creation is Successful",
    "user": user_schema.dump(new_user)
  })

  # create a new User in my database
  # send a response

#  view profile
# update Profile
#delete Profile