from __future__ import unicode_literals
import youtube_dl
import os

async def handle_ytd(message):
    link=message.content[5:]
    ydl_opts = {}
    os.chdir(os.getcwd()+'\\video')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print(link)
        ydl.download([link])


