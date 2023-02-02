import discord
import greetings

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

client.run("MTA3MDY0OTIyMzE1MTg5MDQ4Mg.GDopQd.TsBQkrn-ooTYODzGOdA6fnbU5m3gZczJduuwA0")