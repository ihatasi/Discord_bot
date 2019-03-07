# これは何？
Discordのbotプログラムです(Python3.6, discord0.16)．<br>
ブログ記事[https://ihatasi.hatenablog.com/entry/2019/03/07/161915]
本プログラムは自由にご使用していただいて構いません．
ただし，プログラムを実行したことによって生じた問題については自己責任でお願いします．
また，基本的にプログラムを直す予定もないので，間違いを発見したら自分で直してください．
<br>
このプログラムは主に2グループに分けられます．
1. dis_in_bot.py，news.py，get_shortenURL.py
2. nw_from_tw.py

グループ1はDiscordのアクションに対応をしてくれます．<br>
グループ2はTwitterでアクションに対応してくれます．<br>
私はいつもターミナルを2つ用意して，dis_in_bot.pyとnw_from_tw.pyを同時に動かしています．news.pyとget_shortenURL.pyはdis_in_bot.py内で呼ばれる機能です．<br>
dis_in_bot.py，get_shortenURL.py，nw_from_tw.pyにはdiscord，bitly，twitterのアクセスキーやトークン，チャネルIDが必要になります．<br>
imgフォルダ内の画像は本当の画像ではなく差し替えをしているので，自分で拾ってきてください．

# 動かし方
まず，DockerをInstallします．
Dockerを入れられない，使いたくない場合はDockerfileに書かれてる環境を整えて使ってください．<br>
次にDockerfileを用意しているので，`docker build -t discord_bot -f Dockerfile .`
でDockerfileをbuildしてください．<br>
次に`run.sh`内にシェルスクリプトを書いたのでターミナルで
`./run.sh discord_bot bash`
を実行してDockerコンテナ内でプログラムを実行してください．<br>
`python dis_in_bot.py`<br>
`python nw_from_tw.py`<br>
# 機能
dis_in_bot.pyを動かしてDiscordに「-h」と送ると機能リストが表示されます．<br>

