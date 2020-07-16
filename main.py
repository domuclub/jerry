import discord
from discord import FFmpegPCMAudio
from discord.utils import get
from discord.ext import commands
import asyncio
client = commands.Bot(command_prefix = '::')

@client.event
async def on_ready():
	print("jery get ipad")
	await client.change_presence(status=discord.Status.online, activity= discord.Game("Shut The FUck Up"))

@client.command()
async def what_if_seinfeld_still_on_tv(ctx):
  await ctx.send('Jery get ipad')

@client.command(brief='bazinga', description='bazinga')
async def bazinga(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('bazinga.mp3')
    player = voice.play(source)


@client.command(brief='plays clap sound effect', description='plays clap sound effect while user is in bot')
async def clap(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('clap.mp3')
    player = voice.play(source)

@client.command(brief='plays "aww" sound effect', description='plays "aww" sound effect while user is in bot')
async def aww(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('aww.mp3')
    player = voice.play(source)

@client.command(brief='plays laughing sound effect', description='plays laughing sound effect while user is in bot')
async def laugh(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('laugh.mp3')
    player = voice.play(source)

@client.command(brief='plays "ooo" sound effect', description='plays "ooo" sound effect while user is in bot')
async def ooo(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('ooo.mp3')
    player = voice.play(source)

@client.command(brief='plays "uh oh" sound effect', description='plays "uh oh" sound effect while user is in bot')
async def uhoh(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('uhoh.mp3')
    player = voice.play(source)
client.run('NzE1MDQ4OTQ1MjM5MTk1NzQ4.Xs3nyw.MkjZ9MNgNJ8iVZrRggQs1SAeMkU')
