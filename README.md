# freePAS
free PAS (Free Photo Application Service の略)

Raspberry pi 3 B+を用いて、Twitterのツイートに含まれる、特定のハッシュタグに反応して
添付されている画像を自動的に加工するアプリ

複雑になってきた、画像加工をdotやanimeといった、短いキーワードを打つだけで簡単に画像加工ができるようになる。

今回は、24h体制で運用することも視野に、Raspberry pi3 B+を使用した。

TwitterAPIのハッシュタグ検索を利用して、特定の（例：#photo_change)ハッシュタグのついた投稿を取得。
画像付きのツイートを取得後、添付画像をダウンロードし、Raspberry piにてOpenCVで画像加工を施す。
画像加工したものは、投稿者のTwitterIDに@リプライ返信される。

投稿者は、画像加工したものを各SNSに投稿することで、いつもとは違う写真の雰囲気を共有して楽しむことができます。

## Folder Structure(各ファイルの要素)

**freePAS Folder(home directory)**
 * core_sys.py （このプログラムを中枢として各ファイルを実行している)
 * URL_pool.txt (ツイート取得の際、重複を防止するlogファイル) 

 **IO_module folder**
   *	img_Download.py    
   *	img_Upload.py  
   *	key_tweepy.py
   *	login.py
   *	screen_name.txt
   *	command.txt
   *	locate.txt

 **filter_module folder**
   *	anime_filter.py
   *	dot_filter.py
  
 **image folder**
   *	input.jpg
   *	output.jpg
