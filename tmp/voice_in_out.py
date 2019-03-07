import discord
import datetime

TOKEN = "XXXXXXX" # botのトークンキー
TEXT_CHANNEL = 000000000 # テキストチャットのチャンネルID
client = discord.Client()
text_chat = discord.Object(id=TEXT_CHANNEL)

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
    if before.voice.voice_channel == None:
        now = datetime.datetime.now()
        n_time = datetime.datetime(now.year, now.month,
            now.day, now.hour, now.minute)
        message = before.name + "が入ってきました" + ' ('+ str(n_time) + ')'
        print(message)
        await client.send_message(text_chat, message)
    elif after.voice.voice_channel == None:
        now = datetime.datetime.now()
        n_time = datetime.datetime(now.year, now.month,
            now.day, now.hour, now.minute)
        message = after.name + "が出ていきました" + ' ('+ str(n_time) + ')'
        print(message)
        await client.send_message(text_chat, message)

client.run(TOKEN)
