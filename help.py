import discord

async def handle_Help(message): 
    embed = discord.Embed(title="Welcome to Help", description="bot commands", color=0x9b111e)
    embed.add_field(name="!help.", value="display the help menu ", inline=False)
    embed.add_field(name="!hello", value="says hello to the user mentioned", inline=False)
    embed.add_field(name="!gm", value="sends good morning to the user mentioned", inline=False)
    embed.add_field(name="!gn", value="sends good night to the user mentioned", inline=False)
    embed.add_field(name="!gif", value="search gif ", inline=False)
    embed.add_field(name="!ask", value="for assistance from venus", inline=False)
    embed.add_field(name="!img", value="to generate image using DALLA-E", inline=False)
    embed.add_field(name="!weather <city>", value="to show the weather of city", inline=False)
    await message.channel.send(embed=embed) 
