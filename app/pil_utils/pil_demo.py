from PIL import Image
import os
import random



def change_format(old, to_format, new_name=None):
    """This function changes the format of the image named "old" and saves it to a file with extension "to_format",
     returns path to image if all is well, otherwise returns False."""

    photo = Image.open(old)

    base_name, old_format = os.path.splitext(os.path.basename(old))

    if new_name:
        base_name = new_name


    sub_dir = './app/static/reformated/'
    base_name += to_format
    new_photo = sub_dir + base_name

    # check how to convert
    if to_format == '.xbm':
        photo = photo.convert('1')

    if to_format == '.spi':
        photo.save(new_photo, format='SPIDER')
    else:
        photo.save(new_photo)

    photo.close()

    return base_name



def change_size(old, width=None, height=None, to_format=None, new_name=None):
    img = Image.open(old)

    basename, format = os.path.splitext(os.path.basename(old))
    if new_name:
        basename = new_name
    if to_format:
        format = to_format

    basewidth = width or img.size[0]
    wpercent = (basewidth / float(img.size[0]))
    new_height = height or int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, new_height), Image.ANTIALIAS)

    sub_dir = './app/static/reformated/'
    basename += format
    new_photo = sub_dir + basename

    img.save(new_photo)
    img.close()

    return new_photo

