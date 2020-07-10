import discord
import datetime
import random
import numpy as np
import requests
import json
import asyncio

import get_news

TOKEN = "XXXXXXXXXX" # トークンキー
TEXT_CHANNEL = 00000000000 # テキストチャットのチャンネルID
client = discord.Client()

text_chat = discord.Object(id=TEXT_CHANNEL)
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
voice = None
sleeper = None


@client.event
async def on_ready():
    global flag1 ,flag2, flag3, flag4, voice, player
    print('bot is ready.')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    #voiceチャンネルが4つある環境
    voice_id1 = 000000000000000000
    voice_id2 = 000000000000000000
    voice_id3 = 000000000000000000
    voice_id4 = 000000000000000000
    v_ch1 = client.get_channel(voice_id1)
    v_ch2 = client.get_channel(voice_id2)
    v_ch3 = client.get_channel(voice_id3)
    v_ch4 = client.get_channel(voice_id4)
    #人の有無をフラグによって管理する
    if len(v_ch1.members)==0:
        flag1 = 0
    else:
        flag1 = 1
    if len(v_ch2.members)==0:
        flag2 = 0
    else:
        flag2 = 1
    if len(v_ch3.members)==0:
        flag3 = 0
    else:
        flag3 = 1
    if len(v_ch4.members)==0:
        flag4 = 0
    else:
        flag4 = 1

@client.event
async def on_voice_state_update(member, before, after):
    #入退室通知
    global flag1 ,flag2, flag3, flag4, voice
    voice_id1 = 000000000000000000
    voice_id2 = 000000000000000000
    voice_id3 = 000000000000000000
    voice_id4 = 000000000000000000
    #入退室の通知を飛ばしてもらうテキストチャンネル
    text_id = 000000000000000000
    #それぞれのチャンネル情報を獲得
    v_ch1 = client.get_channel(voice_id1)
    v_ch2 = client.get_channel(voice_id2)
    v_ch3 = client.get_channel(voice_id3)
    v_ch4 = client.get_channel(voice_id4)
    t_ch = client.get_channel(text_id)
    #目視用
    print(flag1, flag2, flag3, flag4)
    #一番初めに入ってきた人，一番遅く出て行った人を通知（2種類*4部屋=8処理）
    if (len(v_ch1.members) == 0 and flag1==1 and flag2 ==0 and flag3==0 and flag4==0):
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
        n_time = datetime.datetime(now.year, now.month,
            now.day, now.hour, now.minute, now.second)
        message = str(v_ch1) + "で" + member.display_name + "が通話を終了" + ' ('+ str(n_time) + ')'
        #チャンネル名と時間を指定のテキストチャネルに送る
        print(message)
        await t_ch.send(message)
        flag1 = 0
    elif (len(v_ch1.members) == 1 and flag1==0 and flag2 ==0 and flag3==0 and flag4==0):
            now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
            n_time = datetime.datetime(now.year, now.month,
                now.day, now.hour, now.minute, now.second)
            message = str(v_ch1) + "で" + member.display_name + "が通話を開始" + ' ('+ str(n_time) + ')'
            print(message)
            await t_ch.send(message)
            flag1=1
    elif (len(v_ch2.members) == 0 and flag1==0 and flag2 ==1 and flag3==0 and flag4==0):
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
        n_time = datetime.datetime(now.year, now.month,
            now.day, now.hour, now.minute, now.second)
        message = str(v_ch2) + "で" + member.display_name + "が通話を終了" + ' ('+ str(n_time) + ')'
        print(message)
        await t_ch.send(message)
        flag2 = 0
    elif (len(v_ch2.members) == 1 and flag1==0 and flag2==0 and flag3==0 and flag4==0):
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
        n_time = datetime.datetime(now.year, now.month,
            now.day, now.hour, now.minute, now.second)
        message = str(v_ch2) + "で" + member.display_name + "が通話を開始" + ' ('+ str(n_time) + ')'
        print(message)
        await t_ch.send(message)
        flag2=1
    elif (len(v_ch3.members) == 0 and flag1==0 and flag2 ==0 and flag3==1 and flag4==0):
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
        n_time = datetime.datetime(now.year, now.month,
            now.day, now.hour, now.minute, now.second)
        message = str(v_ch3) + "で" + member.display_name + "が通話を終了" + ' ('+ str(n_time) + ')'
        print(message)
        await t_ch.send(message)
        flag3 = 0
    elif (len(v_ch3.members) == 1 and flag1==0 and flag2==0 and flag3==0 and flag4==0):
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
        n_time = datetime.datetime(now.year, now.month,
            now.day, now.hour, now.minute, now.second)
        message = str(v_ch3) + "で" + member.display_name + "が通話を開始" + ' ('+ str(n_time) + ')'
        print(message)
        await t_ch.send(message)
        flag3=1
    elif (len(v_ch4.members) == 0 and flag1==0 and flag2 ==0 and flag3==0 and flag4==1):
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
        n_time = datetime.datetime(now.year, now.month,
            now.day, now.hour, now.minute, now.second)
        message = str(v_ch4) + "で" + member.display_name + "が通話を終了" + ' ('+ str(n_time) + ')'
        print(message)
        await t_ch.send(message)
        flag4 = 0
    elif (len(v_ch4.members) == 1 and flag1==0 and flag2==0 and flag3==0 and flag4==0):
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
        n_time = datetime.datetime(now.year, now.month,
            now.day, now.hour, now.minute, now.second)
        message = str(v_ch4) + "で" + member.display_name + "が通話を開始" + ' ('+ str(n_time) + ')'
        print(message)
        await t_ch.send(message)
        flag4=1
    #それぞれの部屋の人の有無を2値で管理
    if len(v_ch1.members)==0:
        flag1 = 0
    else:
        flag1 = 1
    if len(v_ch2.members)==0:
        flag2 = 0
    else:
        flag2 = 1
    if len(v_ch3.members)==0:
        flag3 = 0
    else:
        flag3 = 1
    if len(v_ch4.members)==0:
        flag4 = 0
    else:
        flag4 = 1
    print(flag1, flag2, flag3, flag4)


