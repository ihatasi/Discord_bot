import discord
import datetime
import random
import numpy as np

import get_news

TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # トークンキー
TEXT_CHANNEL = 000000000000000000000000 # テキストチャットのチャンネルID
client = discord.Client()
text_chat = discord.Object(id=TEXT_CHANNEL)

@client.event
async def on_ready():
    print('bot is ready.')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

@client.event
async def on_voice_state_update(before, after):
    voice_id = "0000000000000000"#which voice channel?
    text_id = "000000000000000000"#which text channel?
    v_ch = client.get_channel(voice_id)
    t_ch = client.get_channel(text_id)
    if len(v_ch.voice_members) == 0:
        now = datetime.datetime.now()
        n_time = datetime.datetime(now.year, now.month,
            now.day, now.hour, now.minute, now.second)
        message = after.name + "が通話を終了" + ' ('+ str(n_time) + ')'
        print(message)
        await client.send_message(t_ch, message)
    else:
        now = datetime.datetime.now()
        n_time = datetime.datetime(now.year, now.month,
            now.day, now.hour, now.minute, now.second)
        message = before.name + "が通話を開始" + ' ('+ str(n_time) + ')'
        print(message)
        await client.send_message(t_ch, message)
#自動返信
@client.event
async def on_message(message):
    if message.content.startswith('こんにちは'):
        if client.user != message.author:
            file_path = './img/こんにち殺法.jpg'
            await client.send_file(message.channel, file_path)
            await client.send_message(message.channel,
                'こんにち殺法！')

    if message.content.startswith('こんにち殺法'):
        if client.user != message.author:
            million_rand = random.randint(0,9)
            if million_rand == 0:
                file_path ='./img/百万人目.JPG'
                await client.send_file(message.channel, file_path)
            else:
                file_path = './img/こんにち殺法返し.jpg'
                await client.send_file(message.channel, file_path)
                await client.send_message(message.channel,
                    '†こんにち殺法返し†')
        else:
            hello_rand = random.randint(0,9)
            if hello_rand == 0:
                file_path = './img/こんにち殺法返し.jpg'
                await client.send_file(message.channel, file_path)
                await client.send_message(message.channel,
                    '†こんにち殺法返し†')
                file_path = './img/こんにちコンボ.jpg'
                await client.send_file(message.channel, file_path)
    if (('ぷにき' in message.content) or ('プニキ' in message.content)):
        await client.send_message(message.channel,
            'https://kids.yahoo.co.jp/games/sports/013.html')
    if message.content.startswith('tenhou'):
        await client.send_message(message.channel,
            'テンホウのURL')
    if message.content.startswith('-h'):
        await client.send_message(message.channel,
            '鬨の声です．\n'
            '1. DiscordにBotがログインする（最低限の機能）．\n'
            '2. ボイスチャネルの人数が0から1になったとき，'
            '「〇〇（初めに入室した人）が通話を開始しました」と'
            '指定のテキストチャネルに送る．また，最後の一人が抜けたとき，'
            '「〇〇（最後に出た人）が通話を終了しました」と'
            '指定のテキストチャネルに送る．\n'
            '3. 「こんにちは」と送ると'
            '「こんにち殺法！」とその画像を返してくる．\n'
            '4. 「こんにち殺法」から始まる文を送ると'
            '「†こんにち殺法返し†」とその画像返す．\n'
            '5. 10%の確率で自分のこんにち殺法にこんにち殺法返しをして'
            'コンボが決まった画像を送る．\n'
            '6. 「プニキ」と送ると'
            'プーさんのホームランダービーのURLを返す．\n'
            '7. 「tenhou」と送ると'
            '自分たちがいつも使うテンホウの部屋URLを返す．\n'
            '8. 「アレが読みたい」と送るとなろうのURLを返す．\n'
            '9. 「今日のゲーム」と送ると'
            'すでに登録されているリストからゲームを一つ選ぶ．\n'
            '10. 「ynews」と送ると'
            'Yahoo!ニュースのトップ記事を5つのタイトルと短縮URLを返す．\n'
            '11. 「nnews」と送ると'
            'NHKニュースのトップ記事を5つのタイトルと短縮URLを返す．\n'
            '12. Twitterの@UN_NERV(https://twitter.com/UN_NERV)のツイートを取得\n'
            '12-1. 「NHK」が入ったツイートを自動取得\n'
            '12-2. 「緊急地震速報　最終報」または「地震情報」を自動取得\n'
            '12-3. 「全国の天気」を自動取得\n'
            )

    if message.content.startswith('アレが読みたい'):
        await client.send_message(message.channel,
            'https://syosetu.com')
    if message.content.startswith('今日のゲーム'):
        game_list = np.array(["BFV","モンハン","tenhou","プニキ","APEX"])
        game_rand = random.randint(0,4)
        await client.send_message(message.channel,
            game_list[game_rand])
    if message.content.startswith('ynews'):
        news_id = '000000000000000000' #newsテキストチャネルID
        news_ch = client.get_channel(news_id)
        await client.send_message(news_ch, "今日のYahooニュースです．")
        # Yahooトップのトピック記事タイトルを取得
        news_data = get_news.get_yahoo_news()
        # 取得データの表示
        news_data = news_data[:-2]
        top_news = ""
        for news in (news_data):
            top_news += news[0]+news[1]+'\n'
        await client.send_message(news_ch, top_news)
    if message.content.startswith('nnews'):
        news_id = '00000000000000000000' #newsテキストチャネルID
        news_ch = client.get_channel(news_id)
        await client.send_message(news_ch, "今日のNHKニュースです．")
        # NHKトップのトピック記事を取得
        text_data, news_data = get_news.get_nhk_news()
        # テキストデータのみの時
        text_ = ""
        for news in text_data:
            for target in news:
                text_ += target+'\n'
        await client.send_message(news_ch, text_)

client.run(TOKEN)
