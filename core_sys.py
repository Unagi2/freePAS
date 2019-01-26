# -*- coding: utf-8 -*-

import os
import threading
import cv2
import time
import os.path
from filter_module import anime_filter
from filter_module import dot_filter
from IO_module import img_Upload
from IO_module import img_Download

path = r'/home/pi/Desktop/image_pro/image/input.jpg'


if __name__ == '__main__':
    while True:
        #filiter
        filter_1 = 'dot'
        filter_2 = 'anime'

        #画像ダウンロード from Twitter
        img_Download.input()
        
        if os.path.isfile(path) == 1:
            f = open(r'/home/pi/Desktop/image_pro/IO_module/command.txt', encoding='utf-8')
            command = f.read()  # ファイル終端まで全て読んだデータを返す
            f.close()
            #画像処理選択
            if command.find(filter_1) == 0:
                print("dot")
                dot_filter.dot_art(alpha=0.4, K= 4)
                
                #画像アップロード to Twitter
                img_Upload.output(command)

            if command.find(filter_2) == 0:
                print("anime")
                anime_filter.anime_art()

                #画像アップロード to Twitter
                img_Upload.output(command)
        else:
            print("画像未取得")

        time.sleep(1)