async def Timeout(t):
    #音楽再生後，自動で消えるようにした
    #音楽再生時に新しい曲の長さに合わせてbotをボイスチャンネルから追い出す
    global voice
    #tは音楽の再生時間
    await asyncio.sleep(t)
    #再生時間分待ってもらってからdisconnect
    await voice.disconnect()
    #voiceをNoneに変更しておく
    voice = None

#自動返信
@client.event
async def on_message(message):
    #自分からのメッセージには返信しないように
    if message.author == client.user:
        return
    #Timeout関数を使う時に必要
    loop = asyncio.get_event_loop()
    global voice, sleeper
    if (message.content.startswith('特別になりたい') or message.content.startswith('stop')):
        #左側のメッセージの場合，対応する音楽を再生．右はstop
        #メッセージの送り主がいるボイスチャネルを特定
        channel = message.author.voice.channel
        #voiceがない場合は上で特定したチャネルにbotを接続
        if voice == None:
            voice = await channel.connect()
        # 接続しているかを確認
        elif(voice.is_connected() == True):
            # 接続先で音声を流しているか確認
            if(voice.is_playing()):
                # 流していれば停止させる
                voice.stop()
                if message.content.startswith('stop'):
                    #sleeperが起動している時は，処理を中止させる
                    if sleeper != None:
                        sleeper.cancel()
                    await voice.disconnect()
                    voice = None
                    return
            #botを移動させる
            await voice.move_to(message.author.voice.channel)
        if message.content.startswith('特別になりたい'):
            #キーメッセージをもらった場合，対応するセリフと音楽を流す
            await message.channel.send('私，特別になりたいの')
            voice.play(discord.FFmpegPCMAudio('./music/dummy1.mp3'), after=lambda e: print('end'))
            #音量を調節する
            voice.source = discord.PCMVolumeTransformer(voice.source)
            #20%の音量に
            voice.source.volume = 0.2
            #音楽を上から再生する時は，sleeperの処理を中止させる
            if sleeper != None:
                sleeper.cancel()
            #音楽にあった長さ分の処理をsleepさせる
            sleeper = loop.create_task(Timeout(t=149))
    #上のプログラムと同じ
    if (message.content.startswith('どうして') or message.content.startswith('stop')):
        channel = message.author.voice.channel
        if voice == None:
            voice = await channel.connect()
        elif(voice.is_connected() == True):
            if(voice.is_playing()):
                voice.stop()
                if message.content.startswith('stop'):
                    if sleeper != None:
                        sleeper.cancel()
                    await voice.disconnect()
                    voice = None
                    return
            await voice.move_to(message.author.voice.channel)
        if 'どうして' in message.content:
            await message.channel.send('と"う"し"て"ーえ"ーえ"ー')
            voice.play(discord.FFmpegPCMAudio('./music/dummy2.mp3'), after=lambda e: print('end'))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.05
            if sleeper != None:
                sleeper.cancel()
            sleeper = loop.create_task(Timeout(t=20))
    #上のプログラムと同じ
    if (message.content.startswith('能天気') or message.content.startswith('stop')):
        channel = message.author.voice.channel
        if voice == None:
            voice = await channel.connect()
        elif(voice.is_connected() == True):
            if(voice.is_playing()):
                voice.stop()
                if message.content.startswith('stop'):
                    if sleeper != None:
                        sleeper.cancel()
                    await voice.disconnect()
                    voice = None
                    return
            await voice.move_to(message.author.voice.channel)
        if '能天気' in message.content:
            await message.channel.send('行こう')
            voice.play(discord.FFmpegPCMAudio('./music/dummy3.mp3'), after=lambda e: print('end'))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 0.05
            if sleeper != None:
                sleeper.cancel()
            sleeper = loop.create_task(Timeout(t=48.5))
    #メッセージに対して画像を返す1
    if message.content.startswith('こんにちは'):
        file_path = './img/dummy1.jpg'
        await message.channel.send('こんにち殺法！', file=discord.File(file_path))
        hello_rand = random.randint(0,9)
        if hello_rand == 0:
            file_path = './img/dummy2.jpg'
            await message.channel.send('†こんにち殺法返し†', file=discord.File(file_path))
            file_path = './img/dummy3.jpg'
            await message.channel.send('', file=discord.File(file_path))
    #メッセージに対して画像を返す2
    if ('ねねっち' in message.content):
        #0~18の19枚用意してある中からランダムに返す
        p = random.randint(0,18)
        file_path = './img/image{}.jpg'.format(p)
        await message.channel.send('', file=discord.File(file_path))
    #メッセージに対して画像を返す3
    if message.content.startswith('こんにち殺法'):
        million_rand = random.randint(0,9)
        if million_rand == 0:
            file_path ='./img/dummy4.JPG'
            await message.channel.send('', file=discord.File(file_path))
        else:
            file_path = './img/dummy2.jpg'
            await message.channel.send('†こんにち殺法返し†', file=discord.File(file_path))
    #メッセージに対してURLを返す1
    if (('ぷにき' in message.content) or ('プニキ' in message.content)):
        await message.channel.send('https://kids.yahoo.co.jp/games/sports/013.html')
    #メッセージに対してURLを返す2
    if message.content.startswith('tenhou'):
        await message.channel.send('http://tenhou.net/0/?LXXXXX')
    #メッセージに対してURLを返す3
    if message.content.startswith('アレが読みたい'):
        await message.channel.send('https://syosetu.com')
    #機能一覧
    if message.content.startswith('-h'):
        await message.channel.send(
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
            '11. 「nnews」と送ると'
            'NHKニュースのトップ記事を5つのタイトルと短縮URLを返す．\n'
            '12. 「特別になりたい」と送ると特別になれます.stopで停止．\n'
            '13. 「どうして」と送るとサカナクションになれます.stopで停止．\n'
            '14. 「能天気」と送ると能天気になれます.stopで停止．\n'

            )
    #リストからくじ引きする処理
    if message.content.startswith('今日のゲーム'):
        game_list = np.array(["BFV","モンハン","tenhou","プニキ","ポケモンバトル","HoI4","人生","スプラ","マリオカート"])
        game_rand = random.randint(0,4)
        await message.channel.send(game_list[game_rand])
    #ynews と入力したらヤフーのトップニュースを返してくれる
    if message.content.startswith('ynews'):
        #テキストチャンネルを指定する
        news_id = 0000000000000000
        news_ch = client.get_channel(news_id)
        await news_ch.send("今日のYahooニュースです．")
        # Yahooトップのトピック記事タイトルを取得
        news_data = get_news.get_yahoo_news()
        # 取得データの表示
        #news_data = news_data[:-2]
        top_news = ""
        for news in (news_data):
            top_news += '・'+news[0]+'\n'+news[1]+'\n'+news[2]+'\n'+ '-----' +'\n'
        await news_ch.send(top_news)
    #nnews と入力したらNHKのトップニュースを返してくれる
    if message.content.startswith('nnews'):
        #テキストチャンネルを指定する
        news_id = 00000000000000000
        news_ch = client.get_channel(news_id)
        await news_ch.send("今日のNHKニュースです．")
        # NHKトップのトピック記事を取得
        text_data, news_data = get_news.get_nhk_news()
        # テキストデータのみの時
        text_ = ""
        for news in text_data:
            for target in news:
                text_ += target+'\n'
        await news_ch.send(text_)
client.run(TOKEN)
