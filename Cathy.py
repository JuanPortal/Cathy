from discord.ext import commands
import discord
from gtts import gTTS
import time

client = commands.Bot(command_prefix="$")
client.remove_command("help")


@client.event
async def on_ready():
    print("Chatty Cathy ready to talk!")


@client.command(pass_context=True)
async def unir(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    
    
@client.command(pass_context=True)
async def salir(ctx):
    await ctx.guild.voice_client.disconnect()


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
    
    
@client.command(pass_context=True)
async def say(ctx, *args):
    await ctx.channel.purge(limit=1)
    texto = "".join(args)
    myobj = gTTS(text=texto, lang="en", slow=False)
    myobj.save("voz.pcm")

    channel = ctx.message.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio('voz.pcm'))

    vc.source = discord.PCMVolumeTransformer(vc.source)
    vc.source.volume = 7.0

    time.sleep(3)
    await ctx.guild.voice_client.disconnect()
    
    
@client.command(pass_context=True)
async def help(ctx):
    em = discord.Embed(
        title="Help",
        description="***$di*** lee el mensaje en español\n\n***$say*** lee el mensaje en inglés\n\n***$unir*** une a \
        Cathy al canal de voz\n\n***$salir*** bota a Cathy del canal de voz"
    )
    await ctx.send(embed=em)
    

client.run("ODA1NDg1MTk5MDY0NDMyNjgz.YBbkjA.G2sM7qZafaldkkCkAI9kBzxvfIM")
