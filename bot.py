#bot.py
#imports
import os
import discord
import re
import time
from discord import channel
from discord.ext import commands
from dotenv import load_dotenv
from worker import worker
from worker import QRcreator

#load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('PREFIX')

#instantiate client object
client = commands.Bot(command_prefix=PREFIX)

#logger function
def log(ctx):

    author = ctx.author

    aID = "Author ID: " + str(author.id)
    aName = ">> Author Name: " + str(author.name)
    aDisc = "> Discriminator: " + str(author.discriminator)
    isBot = "> Author Is Bot?: " + str(author.bot)
    aNick = ">> Nickname: " + str(author.nick)

    guild = author.guild

    gID = "Server ID: " + str(guild.id)
    gName = ">> Server Name: " + str(guild.name)
    #gSID = "Server shart: " + str(guild.shard_id)
    #chunked = "Server is chunked?: " + str(guild.chunked)
    gMemCount = "Member count of the server: " + str(guild.member_count)

    aFinal = "\n".join([aID, aName, aDisc, isBot, aNick, gID, gName, gMemCount])    

    content = ">>> Message content: " + str(ctx.content)

    channel = ctx.channel

    cID = "Channel ID: " + str(channel.id)
    cName = ">> Channel Name: " + str(channel.name)
    cPos = "Channel's Position: " + str(channel.position)
    cNSFW = "> Channel Is Nsfw?: " + str(channel.nsfw)
    cNews = "> Channel Type: " + str(channel.type)
    catID = "Category ID: " + str(channel.category_id)

    cFinal = "\n".join([cID, cName, cPos, cNSFW, cNews, catID])

    row = "".join(["\n", aFinal, "\n", content, "\n", cFinal, "\n"])

    return row

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

@client.command()
async def queryfind(ctx, arg: str, sort: str = 'popular', page: int = 1):
    resp = worker.printSearchDoujin(arg, sort, page)
    for thing in resp:
        await ctx.send(thing + "\n\n")
        time.sleep(0.5)

@client.command()
async def QR(ctx, arg: str, masknum: int = 0):
    try:
        resp = QRcreator.createQR(arg, masknum)
        squashed = []
        for i in range(4):
            squashed.append("00000000000000000000000000000")
        for row in resp:
            c = []
            c.append("0000")
            for bit in row:
                c.append(str(bit))
            c.append("0000")
            squashed.append("".join(c))
        
        for i in range(4):
            squashed.append("00000000000000000000000000000")
        
        final = "\n".join(squashed)
        t = final.translate(final.maketrans("01","⬜⬛"))

        for i in range(5):
            await ctx.send(t[i*150:(i+1)*150])

        await ctx.send(t[750:])
    except QRcreator.LengthError:
        await ctx.send("ERROR: Argument longer than 7 characters (56 bits)")

#Raw anime handler
@client.event
async def on_message(ctx):
    pattern = r"raw anime"
    found = re.search(pattern, ctx.content, re.IGNORECASE & re.MULTILINE)
    checker = re.search("^\?>", ctx.content, re.IGNORECASE & re.MULTILINE)
    if checker:
        print(log(ctx))
    if found and ctx.author.bot == False:
        await ctx.reply("Have you heard of nyaa.si? It provides raw animes, iirc")
    else:
        await client.process_commands(ctx)

#If there is an error, it will answer with an error
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'Error. Try .help ({error})')

client.run(TOKEN)
