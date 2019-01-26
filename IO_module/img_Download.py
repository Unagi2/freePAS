from IO_module import login #login.py　というtwitterログイン情報を記載したpyファイルを事前に作成しておく
#import login
#from key_tweepy import key_tweepy_proc
import datetime
import tweepy
from datetime import datetime as dt
import time
import requests
import shutil

def download_img(url, file_name):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

def input():
    while True:
        api=login.login("TwitterID入力")
        #api = key_tweepy_proc()
        for tweet in api.search(q='"#ハッシュタグ名 filter:images"',result_type='mixed', count=1):#qはキーワード excludeはリツイート避け exclude:retweets
            i = 1;
            class END(Exception):
                pass

            try:
                url=tweet.extended_entities['media'][0]['media_url']
                #tweet = tweet.full_text
                #print("\n"+url+"\n")
                print("=======================================")
                print(tweet.text+"\n")
                screen_name = tweet.user.screen_name
                command_tweet = tweet.text
                command_tweet = command_tweet.split('#free_PAS')[0]
                print(command_tweet)
                print(screen_name+"\n")
                #print("=======================================")


                f = open(r'/home/pi/Desktop/image_pro/IO_module/command.txt', 'w')# 書き込みモードで開く
                f.write(command_tweet) # 引数の文字列をファイルに書き込む
                f.close() # ファイルを閉じる


                f = open(r'/home/pi/Desktop/image_pro/IO_module/screen_name.txt', 'w')# 書き込みモードで開く
                f.write(screen_name) # 引数の文字列をファイルに書き込む
                f.close() # ファイルを閉じる



                flag = False
                Check = 1
                with open(r'/home/pi/Desktop/image_pro/URL_pool.txt', encoding='utf-8') as f:
                    for line in f:
                        line = line.rstrip('\r\n')
                        #print(line)
                        if url in line:
                            #print("重複検出")
                            Check = 0
                            break
                        else:
                            #print("重複不検出")
                            Check = 1

                    if Check == 1:
                        print("[重複不検出]")
                        print("画像保存")         # 1文字目が#ではない場合は読み込んだ1行をを出力する
                        print("=======================================")
                        #新規画像は保存処理
                        tdatetime = dt.now()
                        filename=r'/home/pi/Desktop/image_pro/image/input'+'.jpg'  #"img"という事前に作成したフォルダに保存
                        download_img(url,filename)

                        f = open(r'/home/pi/Desktop/image_pro/URL_pool.txt', 'a')# 書き込みモードで開く
                        f.write(url+"\n") # 引数の文字列をファイルに書き込む
                        f.close() # ファイルを閉じる

                        #print("BREAK!")
                        raise END

                    elif Check == 0:
                        print("[重複検出]\n")
                        print("=======================================")

            except END:
                i = 0;
                break
        if i == 0:
            i = 1
            break
        time.sleep(7)
