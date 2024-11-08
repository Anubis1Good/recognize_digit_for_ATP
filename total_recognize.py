import os
from recognize import recognize


path_folders = 'raw'

list_folders = os.listdir(path_folders)

for folder in list_folders:
    folder_path = os.path.join(path_folders,folder)
    recognize(folder_path)
    # break