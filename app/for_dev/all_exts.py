f_all = dict(
    bmp=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .webp .spi .xbm .pdf ",
    dib=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .webp .spi .xbm .pdf ",
    gif=".bmp .dib .gif .ico .im .pcx .png .tga .tiff .webp .spi .xbm .pdf ",
    icns=".bmp .dib .gif .ico .im .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    ico=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    im=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    jpeg=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    jpg=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    pcx=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    png=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    ppm=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    sgi=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    spi=".gif .im .tiff .webp .spi .xbm .pdf ",
    tga=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    tiff=".bmp .dib .gif .ico .im .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    webp=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .sgi .tga .tiff .webp .spi .xbm .pdf ",
    xbm=".bmp .dib .gif .ico .im .jpeg .jpg .pcx .png .ppm .tga .tiff .webp .spi .xbm .pdf ")

all_to = {}


for i in f_all:
    all_to[i] = f_all[i].split()


def what_can(ext):
    good = []

    for li in all_to:
        if ext in all_to[li]:
            good.append(li)

    return good
