from . import convert
from flask import render_template, request, url_for, current_app, send_file, redirect
from werkzeug.utils import secure_filename
from ..pil_utils import pil_demo
import os
from ..for_dev.all_exts import all_to, what_can
import time
from .. import scheduler



full = [key.upper() for key in all_to]
full.remove('ICNS')


def delete_file(*filenames):
    """
    This function remove all files in 'filenames'
    :param filenames:
    :return: None
    """
    # sleep
    time.sleep(10)


    # then delete all files
    for filename in filenames:
        os.remove(filename)
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
        name, format = os.path.splitext(filename)

        if format == '':
            return render_template('uploading.html', extension=extension, suitable=suitable)

        if format.lower().replace('.', '') not in suitable:
            return render_template('bad_extension.html', bad=format, good=suitable)

        to_save = os.path.join(current_app.config.get('BASE_DIR'), 'p1sttt/app/static/users_images/')
        to_work = os.path.join(current_app.config.get('BASE_DIR'), 'p1sttt/app/static/reformated/')

        file.save(os.path.join(to_save, filename))

        new_file = pil_demo.change_format(to_save + filename, extension)

        filename_1 = to_work + new_file

        filename_2 = to_save + name + format

        scheduler.add_job(func=delete_file, trigger='date', args=[filename_1, filename_2], id=filename)

        return render_template('downloading.html', file=url_for('static', filename='reformated/' + new_file))

    extension = request.args.get('extension')
    suitable = what_can(extension)
    return render_template('uploading.html', extension=extension, suitable=suitable)



@convert.route('/send_image/<filename>', methods=['GET'])
def send_image(filename):
    """
    This function just sends file
    """
    send_file(filename)

