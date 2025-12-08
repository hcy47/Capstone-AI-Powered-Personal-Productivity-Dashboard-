from flask import Blueprint

widgets_bp = Blueprint('widgets_bp', __name__)

from . import routes
