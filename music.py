import discord
import yt_dlp as youtube_dl
import os
import asyncio
from py_youtube import Search

voice_clients = {}

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': '-vn'}

async def handle_play(message):

    try:
        #voice instance
        voice_client = await message.author.voice.channel.connect()          #connecting to a voice channel
        voice_clients[voice_client.guild.id] = voice_client                  #saving voice client inside dic voice clients with server id
    except Exception as err:
        print(err)    
    
    try:

        search_term = message.content.replace('!play ','')
        query = Search(search_term,limit = 1).videos()
        print(search_term)
        url = f'https://www.youtube.com/watch?v='+ query[0]['id']

        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download = False))

        song = data['url']
        player = discord.FFmpegPCMAudio(song, **ffmpeg_options,executable = 'E:\\Mini_project_s6\\ffmpeg\\ffmpeg.exe')

        voice_clients[message.guild.id].play(player)

    except Exception as err:
        print(err)

async def handle_pause(message):
    try:
        voice_clients[message.guild.id].pause()
    except Exception as err:
        print(err)

async def handle_resume(message):
    try:
        voice_clients[message.guild.id].resume()
    except Exception as err:
        print(err)

async def handle_stop(message):
    try:
        voice_clients[message.guild.id].stop()
        await voice_clients[message.guild.id].disconnect()
    except Exception as err:
        print(err)



#___________________________________________________help________________________________________________________________________________
async def handle_help(message): 
    embed = discord.Embed(title="Welcome to music Help", description="To start with join a voice channel and use !play <url of video>", color=0x9b111e)
    embed.add_field(name="!play <url of video>", value="TO play music of that url(audio) ", inline=False)
    embed.add_field(name="!pause", value="pauses the music", inline=False)
    embed.add_field(name="!resume", value="resumes playing the music", inline=False)
    embed.add_field(name="!stop", value="to disconnect the bot from the channel", inline=False)
    await message.channel.send(embed=embed) 

