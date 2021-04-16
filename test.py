import os

import cv2

# Path of image folder
folder_path = '/home/webwerks/Desktop/product-images'

# Changing the current working directory to specified path
os.chdir(folder_path)

# Looping through the image folder
for f in os.listdir(folder_path):

    # Checking the extension of file
    if os.path.isfile(f) and (f.endswith('.jpg') or f.endswith('.JPG')):
        # Loading an image
        img = cv2.imread(f)
        # Displaying the image
        cv2.imshow('Img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
