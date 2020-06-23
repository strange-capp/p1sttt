from flask import Blueprint

info_about_image = Blueprint('info_about_image', __name__)

from . import views