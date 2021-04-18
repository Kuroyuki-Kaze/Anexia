#bot.py
#imports
import os
import discord
import re
from discord.ext import commands
from dotenv import load_dotenv
from worker import worker

#load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('PREFIX')

#instantiate client object
client = commands.Bot(command_prefix=PREFIX)

#On startup
@client.event
async def on_ready():
    try:
        print(client.user.name)
        print(client.user.id)
        print("Discord.py Version: {}".format(discord.__version__))
        print(f'{client.user} ready!')
    except Exception as e:
        print(e)

#Ping checking
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

#The actual command
@client.command()
async def sourcefind(ctx, arg, *args):
    cover, obf = "", ""
    for argv in args:
        if argv == "-c":
            cover = argv
        if argv == "-o":
            obf = argv
    resp = worker.printdoujin(arg, obf)
    await ctx.send(resp[0])
    if cover == "-c":
        await ctx.send(resp[1])

#Raw anime handler
@client.event
async def on_message(ctx):
    pattern = r"raw anime"
    found = re.search(pattern, ctx.content, re.IGNORECASE & re.MULTILINE)
    if found and ctx.author.bot == False:
        await ctx.reply("Have you heard of nyaa.si? It provides raw animes, iirc")
    else:
        await client.process_commands(ctx)

#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')

client.run(TOKEN)
