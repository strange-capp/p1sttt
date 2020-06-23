from . import make_gif
from flask import render_template, request, url_for, current_app, send_file, flash, redirect
from werkzeug.utils import secure_filename
import os
from ..for_dev.all_exts import what_can
from ..pil_utils.make_gif import gif
from ..pil_utils.pil_demo import change_size
from PIL import Image
from .. import scheduler
import time

def delete_file(filenames_users, reformated):
    """
    This function remove all files in 'filenames'
    :param filenames:
    :return: None
    """
    time.sleep(1800)

    for filename in filenames_users:
        os.remove(os.getcwd()+'/app/static/users_images/'+filename)
        print(os.getcwd()+'/app/static/users_images/'+filename, 'is deleted')


    for filename in reformated:
        os.remove(os.getcwd() + '/app/static/reformated/' + filename)
        print(os.getcwd() + '/app/static/reformated/' + filename, 'is deleted')
        
        
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
        print(files)
        all_files = []
        to_delete = []

        for file in files:
            filename = secure_filename(file.filename)

            to_delete.append(filename)

            name, format = os.path.splitext(filename)

            suitable = what_can('.gif')

            if format.lower().replace('.', '') not in suitable:
                return render_template('bad_extension.html', bad=filename + ' ' + format, good=suitable)

            pathname = os.path.join(current_app.config.get('UPLOAD_FOLDER'), filename)

            file.save(pathname)
            file.close()

            width, height = Image.open(pathname).size

            pathname = change_size(pathname, width=width, height=height)

            all_files.append(pathname)
        gifka = gif(500, all_files)
        filename = 'reformated/' + os.path.basename(gifka)
        scheduler.add_job(func=delete_file, trigger='date', args=[to_delete, to_delete+[os.path.basename(gifka)]], id=filename)
        return render_template('downloading.html', file=url_for('static', filename=filename))
