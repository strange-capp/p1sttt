from flask import Blueprint

make_gif = Blueprint('make_gif', __name__)

from . import views