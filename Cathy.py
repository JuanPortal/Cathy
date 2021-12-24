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
    
    # print(args)
    # print(texto)
    numero_palabras = len(args)
    tiempo = int(numero_palabras / 130 * 60) + 1
    # print(f"Original: {numero_palabras / 130 * 60}\nRedondeado: {tiempo}")
    time.sleep(tiempo)
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

    # print(args)
    # print(texto)
    numero_palabras = len(args)
    tiempo = int(numero_palabras / 130 * 60) + 1
    # print(f"Original: {numero_palabras / 130 * 60}\nRedondeado: {tiempo}")
    time.sleep(tiempo)
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


@client.command(pass_context=True, aliases=["a"])
async def audio(ctx, *args):
    audio_tilin = ["tilin"]
    audio_cardi = ["cardi", "risa"]
    audio_cuack = ["cuack", "cuac", "cuak", "pato", "kuack", "kuac", "kuak"]
    audio_gaa = ["gaa"]
    audio_lapo = ["lapo", "push", "plus"]
    audio_ohno = ["ñoo", "oh"]
    audio_papi = ["papi", "cachame", "kchame", "kachame"]
    audio_oidos = ["chorri", "mano", "oido", "qven", "queven"]
    audio_sagasti = ["sagasti"]
    audio_auron = ["tengo", "miedo", "auron"]
    audio_nooo = ["pamela", "noo", "noni", "enojada"]
    audio_chupetin = ["chupet"]
    audio_aumrd = ["au", "mierda", "mrd"]
    audio_piero = ["shea", "bobo"]
    audio_ahoraque = ["ahora"]
    audio_equipo = ["equipo", "alfa", "buena", "maravilla", "onda", "dinamita", "escuadron", "lobo"]
    audio_cell = ["cell", "momento", "terror", "enese"]
    audio_raiden = ["destinos", "muerte", "peores", "raiden"]
    audio_woody = ["woody", "bien", "pensado", "budi", "budy", "wudy", "wudi", "gudi", "gudy", "wuudy"]
    audio_eleccion = ["eleccion"]
    audio_ricolas = ["ricolas", "rikolas", "joel"]
    audio_decepcion = ["decepcion", "traicon", "hermano", "amigo"]
    audio_diablos = ["diablo", "orita"]
    audio_nolose = ["dime", "nolose"]
    audio_algoandamal = ["algo", "anda", "mal"]
    audio_manuelgold = ["quee", "kee", "qee"]
    audio_oferton = ["ofert"]
    audio_escuchame = ["escuchame", "huevon", "webon", "wbn", "huebon", "wevon", "wn"]
    audio_aquaman = ["enfermo", "bruce", "wayne", "batman", "aquaman", "estas"]
    audio_yamete = ["yamete", "kudasai", "udasa"]
    audio_imbecil = ["imbe", "gracioso", "inve", "crees"]
    audio_chikistrikis = ["aqui", "aki", "istri"]
    audio_excita = ["porque", "excita", "tanto", "exita"]
    audio_segovia = ["mama", "unaputa", "govia", "chancro"]
    audio_divertido = ["divertido", "hijo", "perra"]
    audio_fiesta = ["suponia", "fiesta", "nose"]
    audio_estrategia = ["llamo", "sele", "estrategia"]
    audio_rick = ["parece", "rick", "falso"]
    audio_yalose = ["yalose", "maric"]
    audio_exhibiste = ["yanos", "exhibiste", "exibiste", "exiviste"]
    audio_quierellorar = ["quiere", "llorar", "vasa"]
    audio_cachera = ["calla", "cachera", "kchera", "kachera", "klla", "kalla"]
    audio_talla = ["aver", "haber", "esde", "talla"]
    audio_premiodoble = ["quebien", "qbien", "premio", "doble"]
    audio_listo = ["nome", "chico", "sea", "listo"]
    audio_porlaptm = ["porla", "ptm", "mare", "oepor", "por la"]
    audio_ratata = ["sabes", "español", "esta", "muy", "tata", "kata", "taka", "traka"]
    audio_soyyo = ["soy"]
    audio_siquemeinteresa = ["esosi", "queme", "interesa"]
    audio_tristepayaso = ["llevo", "vida", "triste", "payaso", "rie", "fuera", "llora", "dentro"]
    audio_freezer = ["basta", "freezer", "frizer", "friser", "frezer", "freeser", "freser", "goku"]
    audio_faraon = ["faraon", "love", "shady", "vengo", "ohme"]
    audio_cagon = ["dafonseka", "cagon", "kgon", "kagon", "dafonseca"]
    audio_meca = ["meca", "meka", "irreverencia", "irreverensia", "irreberencia", "irreberensia", "dross"]
    audio_vizcarra = ["vizcarra", "viscarra", "vizcara", "viscara"]
    audio_castillo = ["castillo", "castilo", "rondero"]
    audio_dota = ["dota", "chibolo"]
    audio_r5 = ["r5"]
    audio_yoyaestoy = ["yoya", "estoy", "enchufe"]
    audio_jimmysanty = ["pero", "eres", "jimmy", "santy", "santi", "jimmi", "jimy", "yimi", "yimy", "yimmi", "yimmy"]
    audio_desahuevate = ["desahuevate", "concha", "desawebate", "desahuebate"]
    audio_mamita = ["tuno", "tienes", "mamita", "manita"]
    audio_wtfmicerebro = ["wtf", "wdf", "cerebro"]
    audio_drogaalallama = ["pucta", "droga", "llama", "ledio", "puta"]
    audio_tepha = ["asco"]

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
        
    elif any(word in arreglar(str(args)).lower() for word in audio_listo):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/No me parece que este chico sea muy listo.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_porlaptm):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Oe, por la ptm.mp3"))
        time.sleep(5)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_ratata):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Tú sabes que mi español está muy ratata.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_soyyo):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Ah, caray, soy yo.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_siquemeinteresa):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Ah, caray, eso sí me interesa.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_tristepayaso):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Llevo la vida de un triste payaso que ríe por fuera y llora por dentro.mp3"))
        time.sleep(8)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_freezer):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Ya basta, Freezer.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_faraon):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Oh, me vengo.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_cagon):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Ah, cagón.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_meca):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Es la meca de la irreverencia.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_vizcarra):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Vizcarra.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_castillo):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Castillo.mp3"))
        time.sleep(3)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_dota):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Dota.mp3"))
        time.sleep(36)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_r5):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/r5.ogg"))
        time.sleep(9)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_yoyaestoy):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Yo ya estoy.mp3"))
        time.sleep(1)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_jimmysanty):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Pero eres o no eres.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_desahuevate):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Desahuévate, conchatumare.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_mamita):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Tú no tienes mamita, mano.mp3"))
        time.sleep(2)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_wtfmicerebro):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Wtf mi cerebro.mp3"))
        time.sleep(8)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_drogaalallama):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Quién pucta le dio droga a la llama.mp3"))
        time.sleep(21)
        await ctx.guild.voice_client.disconnect()
        
    elif any(word in arreglar(str(args)).lower() for word in audio_tepha):
        await ctx.channel.purge(limit=1)
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio("audios/Tepha.ogg"))
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
        ¿Quiere llorar?\n\nCalla, cachera\n\nA ver si esto es de tu talla\n\nMuy bien, premios dobles\n\n \
        No me parece que este chico sea muy listo\n\nOe, por la ptm\n\n \
        Tú sabes que mi español está muy ratata\n\nAh, caray, soy yo\n\nAh, caray, eso sí me interesa\n\n \
        Llevo la vida de un triste payaso que ríe por fuera y llora por dentro\n\nYa basta, Freezer\n\n \
        Oh, me vengo\n\nAh, cagón\n\nEs la meca de la irreverencia\n\nVizcarra\n\nCastillo\n\n \
        Oye mierda corre báñate carajo lee un libro\n\nR5\n\nYo ya estoy\n\nPero eres o no eres?\n\n \
        Desahuévate, conchatumare\n\nTú no tienes mamita, mano?\n\nWtf mi cerebro\n\n \
        Quién pucta le dio droga a la llama?\n\nPuta, qué asco"
    )
    await ctx.send(embed=em)


client.run("ODA1NDg1MTk5MDY0NDMyNjgz.YBbkjA.-EWlOYH_3e6QPdMcXB6tjXasKYI")
