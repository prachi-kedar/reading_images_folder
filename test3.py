import os
from threading import *

# assign directory
directory = '/home/webwerks/Desktop/product-images'

def display():
    # Looping through the image folder
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Checking the extension of file
            if filename.endswith('.jpg') or filename.endswith('.JPG'):
                print(os.path.join(root, filename))


Thread_obj = Thread(target=display)

# Executing thread
Thread_obj.start()
