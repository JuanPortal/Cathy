from discord.ext import commands
import discord
from gtts import gTTS
import time

client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print("Chatty Cathy ready to talk!")


@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel

    await channel.connect()


@client.command(pass_context=True)
async def di(ctx, *args):
    await ctx.channel.purge(limit=1)
    texto = "".join(args)
    myobj = gTTS(text=texto, lang="es", slow=False)
    myobj.save("voz.pcm")

    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('voz.pcm'))

    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 7.0

    time.sleep(3)
    await ctx.guild.voice_client.disconnect()


client.run("ODA1NDg1MTk5MDY0NDMyNjgz.YBbkjA.G2sM7qZafaldkkCkAI9kBzxvfIM")