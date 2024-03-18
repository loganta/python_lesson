import fnmatch
import os

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff', '*.mp3', '*.mp4']
matches = []

for root, dirnames, filenames in os.walk("C:\\"):
    for extension in images:
        matches.extend(os.path.join(root, filename) for filename 
                       in fnmatch.filter(filenames, extension))