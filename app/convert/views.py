from . import convert
from flask import render_template, request, url_for, current_app, send_file, redirect
from werkzeug.utils import secure_filename
from ..pil_utils import pil_demo
import os
from ..for_dev.all_exts import all_to, what_can
import time
from .. import scheduler
from .. import images, db
from ..models import Record



full = [key.upper() for key in all_to]
full.remove('ICNS')


def delete_file(*file_id):
    """
    This function remove all files in 'filenames'
    :param filenames:
    :return: None
    """

    # sleep
    time.sleep(1800)


    # then delete all files
    for id in file_id:
        with current_app.app_context():
            sub_dir = current_app.config.get('SUB_DIR')
        record = Record.query.filter_by(id=id).first()
        filename = record.image_filename
        os.remove(os.path.join(sub_dir, filename))
        print(filename, 'is deleted')


@convert.route('/')
def index():
    """
    This function return content for http://domen/convert/
    """
    return render_template('convert.html', extensions=full)


@convert.route('/choose-file', methods=['POST', 'GET'])
def choose_file():
    """
    This function takes the file name and extension from the request.form object, if present, and displays a form
    to upload the image otherwise.
    Returns a page to download an image or a page to upload an image
    """
    if request.method == 'POST':
        extension = request.form.get('extension')

        suitable = what_can(extension)

        if extension.replace('.', '') not in [ext.lower() for ext in full]:
            return render_template('404.html'), 404

        file = request.files['image']
        filename = secure_filename(file.filename)
        name, image_format = os.path.splitext(filename)

        if image_format == '':
            return render_template('uploading.html', extension=image_format, suitable=suitable)

        if image_format.lower().replace('.', '') not in suitable:
            return render_template('bad_extension.html', bad=image_format, good=suitable)

        filename = images.save(request.files['image'])
        url = images.url(filename)
        new_record = Record(filename, url)
        db.session.add(new_record)
        db.session.commit()

        new_file = pil_demo.change_format(new_record.id, extension)
        new_file = Record.query.filter_by(id=new_file).first()

        scheduler.add_job(func=delete_file, trigger='date', args=[new_record.id, new_file.id], id=str(new_record.id))

        return render_template('downloading.html', file=new_file.image_url)

    extension = request.args.get('extension')
    suitable = what_can(extension)
    return render_template('uploading.html', extension=extension, suitable=suitable)


@convert.route('/send_image/<filename>', methods=['GET'])
def send_image(filename):
    """
    This function just sends file
    """
    send_file(filename)

