from flask import Blueprint, current_app

convert = Blueprint('convert', __name__)

from . import views
