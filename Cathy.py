from discord.ext import commands
import discord
from gtts import gTTS
import time
import random

client = commands.Bot(command_prefix="$")
client.remove_command("help")


@client.event
async def on_ready():
    print("Chatty Cathy ready to talk!")


@client.command(pass_context=True, aliases=["join"])
async def unir(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()


@client.command(pass_context=True, aliases=["leave", "fuckoff"])
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
        Cathy al canal de voz\n\n***$salir*** bota a Cathy del canal de voz\n\n***$audio*** reproduce el audio \
        seleccionado\n\n***$audios*** muestra la lista de audios"
    )
    await ctx.send(embed=em)


def arreglar(palabra):
    palabra = palabra.lower()
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")
    palabra = palabra.replace("ü", "u")
    palabra = palabra.replace(" ", "")
    palabra = palabra.replace(",", "")
    return palabra


@client.command(pass_context=True)
async def audio(ctx, *args):
    audio_tilin = ["tilin"]
    audio_cardi = ["cardi", "risa"]
    audio_cuack = ["cuack", "cuac", "cuak", "pato", "kuack", "kuac", "kuak"]
    audio_gaa = ["gaa"]
    audio_lapo = ["lapo", "push", "plus"]
    audio_ohno = ["ño", "oh"]
    audio_papi = ["papi", "cachame", "kchame", "kachame"]
    audio_oidos = ["chorri", "mano", "oido", "ven"]
    audio_sagasti = ["sagasti"]
    audio_auron = ["tengo", "miedo", "auron"]
    audio_nooo = ["pamela", "noo", "noni", "enojada"]
    audio_chupetin = ["chupet"]
    audio_aumrd = ["au", "mierda", "mrd"]
    audio_piero = ["shea", "bobo"]
    audio_ahoraque = ["ahora"]
    audio_equipo = ["equipo", "alfa", "buena", "maravilla", "onda", "dinamita", "escuadron", "lobo"]
    audio_cell = ["cell", "momento", "terror"]
    audio_raiden = ["destinos", "muerte", "peores", "raiden"]
    audio_woody = ["woody", "bien", "pensado", "budi", "budy", "wudy", "wudi", "gudi", "gudy", "wuudy"]
    audio_eleccion = ["eleccion"]
    audio_ricolas = ["ricolas", "rikolas", "joel"]
    audio_decepcion = ["decepcion", "traicon", "hermano", "amigo"]
    audio_diablos = ["diablo", "orita"]
    audio_nolose = ["dime", "lose"]
    audio_algoandamal = ["algo", "anda", "mal"]
    audio_manuelgold = ["quee", "kee", "qee"]
    audio_oferton = ["pt", "ofert"]
    audio_escuchame = ["escuchame", "huevon", "webon", "wbn", "huebon", "wevon", "wn"]
    audio_aquaman = ["enfermo", "bruce", "wayne", "batman", "aquaman", "estas"]
    audio_yamete = ["yamete", "kudasai"]
    audio_imbecil = ["imbe", "gracioso", "inve"]
    audio_chikistrikis = ["aqui", "aki", "istri"]
    audio_excita = ["porque", "excita", "tanto"]
    audio_segovia = ["mama", "puta", "govia", "madre", "chancro", "vieja"]
    audio_divertido = ["divertido", "hijo", "perra"]
    audio_fiesta = ["suponia", "esto", "fiesta"]
    audio_estrategia = ["llama", "sele", "estrategia"]
    audio_rick = ["rick", "falso"]
    audio_yalose = ["yalose", "maric"]
    audio_exhibiste = ["yanos", "exhibiste", "exibiste", "exiviste"]
    audio_quierellorar = ["quiere", "llorar", "vasa"]
    audio_cachera = ["calla", "cachera", "kchera", "kachera", "klla", "kalla"]
    audio_talla = ["aver", "haber", "esde", "talla"]
    audio_premiodoble = ["quebien", "qbien", "premio", "doble"]

    if any(word in arreglar(str(args)).lower() for word in audio_tilin):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Tilín.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_cardi):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Cardi.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_cuack):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Cuack.mp3"))
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_gaa):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Gaa.mp3"))
        time.sleep(4)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_lapo):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Lapo.mp3"))
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_ohno):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Oh ño.mp3"))
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_papi):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Papi, cáchame.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_oidos):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Oídos.mp3"))
        time.sleep(4)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_sagasti):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/SaGAAAAAAAsti.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_auron):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Miedo.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_chupetin):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Chupetín.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_nooo):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        num = random.randint(1, 3)
        vc.play(discord.FFmpegPCMAudio(f"audios/Noooo{num}.mp3"))
        # print(num)
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()

    elif any(word in arreglar(str(args)).lower() for word in audio_aumrd):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Au, mrd.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_piero):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Piero.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_ahoraque):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Ahora qué.mp3"))
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_equipo):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Equipo.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_cell):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Cell.mp3"))
        time.sleep(5)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_raiden):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Raiden.mp3"))
        time.sleep(4)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_woody):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Bien pensado, Woody.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_eleccion):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/No tengo elección.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_ricolas):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Ricolás.mp3"))
        time.sleep(7)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_decepcion):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Decepción.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_diablos):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Diablos, señorita.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_nolose):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/No lo sé, tú dime.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_algoandamal):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Algo anda mal.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_manuelgold):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Qué.mp3"))
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_oferton):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Puta, qué ofertón.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_escuchame):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Escúchame, huevón.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_aquaman):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Estás enfermo, Bruce Wayne.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_yamete):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Yamete kudasai.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_imbecil):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Imbécil, te crees muy gracioso.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_chikistrikis):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Aquí no, chikistrikis.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_excita):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Por qué me excita tanto.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_segovia):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Tu mamá es una puta.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_divertido):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Qué divertido es ese hijo de perra.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_fiesta):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Hey, no se suponía que esto era una fiesta.mp3"))
        time.sleep(4)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_estrategia):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/A eso se le llama estrategia.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_rick):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/No lo sé, Rick, parece falso.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_yalose):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Ya lo sé, maricón, ya lo sé.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_exhibiste):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Ya nos exhibiste.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_quierellorar):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Quiere llorar.mp3"))
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_cachera):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Calla, cachera.mp3"))
        time.sleep(5)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_talla):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/A ver si esto es de tu talla.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_premiodoble):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Muy bien, premios dobles.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()


