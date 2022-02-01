import os
import discord
import datetime
import psycopg2
import settings

from dotenv import load_dotenv
from discord.ext import commands
from email.errors import MessageError
from unicodedata import name
from wordleparser import get_points, parse, get_scoreboard

bot = commands.Bot(command_prefix='!')

# Default Events
@bot.event
async def on_ready():
    #try:
        #connect to database
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.content.startswith("Wordle"):
        player = message.author.name
        day, score = parse(message.content)
        points = get_points(score)
        cid = message.TextChannel.Guild.id
        add_to_db(cid, player, score, points, day)
    await bot.process_commands(message)

# Custom Commands
@bot.command()
async def score(ctx):
    await ctx.send("```\n{}```".format(get_scoreboard()))

@bot.command()
async def add(ctx):
    pass

def add_to_db(cid, player, score, points, day):


################################################################################
if __name__ == "__main__":
    try:
        # Connect to DB
        connection = psycopg2.connect(user=settings.DATABASE_USER,
                                      password=settings.DATABASE_PSWD,
                                      host=settings.DATABASE_HOST,
                                      port=settings.DATABASE_PORT,
                                      database=settings.DATABASE_NAME)
        # Create a cursor to perform database operations
        cursor = connection.cursor()
    except Exception as error:
        print( "Error connecting to DB: ", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            bot.run(settings.DISCORD_TOKEN)