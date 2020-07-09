# これは何？
Python3.6，discord.py==1.3.3で動かしています<br>
Discordのbotプログラムです．<br>
本プログラムは自由にご使用していただいて構いません．
ただし，プログラムを実行したことによって生じた問題については自己責任でお願いします．<br>
このプログラムは主に2グループに分けられます．
dis_in_bot.py，get_news.py，shortenURL.pyはDiscordのアクションに対応をしてくれます．<br>

私はいつもAWS Cloud9上で，dis_in_bot.pyを動かしています．<br>
**dis_in_bot.py，shortenURL.pyにはdiscord，bitlyのアクセスキーやトークンが必要になります．**<br>
音楽再生もでき，再生時にbotがvoiceチャンネルに現れ，再生後にvoiceチャンネルから出ていく処理をしています．<br>
**img, musicフォルダ内の画像は本当の画像ではなく差し替えをしているので，自分で拾ってきてください．**

# 動かし方
AWS Cloud9上で動かすようにしています．
初めにrequirements.txtを使用して，必要なモジュールをインストールしてください．<br>
次に音声再生を使いたい場合は，下のffmpegから整えてください．

# ffmpeg
AWS Cloud9で音声再生させたい時は，以下のURL先のコマンドで環境ができる<br>
https://gist.github.com/willmasters/382fe6caba44a4345a3de95d98d3aae5

# opus
opusがいると思っていましたが，なくても行けました．ほしい人は`sudo yum install opus`でいけます．
