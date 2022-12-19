#   extentions.py

def main():

    #   Initializing lists

    extensions = [
            #   Images
            ['gif',
            'jpg',
            'jpeg',
            'png',],

            #   Applications
            [
                'pdf',
                'zip',
            ],
            #   Other
            ['txt',]

                ]

    #   Prompting the user for file name with extention and handling the string
    prmpt = input('Type in a file name: ')

    #   Handling the string
    prmpt = prmpt.lower().strip()

    #   Slicing the string and removing the dot notation
    ext = prmpt[-4:].replace('.', '')

    #   Checking if the extension is a image
    if ext in extensions[0]:

        #   Retrieve the extension from list
        ext = extensions[0].index(ext)
        ext = extensions[0][ext]

        if ext == 'gif':print('image/gif')
        elif ext == 'png':print('image/png')
        else :print(f'image/jpeg')

    #   Checking if the extension is an Application
    elif ext in extensions[1]:

        #   Retrieve the extension from list
        ext = extensions[1].index(ext)
        ext = extensions[1][ext]
        print(f'application/{ext}')

#   Checking if the extension is a text
    elif ext in extensions[2]:

        #   Retrieve the extension from list
        ext = extensions[2].index(ext)
        ext = extensions[2][ext]
        print(f'text/plain')

    else:
        print('application/octet-stream')

main()