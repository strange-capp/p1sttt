from . import info_about_image
from flask import render_template, request, current_app
from werkzeug.utils import secure_filename
from ..for_dev.all_exts import all_to
import os
from PIL import Image

suitable = ["." + ext.lower() for ext in all_to]


@info_about_image.route('/', methods=['GET'])
def index():
    """
    This function return contetn for http://domen/info_about_image/
    """
    return render_template('info_about_image.html', suitable=suitable)



@info_about_image.route('show_info/', methods=['POST'])
def show_info():
    file = request.files['image']
    filename = secure_filename(file.filename)
    name, format = os.path.splitext(os.path.basename(filename))

    if format.lower() not in suitable:
        return render_template('404.html'), 404

    if format.lower() not in suitable:
        return render_template('bad_extension.html', bad=format, good=[ext.replace('.', '') for ext in suitable])
    
    filepath = os.path.join(current_app.config.get('UPLOAD_FOLDER'), filename)
    
    file.save(filepath)
    file.close()
    
    image = Image.open(filepath)
    
    name = name + format
    mode = image.mode
    width = image.width
    height = image.height
    image_format = image.format
    size = os.path.getsize(filepath)
    

    return render_template('info.html', name=name, mode=mode,
                           width=width, height=height,
                           image_format=image_format, size=size)