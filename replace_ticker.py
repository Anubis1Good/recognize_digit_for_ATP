import os
import shutil
dir_path = 'replaced'
files = os.listdir(dir_path)
for file in files:
    old_name = os.path.join(dir_path,file)
    new_name = file.replace('RUAL','CNY')
    new_name_path = os.path.join(dir_path,new_name)
    os.rename(old_name,new_name_path)
    # path_file = os.path.join('08.08.24',new_name)
    # shutil.copy(new_name_path,path_file)