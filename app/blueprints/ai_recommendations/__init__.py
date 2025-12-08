from flask import Blueprint

ai_recommendations_bp = Blueprint('ai_recommendations_bp', __name__)

from . import routes
