from . import make_gif
from flask import render_template, request, url_for, current_app, send_file, flash, redirect
from werkzeug.utils import secure_filename
import os
from ..for_dev.all_exts import what_can
from ..pil_utils.make_gif import gif
from .. import scheduler
import time
from ..models import Record
from .. import db, images

def delete_file(file_ids):
    """
    This function remove all files in 'filenames'
    :param filenames:
    :return: None
    """
    time.sleep(1800)

    for file_id in file_ids:
        filename = Record.query.filter_by(id=file_id).first().image_filename
        os.remove(os.path.join(current_app.config['SUB_DIR'], filename))
        print(filename, 'is deleted')
        
@make_gif.route('/', methods=['GET'])
def index():
    """
        This function return contetn for http://domen/make_gif/
        """
    suitable = what_can('.gif')
    return render_template('make_gif.html', suitable=suitable)


@make_gif.route('/making', methods=['POST', 'GET'])
def making():
    """
    This function take image from form and convert it to the format taken from the same form, return page to downloading
    .gif
    If method == 'GET', function return page uploading mages to make them .gif
    :return:
    """
    if request.method == 'POST':
        files = request.files.getlist('test-file[]')

        all_files = []

        for file in files:
            filename = secure_filename(file.filename)
            name, image_format = os.path.splitext(filename)

            suitable = what_can('.gif')

            if image_format == '':
                return render_template('uploading.html', extension=image_format, suitable=suitable)

            if image_format.lower().replace('.', '') not in suitable:
                return render_template('bad_extension.html', bad=image_format, good=suitable)

            filename = images.save(file)
            url = images.url(filename)
            new_record = Record(filename, url)
            db.session.add(new_record)
            db.session.commit()

            all_files.append(new_record.id)
        gifka = gif(500, all_files)

        new_file = Record.query.filter_by(id=gifka).first()

        scheduler.add_job(func=delete_file, trigger='date', args=[all_files+[new_file.id]], id=str(new_file.id))

        return render_template('downloading.html', file=new_file.image_url)
