from . import main
from flask import render_template



@main.route('/', methods=['GET', 'POST'])
def index():
    """
        This function return contetn for http://domen/
        """
    return render_template('index.html')