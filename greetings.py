import gif

lmt = 8
# hello

async def handle_hello(message):
    if len(message.mentions)>0:
        user = message.mentions[0]
        await message.channel.send(f"hello, {user.mention}!")
        #send gif
        await gif.handle_gifs('hello',message,lmt)
    else:
        await message.channel.send("Please mention a user")



# good morning 

async def handle_gm(message):
    if len(message.mentions)>0:
        user = message.mentions[0]
        await message.channel.send(f"good morning, {user.mention}!")
        #send gif
        await gif.handle_gifs('good morning',message,lmt)
    else:
        await message.channel.send("Please mention a user")



# good night

async def handle_gn(message):
    if len(message.mentions)>0:
        user = message.mentions[0]
        await message.channel.send(f"good night, {user.mention}!")
        #send gif
        await gif.handle_gifs('good night',message,lmt)
    else:
        await message.channel.send("Please mention a user")
