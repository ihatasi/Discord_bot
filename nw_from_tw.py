#using Twitter API
import tweepy
import time
import asyncio
import discord
from datetime import datetime, timedelta, timezone

#discordBotのトークン
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#twitter
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token = "00000000000XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#ツイート取得
tweet_data = []
t_id = [0]
def Send2Disco(converted, ch):
    #loopの初期化（これがないと2回目以降でloopが閉じているのでエラーが出る）
    loop = asyncio.new_event_loop()
    #初期化したloopを使う
    client = discord.Client(loop=loop)
    #それぞれのチャネルIDの登録
    news_id = '00000000000000000000'
    eq_id = '00000000000000000000000'
    we_id = '0000000000000000000'
    ch_id = [news_id, eq_id, we_id]
    #今回使うチャネルIDの選択
    target_ch = ch_id[ch]
    @client.event
    async def on_ready(target_ch=target_ch):
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('-----')
        ch = client.get_channel(target_ch)
        await client.send_message(ch, converted)
        #終了
        await client.logout()

    client.run(TOKEN)
    #client.logout()で終了してこっちにくる
    print('client closed')
    return

while True:
    for tweet in tweepy.Cursor(api.user_timeline, tweet_mode='extended',
        screen_name = "UN_NERV").items(3):#最新のツイートを3件取得
        if('NHK' in tweet.full_text):#特定の文字列を含むと次へ
            ch_id = 0
            if(tweet.id in t_id):#今までに同じツイートidがないか見る
                break#あったら無視
            t_id.append(tweet.id)#ツイートidを登録
            tweet.created_at += timedelta(hours=9)
            tweet_data = [tweet.id,
            tweet.created_at.strftime('%H:%M - %Y/%m/%d'),
            tweet.full_text]#tweet_dataに上書き
            converted = tweet_data[2]+"\n"+tweet_data[1]+"\n"
            print(converted)
            Send2Disco(converted, ch_id)
            print('returned from news')
    for tweet in tweepy.Cursor(api.user_timeline, tweet_mode='extended',
        screen_name = "UN_NERV").items(5):#最新のツイートを5件取得
        if(('緊急地震速報 最終報' in tweet.full_text) or \
            ('地震情報' in tweet.full_text)):#特定の文字列を含むと次へ
            ch_id = 1
            if(tweet.id in t_id):#今までに同じツイートidがないか見る
                break#あったら無視
            t_id.append(tweet.id)#ツイートidを登録
            tweet.created_at += timedelta(hours=9)
            tweet_data = [tweet.id,
            tweet.created_at.strftime('%H:%M - %Y/%m/%d'),
            tweet.full_text]#tweet_dataに上書き
            converted = tweet_data[2]+"\n"+tweet_data[1]+"\n"
            print(converted)
            Send2Disco(converted, ch_id)
            print('returned from eq')
    for tweet in tweepy.Cursor(api.user_timeline, tweet_mode='extended',
        screen_name = "UN_NERV").items(5):#最新のツイートを5件取得
        if('全国の天気' in tweet.full_text):#特定の文字列を含むと次へ
            ch_id = 2
            if(tweet.id in t_id):#今までに同じツイートidがないか見る
                break#あったら無視
            t_id.append(tweet.id)#ツイートidを登録
            tweet.created_at += timedelta(hours=9)
            tweet_data = [tweet.id,
            tweet.created_at.strftime('%H:%M - %Y/%m/%d'),
            tweet.full_text]#tweet_dataに上書き
            converted = tweet_data[2]+"\n"+tweet_data[1]+"\n"
            print(converted)
            Send2Disco(converted, ch_id)
            print('returned from wth')
    time.sleep(30)
