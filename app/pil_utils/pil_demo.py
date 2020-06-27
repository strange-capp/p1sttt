from PIL import Image
import os
from flask import current_app
from ..models import Record
from flask import url_for
from .. import db



def change_format(old_id, to_format, new_name=None):
    """This function changes the format of the image named "old" and saves it to a file with extension "to_format",
     returns path to image if all is well, otherwise returns False."""

    rec = Record.query.filter_by(id=old_id).first()
    imagename = rec.image_filename
    imagedir = os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], imagename)

    photo = Image.open(imagedir)

    base_name, old_format = os.path.splitext(os.path.basename(imagename))

    if new_name:
        base_name = new_name

    sub_dir = current_app.config.get('SUB_DIR')
    base_name += to_format
    new_photo = sub_dir + '/' + base_name

    print(new_photo)

    # check how to convert
    if to_format == '.xbm':
        photo = photo.convert('1')

    if to_format == '.spi':
        photo.save(new_photo, format='SPIDER')
    else:
        photo.save(new_photo)

    photo.close()

    new_record = Record(base_name, url_for('static', filename='photos/'+base_name, _external=True))
    db.session.add(new_record)
    db.session.commit()

    return new_record.id



def change_size(old_id, width=None, height=None, to_format=None, new_name=None):
    rec = Record.query.filter_by(id=old_id).first()
    imagename = rec.image_filename
    imagedir = os.path.join(current_app.config['UPLOADED_IMAGES_DEST'], imagename)

    photo = Image.open(imagedir)

    basename, format = os.path.splitext(imagename)

    if new_name:
        basename = new_name
    if to_format:
        format = to_format

    basewidth = width or photo.size[0]
    wpercent = (basewidth / float(photo.size[0]))
    new_height = height or int((float(photo.size[1]) * float(wpercent)))
    img = photo.resize((basewidth, new_height), Image.ANTIALIAS)

    sub_dir = current_app.config.get('SUB_DIR')
    basename += format
    new_photo = os.path.join(sub_dir, basename)

    img.save(new_photo)
    img.close()

    new_record = Record(basename, url_for('static', filename='photos/' + basename, _external=True))
    db.session.add(new_record)
    db.session.commit()

    return new_record.id

