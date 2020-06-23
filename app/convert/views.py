from . import convert
from flask import render_template, request, url_for, current_app, send_file
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
    time.sleep(1800)


    # then delete all files
    for filename in filenames:
        os.remove(os.getcwd()+'/app/static/'+filename)
        print(os.getcwd()+'/app/static/'+filename, 'is deleted')


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

        if format.lower().replace('.', '') not in suitable:
            return render_template('bad_extension.html', bad=format, good=suitable)

        file.save(os.path.join(current_app.config.get('UPLOAD_FOLDER'), filename))
        file.close()

        new_file = pil_demo.change_format('./app/static/users_images/' + filename, extension)

        filename_1 = 'reformated/' + new_file

        filename_2 = 'users_images/' + name + format

        scheduler.add_job(func=delete_file, trigger='date', args=[filename_1, filename_2], id=filename)

        print(scheduler.get_jobs())

        return render_template('downloading.html', file=url_for('static', filename=filename_1))

    extension = request.args.get('extension')
    suitable = what_can(extension)
    return render_template('uploading.html', extension=extension, suitable=suitable)



@convert.route('/send_image/<filename>', methods=['GET'])
def send_image(filename):
    """
    This function just sends file
    """
    send_file(filename)
