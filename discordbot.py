from discord.ext import commands
import os
import traceback
import discord
import random
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
arr = ['ぐー:punch:', 'ちょき:v:', 'ぱー:hand_splayed:']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def janken(ctx):
    await ctx.send("「"+random.choice(arr)+"」を出しました。")

# arr = ['ぐー:punch:', 'ちょき:v:', 'ぱー:hand_splayed:']
# # 接続に必要なオブジェクトを生成
# client = discord.Client()


# # メッセージ受信時に動作する処理
# @client.event
# async def on_message(message):
#     # メッセージ送信者がBotだった場合は無視する
#     if message.author.bot:
#         return

#     if message.content == 'じゃんけん':
#         await message.channel.send(message.author.mention+" は「"+random.choice(arr)+"」を出しました。")


bot.run(token)
