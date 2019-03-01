import discord
import datetime

TOKEN = "XXXXXXX" # botのトークンキー
TEXT_CHANNEL = 000000000 # テキストチャットのチャンネルID
client = discord.Client()
text_chat = discord.Object(id=TEXT_CHANNEL)
flag = 0

#botが準備できたとき
@client.event
async def on_ready():
    print('bot is ready.')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#voiceチャネルのstatusが変わったとき
@client.event
async def on_voice_state_update(before, after):
    global flag
    if before.voice.voice_channel == None:
        #message = before.name + "が入ってきました"
        if flag == 0:
            now = datetime.datetime.now()
            n_time = datetime.datetime(now.year, now.month,
                now.day, now.hour, now.minute)
            message = before.name + "が通話を開始" + ' ('+ str(n_time) + ')'
            print(message)
            await client.send_message(text_chat, message)
        flag += 1
    elif after.voice.voice_channel == None:
        flag -= 1
        #message = after.name + "が出ていきました"
        if flag == 0:
            now = datetime.datetime.now()
            n_time = datetime.datetime(now.year, now.month,
                now.day, now.hour, now.minute)
            message = after.name + "が通話を終了" + ' ('+ str(n_time) + ')'
            print(message)
            await client.send_message(text_chat, message)

client.run(TOKEN)
