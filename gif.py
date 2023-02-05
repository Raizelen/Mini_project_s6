import discord
import random
import requests
import os
from dotenv import load_dotenv
lmt = 8

load_dotenv()
tenor_api_key= os.getenv("tenor_api_key")
ckey= os.getenv("ckey")

async def handle_gif(message):
    search_term = message.content[5:]
    await handle_gifs(search_term,message,lmt)

async def handle_gifs(search_term,message,lmt):
    
    response = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, tenor_api_key, ckey,  lmt))

    if response.status_code == 200:
        #embed = discord.Embed(color=0x9b111e)
        json_response = response.json()
        gifs = json_response['results']
        gif = random.choice(gifs)
        gif_url = gif['url']

        #embed.set_image(url=gif_url)
        print(gif_url)
        await message.channel.send(gif_url)
        #await message.channel.send(embed=embed)
        # embed = discord.Embed()
        # embed.set_image(url=gif_url)
        # print(gif_url)
        # await message.channel.send(embed=embed)

    else:
        print(f"An error occurred: {response.status_code}")
