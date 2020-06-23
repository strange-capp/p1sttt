all_ext = '''BMP DIB EPS GIF ICNS ICO IM JPEG MSP PCX
PNG PPM SGI SPIDER TGA TIFF WebP
XBM BLP CUR DCX DDS FLI FLC FPX FTEX
GBR GD IMT IPTC
MCIDAS MIC MPO PCD PIXAR PSD WAL WMF
XPM PALM PDF XV BUFR FITS GTID HDF5 MPEG'''

full_ext = '''BMP DIB GIF ICNS ICO IM JPEG PCX
PNG PPM SGI TGA TIFF WebP SPI
XBM PDF'''

write_ext = ''

read_ext = '''BLP CUR DCX DDS FLI FLC FPX FTEX
GBR GD IMT IPTC
MCIDAS MIC MPO PCD PIXAR PSD WAL WMF
XPM'''

def text_to_list(text):
    to_list = []

    for i in text.split():
        to_list.append(i)

    return to_list


all_exten = text_to_list(all_ext)
full = text_to_list(full_ext)
write = text_to_list(write_ext)
read = text_to_list(read_ext)


if __name__ == '__main__':
    print(all_exten, full, write, read)


