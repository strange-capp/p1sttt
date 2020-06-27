from PIL import Image
import os
from ..pil_utils.pil_demo import change_size
from flask import current_app
from ..models import Record
from flask import url_for
from .. import db




def gif(speed, user_images, name=None):

    rec = Record.query.filter_by(id=user_images[0]).first()
    imagename = rec.image_filename
    imagedir = os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], imagename)

    basename, format = os.path.splitext(imagename)

    if name:
        basename = name

    resized = []

    main_image = Image.open(imagedir)

    gif_size = main_image.size

    for image in user_images:
        new_size_image = change_size(image, width=gif_size[0], height=gif_size[1])
        resized.append(new_size_image)

    images = []

    images.append(main_image.convert('RGB'))

    for file in resized:
        rec = Record.query.filter_by(id=file).first()
        imagename = rec.image_filename
        imagedir = os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], imagename)
        image = Image.open(imagedir).convert('RGB')
        images.append(image)

    sub_dir = current_app.config.get('SUB_DIR')
    fullname = os.path.join(sub_dir, basename + '.gif')


    images[0].save(fullname, save_all=True, append_images=images[1:], optimize=False, duration=speed, loop=0)

    new_record = Record(basename + '.gif', url_for('static', filename='photos/' + basename + '.gif', _external=True))
    db.session.add(new_record)
    db.session.commit()

    return new_record.id





