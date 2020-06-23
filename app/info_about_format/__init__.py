from flask import Blueprint

info_about_format = Blueprint('info_about_format', __name__)

from . import views, info