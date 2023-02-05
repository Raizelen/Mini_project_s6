import openai
import discord
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("openai_api_key")


async def handle_ask(message):
    text = message.content
    prompt = text

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    response = completions.choices[0].text
    await message.channel.send(response.strip())

async def handle_img(message):
    response = openai.Image.create(
        prompt=message.content[3:],
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    embed = discord.Embed(title="Generated Image")
    embed.set_image(url=image_url)
    #embed.timestamp = datetime.utcnow()
    await message.channel.send(embed=embed)