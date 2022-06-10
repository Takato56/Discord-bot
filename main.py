import discord
from discord.ext import commands


client = discord.Client()
client = commands.Bot(command_prefix='h.')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def sus(ctx, arg):
    print(ctx.author)
    print(ctx.message)
    print(ctx.guild)

@client.command()
async def play(ctx, url : str, channel):
    voiceChannel = discord.utils.get(ctx.guild.voice_channel, name=channel)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await voiceChannel.connect()

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send('Bot is not currently in a voice channel')

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send('No audio is playing')

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('The audio is not paused')

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

client.run('Token goes here')


