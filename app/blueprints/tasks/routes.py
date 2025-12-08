from flask import request, jsonify
from app.models import Task, db
from .schemas import task_schema, tasks_schema
from marshmallow import ValidationError
from . import tasks_bp


# create Task
@tasks_bp.route('', methods=['POST'])
def create_task():
  # Load validate the request data
  try:
    data = task_schema.load(request.json)
  except ValidationError as e:
    return jsonify(e.messages), 400
  
  new_task = Task(**data) 
  db.session.add(new_task)
  db.session.commit()

  return task_schema.jsonify(new_task), 201

  #send a response 
  return jsonify({
    "message": "Task creation is Successful",
    "task": tasks_schema.dump(new_task)
  }), 201


#  view Task 
@tasks_bp.route('/<int:id>', methods=['GET'])
def get_task(id):
    task = db.session.get(Task, id)

    if task:
        return task_schema.jsonify(task), 200

    return jsonify({"error": "Task not found"}), 404


# update Profile
@tasks_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
  task= db.session.get(Task, task_id)

  if not task:
    return jsonify({'error':'Invalid task Id'}), 404
  
  try:
    data = task_schema.load(request.json)
  except ValidationError as e:
    return jsonify(e.messages), 400
  

  
  for key, value in data.items():
    setattr(task, key, value)

  db.session.commit()
  return jsonify({
    "message": "Succesfully updated task",
    "task": task_schema.dump(task)
  }), 200



#delete Task
@tasks_bp.route('/<int:task_id>',methods=['DELETE'])
def delete_task(task_id):
  task = db.session.get(Task, task_id)
  if task:
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Succesfully deleted task."}), 200
  return jsonify({"error": "Invalid task id"}), 404