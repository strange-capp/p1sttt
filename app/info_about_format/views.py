from . import info_about_format
from flask import render_template, request
from .info import info

all_formats = [ext for ext in info]

@info_about_format.route('/', methods=['GET'])
def index():
    """
        This function return contetn for http://domen/info_about_format/
    """
    return render_template('info_about_format.html', extensions=all_formats)



@info_about_format.route('/show/', methods=['GET'])
def show():
    format = request.args.get('format')
    text = info[format]
    return render_template('show_format.html', format=format, text=text)