import discord
import os
from dotenv import load_dotenv
import requests
import re
import textwrap

load_dotenv()
weather_api_key = os.getenv("weather_api_key")

async def handle_Weather(message):
    # Location
    city = message.content[9:]
    # API endpoint
    endpoint = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}"
    # Make a GET request
    response = requests.get(endpoint)
    # Get the JSON data
    data = response.json()
    # Print the temperature
    temperature = data["main"]["temp"]

    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    icon_code = data["weather"][0]["icon"]
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    celsius = temperature - 273.15
    celsius = round(celsius, 2)
    embed = discord.Embed(title=f"Weather in {city}", color=0x00ff00)
    embed.set_thumbnail(url=icon_url)
    embed.add_field(name="Temperature", value=f"{celsius} celsius", inline=True)
    embed.add_field(name="Humidity", value=f"{humidity}%", inline=True)
    embed.add_field(name="Wind Speed", value=f"{wind_speed} m/s", inline=True)
    # embed.timestamp = datetime.utcnow()
    await message.channel.send(embed=embed)