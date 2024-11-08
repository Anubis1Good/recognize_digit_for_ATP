import os
from datetime import datetime

imgs_path = 'raw\images'

files = os.listdir(imgs_path)

for file in files:
    file_path = os.path.join(imgs_path,file)
    ctime = os.path.getmtime(file_path)
    dtime = datetime.fromtimestamp(ctime)
    cdate = str(dtime.date()).split('-')
    cdate.reverse()
    cdate = '.'.join(cdate)
    dir_path = os.path.join('raw',cdate)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    new_path = os.path.join(dir_path,file)
    os.replace(file_path,new_path)

    