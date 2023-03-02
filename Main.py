import discord                  #discord functions
import os                       #to use env
from dotenv import load_dotenv #to enviroment variables e.g. API
# modules
import help
import greetings
import gif
import openAi
import weather
import yt

load_dotenv()
# environment variables
discord_api = os.getenv("discord_bot_api")


intents = discord.Intents().all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Bot is ready.")

# COMMANDS

@client.event
async def on_message(message):
    if message.content.startswith("!ping"):
        await handle_ping(message) 
# greetings
    elif message.content.startswith("!help"):
        await help.handle_Help(message)
    elif message.content.startswith("!hello"):
        await greetings.handle_hello(message)
    elif message.content.startswith("!gm"):
        await greetings.handle_gm(message)
    elif message.content.startswith("!gn"):
        await greetings.handle_gn(message)
# Open AI

    elif message.content.startswith("!ask"):
        await openAi.handle_ask(message)
    elif message.content.startswith("!img"):
        await openAi.handle_img(message)

# gifs
    elif message.content.startswith("!gif"):
        await gif.handle_gif(message)
#weather
    elif message.content.startswith("!weather"):
        await weather.handle_Weather(message)
#yt
    elif message.content.startswith("!ytd"):
        await yt.handle_ytd(message)

#***** system func

async def handle_ping(message):
    pong=round((client.latency * 1000),2) 
    await message.channel.send(f'My ping is {pong}ms!')



# ******************** end of code

client.run(discord_api)