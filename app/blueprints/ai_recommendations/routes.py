from flask import request, jsonify
from app.models import Ai_recommendation, Task, db
from .schemas import ai_recommendation_schema, ai_recommendations_schema
from marshmallow import ValidationError
from . import ai_recommendations_bp
from datetime import datetime, timedelta


# create a simple recommendation for a task
@ai_recommendations_bp.route('/generate/<int:task_id>', methods=['POST'])
def generate_recommendation(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    # naive recommendation: schedule 1 hour before due_date if due_date exists else schedule next hour
    if task.due_date:
        recommended = task.due_date - timedelta(hours=1)
    else:
        recommended = datetime.now() + timedelta(hours=1)

    rec = Ai_recommendation(user_id=task.user_id or None, task_id=task.id, recommended_time=recommended, confidence=0.5)
    db.session.add(rec)
    db.session.commit()

    return ai_recommendation_schema.jsonify(rec), 201


# list recommendations for a user
@ai_recommendations_bp.route('/user/<int:user_id>', methods=['GET'])
def list_for_user(user_id):
    recs = db.session.query(Ai_recommendation).where(Ai_recommendation.user_id == user_id).all()
    return ai_recommendations_schema.jsonify(recs), 200