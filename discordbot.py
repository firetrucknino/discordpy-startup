#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "NTkxNjg3MzIyNTg0NzQzOTM2.XQ4TDg.Hl_Rui4m1TJ9bjvKCRc_GpSV7wk" #トークン
CHANNEL_ID = notification#3907 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '07:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
