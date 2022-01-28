import os
import discord
import wordleparser
import datetime

from dotenv import load_dotenv
from discord.ext import commands
from email.errors import MessageError
from unicodedata import name


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CID = 936621404651155550

client = commands.Bot(command_prefix='!')
scoreboard = {}

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    start_date = datetime.datetime.now() - datetime.timedelta(days=27)
    channel = client.get_channel(CID)
    messages = await channel.history(limit=500, after=start_date).flatten()
    for message in messages:
        if message.content.startswith("Wordle"):
            parser.parse(message.author.name, message.content)

@client.event
async def on_message(message):
    if message.content.startswith("Wordle"):
        parser.parse(message.author.name, message.content)
    await client.process_commands(message)

@client.command()
async def score(ctx):
    await ctx.send("```\n{}```".format(parser.get_scoreboard()))

parser = wordleparser.WordleParser()
client.run(TOKEN)