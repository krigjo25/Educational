#   Responsories
import sys, os
from PIL import Image, ImageOps

def main():

    """
        #   Author :    krigjo25
        #   Date :      06.09-22

        #   if the user does not specify exactly two command-line arguments,
        #   if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
        #   if the input’s name does not have the same extension as the output’s name, or
        #   if the specified input does not exist.

    """

            #   Configuring the extentions
    path = os.path.splitext(sys.argv[1])
    path1 = os.path.splitext(sys.argv[2])

    #   Initializing a list
    ext = [
            '.jpg',
            '.jpeg',
            '.png',]

    #   Combining values to check the cmdline values.
    if len(sys.argv) < 3: sys.exit('Too few command line arguments')
    elif len(sys.argv) >= 4: sys.exit('Too many Command line arguments')
    elif path[1] not in ext or path1[1] not in ext :sys.exit('Not a valid extension name')
    elif path[1] != path1[1]: sys.exit('The extentions is not equal')

    else: return CropImage()

def CropImage():

    """

        #   Author :    krigjo25
        #   Date :      16.11-22
        #   if the user does not specify exactly two command-line arguments,
        #   if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
        #   if the input’s name does not have the same extension as the output’s name, or
        #   if the specified input does not exist.

    """
    try:
        with Image.open(sys.argv[1]) as photo, Image.open(r'shirt.png') as shirt:

            #   Crop the image
            top, bottom = shirt.size

            photo = ImageOps.fit(photo,(top, bottom))

            #   Paste the overlay and save the new photo
            photo.paste(shirt, shirt)
            photo.save(sys.argv[2])


    except FileNotFoundError as e: sys.exit(e)

if __name__ == '__main__':
    main()