@client.command(pass_context=True)
async def audios(ctx):
    em = discord.Embed(
        title="Audios",
        description="\nCardi\n\nCuack\n\nGaaa\n\nLapo\n\nTengo miedo\n\nOh ñooo\n\n \
        Pero qué ven mis oídos, mano\n\nPapi, cáchame\n\nSagasti\n\nA la mierda, Tilín\n\nChupetín\n\n \
        No shea bobo\n\nAu, mierda\n\n¿Ahora qué?\n\nEquipo Alfa Buena Maravilla Onda \
        Dinamita Escuadrón Lobo\n\nEn ese momento... Cell sintió el verdadero terror\n\n \
        Hay destinos peores que la muerte\n\nBien pensado, Woody\n\n No tengo elección\n\n \
        Ricolás\n\nLa decepción, la traición\n\nDiablos, señorita\n\nNo lo sé, tú dime\n\n \
        Algo anda mal\n\n¿Quééé?\n\nPuta, qué ofertón\n\nEscúchame, huevón\n\n \
        Estás enfermo, Bruce Wayne\n\nYamete Kudasai\n\nImbécil, ¿te crees muy gracioso?\n\n \
        Aquí no, chikistrikis\n\n¿Por qué me excita tanto?\n\nQué divertido es ese hijo de perra\n\n \
        Hey, ¿no se suponía que esto era una fiesta?\n\nA eso se le llama estrategia\n\n \
        Ya lo sé, maricón, ya lo sé\n\nNo lo sé, Rick, parece falso\n\nYa nos exhibiste\n\n \
        ¿Quiere llorar?\n\nCalla, cachera\n\nA ver si esto es de tu talla\n\nMuy bien, premios dobles"
    )
    await ctx.send(embed=em)


client.run("ODA1NDg1MTk5MDY0NDMyNjgz.YBbkjA.-EWlOYH_3e6QPdMcXB6tjXasKYI")
