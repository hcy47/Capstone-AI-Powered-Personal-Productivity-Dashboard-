from flask import Blueprint

task_histories_bp = Blueprint('task_histories_bp', __name__)

from . import routes
