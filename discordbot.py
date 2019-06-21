import discord
from discord.ext import tasks

TOKEN = "NTkxNjg3MzIyNTg0NzQzOTM2.XQ0chA.DFt5eQ2TUFuWloCnwhllfxaKzaA" #トークン
CHANNEL_ID = nortification#3907 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=5)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
