import discord                  #discord functions
import os                       #to use env
from dotenv import load_dotenv #to enviroment variables e.g. API
# modules
import greetings

load_dotenv()
# environment variables
discord_api = os.getenv("discord_bot_api")


intents = discord.Intents().all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_message(message):
    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")



# ******************** end of code

client.run(discord_api)