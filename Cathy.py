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
    

def arreglar(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")
    palabra = palabra.replace(" ", "")
    palabra = palabra.replace(",", "")
    return palabra


@client.command(pass_context=True)
async def audio(ctx, *args):
    audio_tilin = ["tilin"]
    audio_cardi = ["cardi", "risa"]
    audio_cuack = ["cuack", "cuac", "pato", "kuac", "kuack"]
    audio_gaa = ["gaa", "gaaa", "gaaaa", "gaaaaa"]
    audio_lapo = ["lapo", "push", "plus"]
    audio_ohno = ["oño", "ohño", "ño", "oh"]
    audio_papi = ["papicachame", "papi", "cachame", "kchame"]
    audio_oidos = ["queven", "chorri", "mis oidos", "oidos", "qvenmisoidos"]
    audio_sagasti = ["sagasti"]
    audio_auron = ["tengo", "miedo", "auron"]
    
    channel = ctx.message.author.voice.channel
    vc = await channel.connect()

    if any(word in arreglar(str(args)).lower() for word in audio_tilin):
        await ctx.channel.purge(limit=1)
        vc.play(discord.FFmpegPCMAudio("audios/Tilín.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_cardi):
        await ctx.channel.purge(limit=1)
        vc.play(discord.FFmpegPCMAudio("audios/Cardi.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_cuack):
        await ctx.channel.purge(limit=1)
        vc.play(discord.FFmpegPCMAudio("audios/Cuack.mp3"))
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_gaa):
        await ctx.channel.purge(limit=1)
        vc.play(discord.FFmpegPCMAudio("audios/Gaa.mp3"))
        time.sleep(4)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_lapo):
        await ctx.channel.purge(limit=1)
        vc.play(discord.FFmpegPCMAudio("audios/Lapo.mp3"))
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_ohno):
        await ctx.channel.purge(limit=1)
        vc.play(discord.FFmpegPCMAudio("audios/Oh ño.mp3"))
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_papi):
        await ctx.channel.purge(limit=1)
        vc.play(discord.FFmpegPCMAudio("audios/Papi, cáchame.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_oidos):
        await ctx.channel.purge(limit=1)
        vc.play(discord.FFmpegPCMAudio("audios/Oídos.mp3"))
        time.sleep(4)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_sagasti):
        await ctx.channel.purge(limit=1)
        vc.play(discord.FFmpegPCMAudio("audios/SaGAAAAAAAsti.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_auron):
        await ctx.channel.purge(limit=1)
        vc.play(discord.FFmpegPCMAudio("audios/Miedo.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()


@client.command(pass_context=True)
async def audios(ctx):
    em = discord.Embed(
        title="Audios",
        description="\nCardi\n\nCuack\n\nGaaaa\n\nLapo\n\nTengo miedo\n\nOh ñooo\n\nPero qué ven mis oídos, mano\n\nPa\
        pi, cáchame\n\nSaGAAAAAAAAAAAAAsti\n\nA la mierda, Tilín"
    )
    await ctx.send(embed=em)


client.run("ODA1NDg1MTk5MDY0NDMyNjgz.YBbkjA.G2sM7qZafaldkkCkAI9kBzxvfIM")
