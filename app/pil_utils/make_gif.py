from PIL import Image
import os
from ..pil_utils.pil_demo import change_size




def gif(speed, user_images, name=None):

    basename, format = os.path.splitext(os.path.basename(user_images[0]))

    if name:
        basename = name

    resized = []
    main_image = Image.open(user_images[0])
    gif_size = main_image.size

    for image in user_images:
        new_size_image = change_size(image, width=gif_size[0], height=gif_size[1])
        resized.append(new_size_image)

    images = []

    images.append(main_image)
    for file in resized:

        image = Image.open(file).convert('RGB')
        images.append(image)

    sub_dir = './app/static/reformated/'
    fullname = sub_dir + basename + '.gif'
    images[0].save(fullname, save_all=True, append_images=images[1:], optimize=False, duration=speed, loop=0)

    return fullname





