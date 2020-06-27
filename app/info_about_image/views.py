from . import info_about_image
from flask import render_template, request, current_app
from werkzeug.utils import secure_filename
from ..for_dev.all_exts import all_to
import os
from PIL import Image
from .. import scheduler
import time
from .. import db, images
from ..models import Record

suitable = ["." + ext.lower() for ext in all_to]


def delete_file(*file_ids):
    """
    This function remove all files in 'filenames'
    :param filenames:
    :return: None
    """
    # sleep
    time.sleep(10)


    # then delete all files
    for file_id in file_ids:
        record = Record.query.filter_by(id=file_id).first()
        filename = record.image_filename
        os.remove(os.path.join(current_app.config['SUB_DIR'], filename))
        print(filename, 'is deleted')


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

    if format == '':
        return render_template('info.html', extension=format, suitable=suitable)

    if format.lower() not in suitable:
        return render_template('bad_extension.html', bad=format, good=[ext.replace('.', '') for ext in suitable])

    filename = images.save(request.files['image'])
    url = images.url(filename)
    new_record = Record(filename, url)
    db.session.add(new_record)
    db.session.commit()

    filepath = os.path.join(current_app.config.get('SUB_DIR'), filename)

    with current_app.app_context():
        scheduler.add_job(func=delete_file, trigger='date', args=[new_record.id], id=str(new_record.id))
    
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