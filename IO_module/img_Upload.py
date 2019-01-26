# -*- coding: utf-8 -*-

import os
import sys
import tweepy
from IO_module.key_tweepy import key_tweepy_proc

def output(command): # + user
    #print(command_tweet)
    sys.stderr.write("\n***　Upload Start ***\n")
    api = key_tweepy_proc()

    f = open(r'/home/pi/Desktop/image_pro/IO_module/screen_name.txt', encoding='utf-8')
    send_name = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()
    #print(sendname)
    message = ""
    message += "@" + send_name + "\n" #'user'
    message += command + "\n"
    message += "Image processing is completed!!\n"

    #message += "2019年1月21日\n"
    #
    #
    #api.update_status(message)
    f = open(r'/home/pi/Desktop/image_pro/IO_module/locate.txt', encoding='utf-8')
    locate = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()
    locate = locate.rstrip('\r\n')
    api.update_with_media(filename=locate,status=message)
    #
    sys.stderr.write("*** Upload Finish ***\n\n")

    print('Upload SUCCESS || Command / {}'.format(command))
    #os.remove(r'C:\Users\KITAKAMI\Desktop\image_pro\image\output.jpg')
    #os.remove(r'C:\Users\KITAKAMI\Desktop\image_pro\image\input.jpg')

    #if(False == os.path.isfile(r'C:\Users\KITAKAMI\Desktop\image_pro\image\output.jpg')):
        #print('\nImage:Remove Success!')
    #else:
        #print('\nImage:Remove Failed')
