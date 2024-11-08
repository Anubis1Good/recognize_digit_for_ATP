import os
import cv2
import numpy as np
import easyocr
from tqdm import tqdm
from config import ColorsBtnBGR

reader = easyocr.Reader(['en'])


chart_cords = (686,400,1362,700)
def recognize(path_imgs):
    # path_imgs = '31.07.24'
    imgs = tqdm(os.listdir(path_imgs))

    for ri in imgs:
        if ri.count('_') < 2:
            path_img = os.path.join(path_imgs,ri)
            img = cv2.imread(path_img)
            img = img[chart_cords[1]:chart_cords[3],chart_cords[0]:chart_cords[2]]
            mask1 = cv2.inRange(img,ColorsBtnBGR.cur_price_1,ColorsBtnBGR.cur_price_1)
            mask2 = cv2.inRange(img,ColorsBtnBGR.cur_price_2,ColorsBtnBGR.cur_price_2)
            mask = cv2.add(mask1,mask2)
            cords = np.argwhere(mask)
            try:
                img = img[cords[0][0]:cords[-1][0],cords[0][1]:cords[-1][1]]
                img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                img = cv2.resize(img,(img.shape[1]*10,img.shape[0]*10))
                img2 = img.copy()
                kernel = np.ones((5,7))
                img = cv2.erode(img,kernel)
                _,img = cv2.threshold(img,160,255,cv2.THRESH_BINARY)
                res = reader.readtext(img)
                all_res = ''
                for r in res:
                    all_res += r[1]
                res = all_res

                res:str = res.replace(',','.')
                n_res = ''

                for s in res:
                    if s.isdigit():
                        n_res += s
                    if s == '.' and n_res.count('.') == 0:
                        n_res += s
                    if s == '/' or s == '?':
                        n_res += 7
                    if s == 'O' or s == 'o' or s == 'Q':
                        n_res += 0
                    if s == '|' or s == 'I' or s == 'i' or s == '!':
                        n_res += 1

                new_name = path_img[:-4] + '_' + n_res + '.png'
                try:
                    os.rename(path_img,new_name)
                except:
                    pass
            except:
                pass
    # cv2.imshow('img',img)

    # cv2.waitKey(0)