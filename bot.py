#bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from worker import worker

client = commands.Bot(command_prefix="???")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#On startup
@client.event
async def on_ready():
    try:
        print(client.user.name)
        print(client.user.id)
        print("Discord.py Version: {}".format(discord.__version__))
        print(f'{client.user} has connected to Discord!')
    except Exception as e:
        print(e)

#On new message
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

#actual command
@client.command()
async def funky(ctx, arg, cover=""):
    resp = worker.printdoujin(arg)
    await ctx.send(resp[0])
    if cover == "-c":
        await ctx.send(resp[1])

#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')

client.run(TOKEN)