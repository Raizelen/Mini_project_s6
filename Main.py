import discord                  #discord functions
import os                       #to use env
from dotenv import load_dotenv #to enviroment variables e.g. API
# modules
import help
import greetings
import gif
import openAi
import weather

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

# greetings
    if message.content.startswith("!help"):
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




# ******************** end of code

client.run(discord_api)