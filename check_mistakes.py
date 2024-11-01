import os
from tqdm import tqdm

path_imgs = '31.07.24'
path_check = 'need_check'
imgs = tqdm(os.listdir(path_imgs))
last_name = ''
last_price = 1_000_000
for ri in imgs:
    old_path = os.path.join(path_imgs,ri)
    new_path = os.path.join(path_check,ri)
    try:
        name,t,price = ri.split('_')
        price = float(price[:-4])
        if name == last_name:
            if 0.9 < price/last_price < 1.1:
                pass
            else:
                os.replace(old_path,new_path)
        last_name = name
        last_price = price
    except:
        os.replace(old_path,new_path)