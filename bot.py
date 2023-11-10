import discord
import os
import os.path
import random
from pathlib import Path
from discord.ext import commands
import asyncio
import time
import datetime

# Arrays to include people in. For Cooldown, benefits, etc.
# I mean, we could integrate an Database here so the benefits aren't actually lost, but no one
# really cares about it.
users_on_cooldown = []
daily_cooldown = []
bought_two = []
bought_four = []
roleta_cooldown = []
investir_cooldown = []
rinha_cooldown = []
rinha_resposta_cooldown = []
# In the old bot we actually used a file to verify if this was active, but in rewrite let's just use an array.
uwu_array = []

# Defining the cooldown.
cooldown_command = 5

# Now This is the bot's code.
# First, define perms, prefix and the rest of useless shit.
intents = discord.Intents.all()
intents.message_content = True
prefixes = "d$", "D$"
bot = commands.Bot(command_prefix=prefixes, intents=intents)


# Define the XP functions we need.
def increase_xp(user_sent, amount: int):
    checkprofile(user_sent)
    current_xp = int(open(f"profile/{user_sent}/experience", "r+").read())
    with open(f'profile/{user_sent}/experience', 'w') as f:
        f.write(str(current_xp + amount))


def decrease_xp(user_sent, amount: int):
    checkprofile(user_sent)
    current_xp = int(open(f"profile/{user_sent}/experience", "r+").read())
    with open(f'profile/{user_sent}/experience', 'w') as f:
        if current_xp - amount < 0:
            f.write("0")
        else:
            f.write(str(current_xp - amount))


# Define function to check for user's folders, pretty useful.
def checkprofile(user_sent):
    if Path(f"profile/{user_sent}").exists() is False:
        os.makedirs(f"profile/{user_sent}")
        with open(f'profile/{user_sent}/user', 'w') as f:
            f.write(str(user_sent))
        with open(f'profile/{user_sent}/coins', 'w') as f:
            f.write("0")
    if Path(f"profile/{user_sent}/duelos").exists() is False:
        with open(f'profile/{user_sent}/duelos', 'w') as f:
            f.write("0")
    if Path(f"profile/{user_sent}/duelos_vencidos").exists() is False:
        with open(f'profile/{user_sent}/duelos_vencidos', 'w') as f:
            f.write("0")
    if Path(f"profile/{user_sent}/duelos_perdidos").exists() is False:
        with open(f'profile/{user_sent}/duelos_perdidos', 'w') as f:
            f.write("0")
    if Path(f"profile/{user_sent}/experience").exists() is False:
        with open(f'profile/{user_sent}/experience', 'w') as f:
            f.write("0")


# Initiate Bot's log, and define on_message functions.
@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')


@bot.event
async def on_message(message):
    # Just define the cooldown variable so we can know who bought the first benefit.
    if message.author == bot.user:
        return
    elif message.author.bot is True:
        return
    elif "calcinha" in message.content.lower():
        if "active" in uwu_array:
            jokes = "Quewia tanto OwO tew uma..."
        else:
            jokes = "Queria tanto ter uma..."
        await message.channel.send(jokes)
    if "peitos" in message.content.lower():
        if "active" in uwu_array:
            jokes = ["PEITOS?!?! aONDE?!?1 *sweats* PEITOS PEITOS PEITOS PEITOS AAAAAAAAAAAAAA", "São >w< tão macios... quewia pegaw em uns peitos...", "EU QUEWO PEITOOOOOOOOOOS", "Sou o maiow fã de peitos do mundo"]
        else:
            jokes = ["PEITOS???? AONDE?????? PEITOS PEITOS PEITOS PEITOS AAAAAAAAAAAAAA", "São tão macios... queria pegar em uns peitos...", "EU QUERO PEITOOOOOOOOOOS", "Sou o maior fã de peitos do mundo"]
        await message.channel.send(random.choice(jokes))
    increase_xp(message.author.id, 2)
    await bot.process_commands(message)


# Global error catching
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("Esse comando não existe. Desculpe!")
    elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        await ctx.send("Me parece que o comando que você está tentando usar requer um ou mais argumentos.")
    elif isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send("Você não é ADM... Boa tentativa.")


# About Command
# We Also define the uptime function here since that is really the only place we use it.
# We also register the Boot Time for future use.
BOOT_TIME = time.time()


def uptime():
    return str(datetime.timedelta(seconds=int(time.time() - BOOT_TIME)))


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def sobre(ctx):
    print(cooldown_command)
    the_user = bot.get_user(int("727194765610713138"))
    embed = discord.Embed(title='DenjiBot', colour=0x00b0f4)
    embed.set_thumbnail(url=bot.user.display_avatar)
    embed.add_field(name="Tempo Ligado:", value=uptime(), inline=True)
    embed.set_footer(text="Feito por Jocadbz",
                     icon_url=the_user.display_avatar)
    await ctx.send(embed=embed)


# UWU COMMAND
# Enables the UwU mode Nya!
@bot.command()
@commands.has_permissions(administrator=True)
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def increasexp(ctx, amount: int, user: discord.Member):
    increase_xp(user.id, amount)
    await ctx.send(f"Adicionou {amount} XP para {user.display_name}")


# UWU COMMAND
# Enables the UwU mode Nya!
@bot.command()
@commands.has_permissions(administrator=True)
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def decreasexp(ctx, amount: int, user: discord.Member):
    decrease_xp(user.id, amount)
    await ctx.send(f"Removeu {amount} XP de {user.display_name}")


# Battle Command
# Simmulates an idiotic battle between two concepts.
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def battle(ctx, arg1, arg2):
    rand1 = [0, 1]
    if "active" in uwu_array:
        if random.choice(rand1) == 0:
            comeco = ["Foi pow pouco, mas ", "E com gwande fowga ", "Foi uma wuta justa, mas "]
            fim = ["esmagando seu c-cwânyio", "abwindo um buwaco em seu peito.", "decepando s-s-sua cabeça."]
            jokes = f"{random.choice(comeco)}{arg1} ganhow a l-luta contwa {arg2} {random.choice(fim)}"
            await ctx.send(jokes)
        else:
            comeco = ["Foi pow pouco, mas ", "E com gwande fowga ", "Foi uma wuta justa, mas "]
            fim = ["esmagando seu c-cwânyio", "abwindo um buwaco em seu peito.", "decepando s-s-sua cabeça.", "desintegwando seu cowpo.", "sewwando seu c-cowpo ao meio."]
            jokes = f"{random.choice(comeco)}{arg2} ganhow a l-luta contwa {arg1} {random.choice(fim)}"
            await ctx.send(jokes)
    else:
        if random.choice(rand1) == 0:
            comeco = ["Foi por pouco, mas ", "E com grande folga, ", "Foi uma luta justa, mas "]
            fim = ["esmagando seu crânio.", "abrindo um buraco em seu peito.", "decepando sua cabeça."]
            jokes = f"{random.choice(comeco)}{arg1} ganhou a luta contra {arg2} {random.choice(fim)}"
            await ctx.send(jokes)
        else:
            comeco = ["Foi por pouco, mas ", "E com grande folga, ", "Foi uma luta justa, mas "]
            fim = ["esmagando seu crânio.", "abrindo um buraco em seu peito.", "decepando sua cabeça.", "desintegrando seu corpo.", "serrando seu corpo ao meio."]
            jokes = f"{random.choice(comeco)}{arg2} ganhou a luta contra {arg1} {random.choice(fim)}"
            await ctx.send(jokes)


# Gerador de cancelamento
# Roubado de um certo site
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def cancelamento(ctx):
    if "active" in uwu_array:
        motivos = ["sew ;;w;; atwaente d-demais", "tew chawme d-demais", "sew ;;w;; uma pessoa howwívew", "sew ;;w;; uma gwande gostosa", "sew ;;w;; boy wixo", "sew ;;w;; comunyista", "debochaw *blushes* demais sew intewigente d-demais", "sew ;;w;; p-padwãozinho", "pediw ^w^ muito biscoito", "sew ;;w;; cownyo sew uma dewícia", "sew ;;w;; gado d-demais", "não sew nyinguém", "sew ;;w;; posew", "sew ;;w;; insupowtávew", "sew ;;w;; insensívew", "não fazew nyada", "sew ;;w;; twouxa", "se atwasaw", "sempwe sew impaciente d-demais", "tew viwado o Cowonga", "sew ;;w;; BV", "tew muita pweguiça", "sew ;;w;; inútiw", "sew ;;w;; inyadimpwente >w< nyo S-Sewasa", "contaw muita piada wuim", "pwocwastinyaw d-demais", "pow se considewaw incancewávew"]
        await ctx.send(f"{ctx.author.mention} foi cancewado pow {random.choice(motivos)}")
    else:
        motivos = ["ser atraente demais", "ter charme demais", "ser uma pessoa horrível", "ser uma grande gostosa", "ser boy lixo", "ser comunista", "debochar demais ser inteligente demais", "ser padrãozinho", "pedir muito biscoito", "ser corno ser uma delícia", "ser gado demais", "não ser ninguém", "ser poser", "ser insuportável", "ser insensível", "não fazer nada", "ser trouxa", "se atrasar", "sempre ser impaciente demais", "ter virado o Coronga", "ser BV", "ter muita preguiça", "ser inútil", "ser inadimplente no Serasa", "contar muita piada ruim", "procrastinar demais", "por se considerar incancelável"]
        await ctx.send(f"{ctx.author.mention} foi cancelado por {random.choice(motivos)}")


# SÁBIO
# Obtenha respostas para as questões mais importantes da vida.
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def sabio(ctx):
    if "active" in uwu_array:
        jokes = ["SIM, C-C-COM TODA CEWTEZA", "Sim, >w< com cewteza.", "Sim.", "Pwovavewmente.", "Não sei dizew.", "Pwovavewmente não.", "Não.", 'Com c-cewteza n-não.', "NÃO, C-C-COM TODA CEWTEZA NÃO", "O Padowa é-é quem decide UWU"]
    else:
        jokes = ["SIM, COM TODA CERTEZA", "Sim, com certeza.", "Sim.", "Provavelmente.", "Não sei dizer.", "Provavelmente não.", "Não.", 'Com certeza não.', "NÃO, COM TODA CERTEZA NÃO", "O Padola decide."]
    await ctx.send(random.choice(jokes))


# PPT
# Declaração de amor via Discord... que brega.
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def ppt(ctx, lover):
    if 'active' in uwu_array:
        jokes = f"Cawo/Cawa {lover}, o {ctx.author.mention} gostawia de d-decwawaw seus sentimentos a você."
    else:
        jokes = f"Caro/Cara {lover}, o {ctx.author.mention} gostaria de declarar seus sentimentos a você."
    await ctx.send(jokes)


# Jogo
# Simulação do jogo de futebol do seu time. Que você sabe que vai perder.
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def jogo(ctx, time1, time2):
    rand1 = [0, 1, 2, 3, 4, 5]
    if "active" in uwu_array:
        jokes = f"O wesuwtado da pawtida de {time1} x {time2} vai sew {random.choice(rand1)} x {random.choice(rand1)} UWU"
    else:
        jokes = f"O resultado da partida de {time1} x {time2} vai ser {random.choice(rand1)} x {random.choice(rand1)}"
    await ctx.send(jokes)


# Comprar
# Cobrando por PadolaCoins KKKKKKKKKKKKKKK.
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def comprar(ctx):
    thing = """Ficou sem dinheiro apostando com o ADM? Agora você pode realizar a compra de PadolaCoins!
Comprar PadolaCoins é um jeito de ajudar o bot a continuar online, ajuda o criador a pagar as contas, e principalmente, nos ajuda a continuar desenvolvendo!

Para comprar, chame o criador do DenjiBot (@jocadbz) na DM. O valor é negociável."""
    await ctx.send(thing)
    await ctx.send("https://tenor.com/view/mlem-silly-goofy-cat-silly-cat-goofy-gif-27564930")


# Ping
# Não estamos nos referindo ao esporte.
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def ping(ctx):
    if round(bot.latency * 1000) <= 50:
        embed = discord.Embed(title="Ping", description=f":ping_pong: Pingpingpingpingping! O ping é de **{round(bot.latency *1000)}** millisegundos!", color=0x44ff44)
    elif round(bot.latency * 1000) <= 100:
        embed = discord.Embed(title="Ping", description=f":ping_pong: Pingpingpingpingping! O ping é de **{round(bot.latency *1000)}** millisegundos!", color=0xffd000)
    elif round(bot.latency * 1000) <= 200:
        embed = discord.Embed(title="Ping", description=f":ping_pong: Pingpingpingpingping! O ping é de **{round(bot.latency *1000)}** millisegundos!", color=0xff6600)
    else:
        embed = discord.Embed(title="Ping", description=f":ping_pong: Pingpingpingpingping! O ping é de **{round(bot.latency *1000)}** millisegundos!", color=0x990000)
    await ctx.send(embed=embed)


# Comandos Customizados pedidos por pessoas


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def fanho(ctx):
    await ctx.send("https://tenor.com/view/makima-bean-beans-chainsaw-man-gif-25992235")


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def fanho2(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1164692508668862515/1171207341488750714/image0.gif?ex=655bd6d6&is=654961d6&hm=e139f0b8fefedde2b29d3a57212c3111a23db7cfe529ae4e931aac42d11349bb&")


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def reze69(ctx):
    await ctx.send("https://tenor.com/view/rolando-ronaldo-cristiano-gif-26255427")


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def suro(ctx):
    await ctx.send("https://media.discordapp.net/attachments/804443142879182871/941984752603398154/image0-156.gif")


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def dani(ctx):
    await ctx.send("https://tenor.com/view/gojo-gojo-satoru-dancing-jjk-jujutsu-kaisen-gif-25819377")


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def dani2(ctx):
    await ctx.send("https://tenor.com/view/choso-choso-jjk-choso-jujutsu-kaisen-choso-anime-jujutsu-kaisen-gif-10037971888755283102")


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def kaishl(ctx):
    await ctx.send("https://tenor.com/view/bom-dia-valtatui-valtatui-bom-dia-gif-25587386")


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def skyte(ctx):
    await ctx.send("https://tenor.com/view/ronaldo-win-ronaldo-award-ronaldo-gif-24123234")


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def lana(ctx):
    await ctx.send("https://tenor.com/view/himeno-himmy-himeno-chainsaw-man-banging-headbanging-gif-6931555360158583987")


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def padola(ctx):
    gifs = ["https://tenor.com/view/saber-burger-gif-23551262", "https://tenor.com/view/majima-smoke-majima-majima-walking-gif-27442361"]
    await ctx.send(random.choice(gifs))


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def joca(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1164700096668114975/1172164504726028379/image0.gif?ex=655f5243&is=654cdd43&hm=8338bbfcd2ad9857b34d320d456d9ad2e521ab109ceb2db19a2a60e543a4fe27&")


# DAILY
# Win 100 PadolaCoins every 40 minutes.
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def daily(ctx):
    checkprofile(ctx.author.id)

    if ctx.author in daily_cooldown:
        if 'active' in uwu_array:
            await ctx.send("opaaa ÚwÚ pewa *cries* w-wá, você já pegou seus Denji Coins diáwios. Espewe m-mais um tempo pawa pegaw nyovamente. *sweats* (Dica UWU: d$comprar)")
        else:
            await ctx.send("Opaaa pera lá, você já pegou seus Denji Coins diários. Espere mais um tempo para pegar novamente. (Dica: d$comprar)")

    else:
        current_coins = open(f"profile/{ctx.author.id}/coins", "r+").read()
        new_coins = int(current_coins) + 100
        with open(f'profile/{ctx.author.id}/coins', 'w') as f:
            f.write(str(new_coins))
        if 'active' in uwu_array:
            await ctx.send(f"Você ganhou 100 PadowaCoins?!?1")
        else:
            await ctx.send(f"Você ganhou 100 PadolaCoins!")
        daily_cooldown.append(ctx.author)
        await asyncio.sleep(2500)
        daily_cooldown.remove(ctx.author)


# Profile
# Check User Profile
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
# TODO: Try to find a way of reducing code in this specific command.
async def profile(ctx, rsuser: discord.Member = None):
    if rsuser is not None:
        # TODO: Fix the fact that this gets ignored if we throw any letters at it.
        user_sent = rsuser.id
        if bot.get_user(int(user_sent)) is None:
            await ctx.send(f"Tem certeza de que esse user existe?")
            return
    else:
        user_sent = ctx.author.id

    checkprofile(user_sent)

    embed = discord.Embed(title=f"Perfil do {bot.get_user(int(user_sent))}",
                          description="*Use d$daily e d$roleta para ganhar PadolaCoins!*",
                          colour=0x00b0f4)

    embed.add_field(name="Padola Coins",
                    value=f"""{open(f"profile/{user_sent}/coins", "r+").read()}""",
                    inline=False)
    embed.add_field(name="Pontos de Experiência",
                    value=f"""{open(f"profile/{user_sent}/experience", "r+").read()} XP""",
                    inline=False)
    embed.add_field(name="Apostas vencidas",
                    value=f"""{open(f"profile/{user_sent}/duelos", "r+").read()}""",
                    inline=False)
    embed.add_field(name="Duelos Mortalmente Mortais",
                    value=f"""Ganhou {open(f"profile/{user_sent}/duelos_vencidos", "r+").read()} - Perdeu {open(f"profile/{user_sent}/duelos_perdidos", "r+").read()}""",
                    inline=False)

    embed.set_thumbnail(url=bot.get_user(int(user_sent)).display_avatar)

    embed.set_footer(text="Denji-kun Bot",
                     icon_url=bot.user.display_avatar)
    await ctx.send(embed=embed)


# Lojinha
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def lojinha(ctx, arg1=None):
    checkprofile(ctx.author.id)
    if arg1 == "1":
        current_coins = open(f"profile/{ctx.author.id}/coins", "r+").read()
        if int(current_coins) >= 500:
            new_coins = int(current_coins) - 500
            with open(f'profile/{ctx.author.id}/coins', 'w') as f:
                f.write(str(new_coins))
            if "active" in uwu_array:
                await ctx.send("Você compwou o benyefício 1.")
            else:
                await ctx.send("Você comprou o benefício 1.")
            bought_two.append(ctx.author)
            await asyncio.sleep(2500)  # time in seconds
            bought_two.remove(ctx.author)
        else:
            if "active" in uwu_array:
                await ctx.send("Ah mais que triste. Você não tem PadolaCoins o suficiente. (Dica: d$comprar)")
            else:
                await ctx.send("A-Ah, m-mais que twiste!!11 você não tem PadowaCoins o suficiente. *looks at you* (Dica UWU: d$comprar)")
    elif arg1 == "2":
        current_coins = open(f"profile/{ctx.author.id}/coins", "r+").read()
        if int(current_coins) >= 100000:
            if "active" in uwu_array:
                await ctx.send("Você compwou o benyefício 2. Wesponda a essa mensagem como você quew o comando.")
            else:
                await ctx.send("Você comprou o benefício 2. Responda a essa mensagem como você quer o comando.")

            def sus(m):
                return m.author == ctx.author

            try:
                msg = await bot.wait_for('message', check=sus)
            except asyncio.TimeoutError:
                await ctx.send('Compra cancelada. Tente novamente.')
            else:
                await ctx.send('Comando registrado.')
                new_coins = int(current_coins) - 100000
                with open(f'profile/{ctx.author.id}/coins', 'w') as f:
                    f.write(str(new_coins))
                admmasterblaster = await bot.fetch_user("727194765610713138")
                await admmasterblaster.send(f"""Atenção Adm, o {ctx.author.name} comprou um comando personalizado. Ele quer desse jeito: "{msg.content}" """)
        else:
            if "active" not in uwu_array:
                await ctx.send("Ah mais que triste. Você não tem PadolaCoins o suficiente. (Dica: d$comprar)")
            else:
                await ctx.send("A-Ah, m-mais que twiste!!11 você não tem PadowaCoins o suficiente. *looks at you* (Dica UWU: d$comprar)")
    elif arg1 == "3":
        current_coins = open(f"profile/{ctx.author.id}/coins", "r+").read()
        if int(current_coins) >= 1500:
            new_coins = int(current_coins) - 1500
            with open(f'profile/{ctx.author.id}/coins', 'w') as f:
                f.write(str(new_coins))
            if "active" in uwu_array:
                await ctx.send("Você compwou o benyefício 3.")
            else:
                await ctx.send("Você comprou o benefício 3.")
            bought_four.append(ctx.author)
            await asyncio.sleep(2500)  # time in seconds
            bought_four.remove(ctx.author)
        else:
            if "active" not in uwu_array:
                await ctx.send("Ah mais que triste. Você não tem PadolaCoins o suficiente. (Dica: d$comprar)")
            else:
                await ctx.send("A-Ah, m-mais que twiste!!11 você não tem PadowaCoins o suficiente. *looks at you* (Dica UWU: d$comprar)")

    elif arg1 is None:
        if "active" in uwu_array:
            embed = discord.Embed(title="wojinha *huggles tightly* do Denji",
                                  description="compwe >w< benyefícios :3 com seus Padowa *walks away* Coins aqui?!?! - Mande o comando 'd$lojinha <numero>' pawa compwaw!!11 *screeches*",
                                  colour=0x00b0f4)

            embed.add_field(name="I - Rinha e d-duelo Coowdown Wemuvw UWU",
                            value="Não seja afetado pewo coowdown das apostas e d-duelo pow 40 m-minyutos - 500 PadowaCoins",
                            inline=False)
            embed.add_field(name="II - C-Comando customizado",
                            value="cowoque :3 um comando customizado com seu usewnyame ;;w;; - 100000 PadowaCoins",
                            inline=False)
            embed.add_field(name="III - Sonyegaw impostos",
                            value="Seja um fowa da wei e pague zewo impostos nya s-suas twansfewencias pow 40 m-minyutos - 1500 PadowaCoins",
                            inline=False)

            embed.set_footer(text="Denji-kun Bot",
                             icon_url=bot.user.display_avatar)
        else:
            embed = discord.Embed(title="Lojinha do Denji",
                                  description="Compre benefícios com seus Padola Coins aqui! - Mande o comando '$lojinha <numero>' para comprar!",
                                  colour=0x00b0f4)

            embed.add_field(name="I - Rinha e Duelo Cooldown Remover",
                            value="Não seja afetado pelo cooldown das apostas e duelos por 40 minutos - 500 PadolaCoins",
                            inline=False)
            embed.add_field(name="II - Comando customizado",
                            value="Coloque um comando customizado com seu username - 100000 PadolaCoins",
                            inline=False)
            embed.add_field(name="III - Sonegar impostos",
                            value="Seja um fora da lei e pague zero impostos na suas transferencias por 40 minutos - 1500 PadolaCoins",
                            inline=False)

            embed.set_footer(text="Denji-kun Bot",
                             icon_url=bot.user.display_avatar)

        await ctx.send(embed=embed)


# Investir
# Perder ou ganhar? É o bot quem decide.
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def investir(ctx, arg1: int):
    checkprofile(ctx.author.id)

    investir_random = ["win", "lose", "lose", "lose", "win", "lose", "win", "lose"]
    resultado = random.choice(investir_random)
    win_thing = [4, 10, 2, 2, 4, 5]
    win_thing = random.choice(win_thing)

    if arg1 > int(open(f"profile/{ctx.author.id}/coins", "r+").read()):
        if 'active' in uwu_array:
            await ctx.send("Você não tem fundos o s-suficiente pwa i-investiw. (Dica UWU: d$comprar)")
        else:
            await ctx.send("Você não tem fundos o suficiente pra investir. (Dica: d$comprar)")
    else:
        if resultado == "win":
            if 'active' in uwu_array:
                await ctx.send(f"Você wucwou {str(win_thing).replace('0.', '')}%! seu ^w^ wucwo totaw :3 foi {int(int(arg1)*win_thing / 100)} PadowaCoins!")
            else:
                await ctx.send(f"Você lucrou {str(win_thing).replace('0.', '')}%! Seu lucro total foi {int(int(arg1)*win_thing / 100)} PadolaCoins!")
            current_coins = open(f"profile/{ctx.author.id}/coins", "r+").read()
            new_coins = int(round(int(arg1) * win_thing / 100))
            new_coins = int(int(current_coins) + new_coins)
            with open(f'profile/{ctx.author.id}/coins', 'w') as f:
                f.write(str(new_coins))
        else:
            if 'active' in uwu_array:
                await ctx.send(f"Você pewdeu {str(win_thing).replace('0.', '')}%! Suas pewdas totais fowam *twerks* {int(round(int(arg1)*win_thing / 100))} PadowaCoins... Boa sowte nya pwóxima...")
            else:
                await ctx.send(f"Você perdeu {str(win_thing).replace('0.', '')}%! Suas perdas totais foram {int(round(int(arg1)*win_thing / 100))} PadolaCoins... Boa sorte na próxima...")
            current_coins = open(f"profile/{ctx.author.id}/coins", "r+").read()
            new_coins = int(round(int(arg1) * win_thing / 100))
            new_coins = int(int(current_coins) - new_coins)
            with open(f'profile/{ctx.author.id}/coins', 'w') as f:
                f.write(str(new_coins))


# Roleta
# Roda a Roda jequiti
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def roleta(ctx):
    checkprofile(ctx.author.id)
    roleta_random = [100, 10, 50, 200, 0, 100, 10, 10, 400, 400, 200, 200, 100, 100, 10, 200, 0, 0, 400]
    resultado = random.choice(roleta_random)

    if ctx.author in roleta_cooldown:
        if 'active' in uwu_array:
            await ctx.send("opaaa ÚwÚ pewa *cries* w-wá, você já pegou seu giwo. Espewe m-mais um tempo pawa pegaw nyovamente. *sweats* (Dica UWU: d$comprar)")
        else:
            await ctx.send("Opaaa pera lá, você já pegou seu giro. Espere mais um tempo para pegar novamente. (Dica: d$comprar)")

    else:
        if 'active' in uwu_array:
            await ctx.send(f"O wesuwtado da s-s-sua w-woweta foi... {resultado} PadowaCoins?!?1")
        else:
            await ctx.send(f"O resultado da sua roleta foi... {resultado} PadolaCoins!")
            current_coins = open(f"profile/{ctx.author.id}/coins", "r+").read()
            new_coins = int(current_coins) + resultado
            with open(f'profile/{ctx.author.id}/coins', 'w') as f:
                f.write(str(new_coins))
            roleta_cooldown.append(ctx.author)
            await asyncio.sleep(2000)
            roleta_cooldown.remove(ctx.author)


# Doar
# MrBeast
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def doar(ctx, amount: int, user: discord.Member):
    checkprofile(ctx.author.id)
    if bot.get_user(user.id) is None:
        await ctx.send("Tem certeza de que esse user existe?")
    else:
        checkprofile(user.id)
        if amount > int(open(f"profile/{ctx.author.id}/coins", "r+").read()):
            if 'active' in uwu_array:
                await ctx.send("Você não tem fundos o s-suficiente pwa compwetaw essa t-twansação. (Dica UWU: d$comprar)")
            else:
                await ctx.send("Você não tem fundos o suficiente pra completar essa transação. (Dica: d$comprar)")
        else:
            current_coins = open(f"profile/{ctx.author.id}/coins", "r+").read()
            new_coins = int(current_coins) - amount
            if ctx.author in bought_four:
                imposto = 0
            else:
                imposto = round(amount) * 0.05
            current_coins_user = open(f"profile/{user.id}/coins", "r+").read()
            new_coins_user = int(current_coins_user) + amount
            new_coins_user = new_coins_user - imposto
            joca_coins = int(open(f"profile/727194765610713138/coins", "r+").read()) + imposto
            with open(f'profile/{ctx.author.id}/coins', 'w') as f:
                f.write(str(int(new_coins)))
            with open(f'profile/{user.id}/coins', 'w') as f:
                f.write(str(int(new_coins_user)))
            with open(f'profile/727194765610713138/coins', 'w') as f:
                f.write(str(int(joca_coins)))
            if ctx.author not in bought_four:
                if "active" in uwu_array:
                    await ctx.send(f"Você twansfewiu *looks at you* {amount} :3 Padowa *walks away* coins pawa {user.mention}! (imposto cobwado: {str(int(imposto))} PadowaCoins)")
                    await ctx.send(f"compwe >w< o benyefício 4 nya d$wojinha pawa não pagaw ^w^ impostos?!!")
                else:
                    await ctx.send(f"Você transferiu {amount} Padola coins para {user.mention}! (Imposto cobrado: {str(int(imposto))} PadolaCoins)")
                    await ctx.send(f"Compre o benefício 4 na d$lojinha para não pagar impostos!")
            else:
                if "active" in uwu_array:
                    await ctx.send(f"Você twansfewiu *looks at you* {amount} :3 Padowa *walks away* coins pawa {user.mention}! (Sem impostos cobwados *notices buldge*)")
                else:
                    await ctx.send(f"Você transferiu {amount} Padola coins para {user.mention}! (Sem impostos cobrados)")


@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def rinha(ctx, amount: int, user: discord.Member):
    checkprofile(ctx.author.id)
    if ctx.author in rinha_cooldown:
        if 'active' in uwu_array:
            await ctx.send("opaaa ÚwÚ pewa *cries* w-wá, você já apostou. Espewe m-mais um tempo pawa pegaw nyovamente. *sweats* (Dica: Você pode puwaw esse coowdown compwando o benyefício 2 nya d$wojinha)")
        else:
            await ctx.send("Opaaa pera lá, você já apostou. Espere o cooldown acabar. (Dica: Você pode pular esse cooldown comprando o benefício 2 na d$lojinha)")
    else:
        if amount > int(open(f"profile/{ctx.author.id}/coins", "r+").read()):
            if 'active' in uwu_array:
                await ctx.send("Você não tem fundos o s-suficiente pwa apostaw UWU (Dica UWU: d$comprar)")
            else:
                await ctx.send("Você não tem fundos o suficiente pra apostar. (Dica: d$comprar)")
        else:
            if user.id == ctx.author.id:
                if 'active' in uwu_array:
                    await ctx.send("Você não pode apostaw com você mesmo.")
                else:
                    await ctx.send("Você não pode apostar com você mesmo.")
            else:
                checkprofile(user.id)
                if amount > int(open(f"profile/{user.id}/coins", "r+").read()):
                    if 'active' in uwu_array:
                        await ctx.send("me *screeches* pawece que seu o-oponyente não pode cobwiw essa aposta... (Dica UWU: d$comprar)")
                    else:
                        await ctx.send("Me parece que seu oponente não pode cobrir essa aposta... (Dica: d$comprar)")
                else:
                    if 'active' in uwu_array:
                        aposta_message = await ctx.send(f"**Atenção {user.mention}, *screeches* o {ctx.author.mention} quew apostaw {amount} :3 PadowaCoins com você. Weaja a esta mensagem com um e-emoji de d-dedão '👍' em 15 segundos pawa concowdaw com a aposta.**")
                    else:
                        aposta_message = await ctx.send(f"**Atenção {user.mention}, o {ctx.author.mention} quer apostar {amount} PadolaCoins com você. Reaja a esta mensagem com um emoji de dedão '👍' em 15 segundos para concordar com a aposta.**")
                    await aposta_message.add_reaction('👍')

                    def check(reaction, user):
                        return user == user and str(reaction.emoji) == '👍'
                    try:
                        reaction, user = await bot.wait_for('reaction_add', timeout=15.0, check=check)
                    except asyncio.TimeoutError:
                        if 'active' in uwu_array:
                            await ctx.send("Aposta c-cancewada UWU")
                        else:
                            await ctx.send("Aposta cancelada")
                    else:
                        if 'active' in uwu_array:
                            await ctx.send(f"O Ganhadow foi...")
                        else:
                            await ctx.send(f"O Ganhador foi...")
                        things = ["win", "lose", "win", "lose", "win", "lose", "win", "lose", "win", "lose"]
                        resultado = random.choice(things)
                        # You see this text down here? Pretty messy heh?
                        # The first thing you will think of doing is removing those useless variables, but here is the catch: It doesn't work without them.
                        # The code has a absolutely stroke, so I don't reccoment changing anything here.
                        if resultado == 'win':
                            if 'active' in uwu_array:
                                await ctx.send(f"{ctx.author.mention}!!11 Pawabéns, você ganhou {amount} :3 PadowaCoins?!?1")
                            else:
                                await ctx.send(f"{ctx.author.mention}! Parabéns, você ganhou {amount} PadolaCoins!")
                            current_coins = open(f"profile/{ctx.author.id}/coins", "r+").read()
                            new_coins = int(current_coins) + amount
                            current_coins_user = open(f"profile/{user.id}/coins", "r+").read()
                            new_coins_user = int(current_coins_user) - amount
                            with open(f'profile/{ctx.author.id}/coins', 'w') as f:
                                f.write(str(new_coins))
                            with open(f'profile/{user.id}/coins', 'w') as f:
                                f.write(str(new_coins_user))
                            current_duels_user = open(f"profile/{ctx.author.id}/duelos", "r+").read()
                            new_duels_user = int(current_duels_user) + 1
                            with open(f'profile/{ctx.author.id}/duelos', 'w') as f:
                                f.write(str(new_duels_user))

                        else:
                            if 'active' in uwu_array:
                                await ctx.send(f"{user.mention}!!11 Pawabéns, você ganhou {amount} :3 PadowaCoins?!?1")
                            else:
                                await ctx.send(f"{user.mention}! Parabéns, você ganhou {user.mention} PadolaCoins!")
                            current_coins = open(f"profile/{ctx.author.id}/coins", "r+").read()
                            new_coins = int(current_coins) - amount
                            current_coins_user = open(f"profile/{user.id}/coins", "r+").read()
                            new_coins_user = int(current_coins_user) + amount
                            with open(f'profile/{ctx.author.id}/coins', 'w') as f:
                                f.write(str(new_coins))
                            with open(f'profile/{user.id}/coins', 'w') as f:
                                f.write(str(new_coins_user))
                            current_duels_user = open(f"profile/{user.id}/duelos", "r+").read()
                            new_duels_user = int(current_duels_user) + 1
                            with open(f'profile/{user.id}/duelos', 'w') as f:
                                f.write(str(new_duels_user))
                        if ctx.author not in bought_two:
                            rinha_cooldown.append(ctx.author)
                            await asyncio.sleep(15)  # time in seconds
                            rinha_cooldown.remove(ctx.author)


# Duelo
# Extremamente utíl pra fazer GF- D-Digo, roleplay.
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def duelo(ctx, user: discord.Member):
    checkprofile(ctx.author.id)
    if ctx.channel.id == 767851776212336642:
        if 'active' in uwu_array:
            await ctx.send("O Tiwan- digo, ADM do Sewvew mandou tiwaw esse comando do G-Gewaw. Foi maw?!?1")
        else:
            await ctx.send("O Tiran- digo, ADM do Server mandou tirar esse comando do Geral. Foi mal!")
    else:
        if ctx.author in rinha_cooldown:
            if 'active' in uwu_array:
                await ctx.send("opaaa ÚwÚ pewa *cries* w-wá, você já duelou. Espewe m-mais um tempo pawa pegaw nyovamente. *sweats* (Dica: Você pode puwaw esse coowdown compwando o benyefício 2 nya d$lojinha)")
            else:
                await ctx.send("Opaaa pera lá, você já duelou. Espere o cooldown acabar. (Dica: Você pode pular esse cooldown comprando o benefício 2 na d$lojinha)")
        else:
            if user.id == ctx.author.id:
                if 'active' in uwu_array:
                    await ctx.send("Você não pode duewaw contwa você mesmo.")
                else:
                    await ctx.send("Você não pode duelar contra você mesmo.")
            else:
                checkprofile(user.id)
                if 'active' in uwu_array:
                    aposta_message = await ctx.send(f"**Atenção {user.mention}, *screeches* o {ctx.author.mention} quew duelaw :3 com você. Weaja a esta mensagem com um e-emoji de e-espada '⚔️' em 15 segundos pawa concowdaw com o d-duelo.**")
                else:
                    aposta_message = await ctx.send(f"**Atenção {user.mention}, o {ctx.author.mention} quer duelar com você. Reaja a esta mensagem com um emoji de espada '⚔️' em 15 segundos para concordar com o duelo.**")
                await aposta_message.add_reaction('⚔️')

                def check(reaction, user):
                    return user == user and str(reaction.emoji) == '⚔️'

                try:
                    reaction, user = await bot.wait_for('reaction_add', timeout=15.0, check=check)
                except asyncio.TimeoutError:
                    if 'active' in uwu_array:
                        await ctx.send("Duelo c-cancewada UWU")
                    else:
                        await ctx.send("Duelo cancelada")
                else:
                    if 'active' in uwu_array:
                        await ctx.send(f"O Ganhadow foi...")
                    else:
                        await ctx.send(f"O Ganhador foi...")
                    resultado = random.choice(["win", "lose"])
                    if resultado == 'win':
                        if 'active' in uwu_array:
                            await ctx.send(f"{ctx.author.mention}!!11 Pawabéns, você ganhou o d-duelo!")
                        else:
                            await ctx.send(f"{ctx.author.mention}! Parabéns, você ganhou duelo!")
                        current_duels_user = open(f"profile/{ctx.author.id}/duelos_vencidos", "r+").read()
                        new_duels_user = int(current_duels_user) + 1
                        with open(f'profile/{ctx.author.id}/duelos_vencidos', 'w') as f:
                            f.write(str(new_duels_user))
                        current_duels_user = open(f"profile/{user.id}/duelos_perdidos", "r+").read()
                        new_duels_user = int(current_duels_user) + 1
                        with open(f'profile/{user.id}/duelos_perdidos', 'w') as f:
                            f.write(str(new_duels_user))

                    else:
                        if 'active' in uwu_array:
                            await ctx.send(f"{user.mention}!!11 Pawabéns, você ganhou o d-duelo!")
                        else:
                            await ctx.send(f"{user.mention}! Parabéns, você ganhou o duelo!")
                        current_duels_user = open(f"profile/{user.id}/duelos_vencidos", "r+").read()
                        new_duels_user = int(current_duels_user) + 1
                        with open(f'profile/{user.id}/duelos_vencidos', 'w') as f:
                            f.write(str(new_duels_user))
                        current_duels_user = open(f"profile/{ctx.author.id}/duelos_perdidos", "r+").read()
                        new_duels_user = int(current_duels_user) + 1
                        with open(f'profile/{ctx.author.id}/duelos_perdidos', 'w') as f:
                            f.write(str(new_duels_user))
                    if ctx.author not in bought_two:
                        rinha_cooldown.append(ctx.author)
                        await asyncio.sleep(15)
                        rinha_cooldown.remove(ctx.author)
                    else:
                        pass


# Ajuda
# O comando de ajuda
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def ajuda(ctx):
    texto = """```
Guia de comandos:
- d$duelo <pessoa>
Inicia um duelo amigável.

- d$rinha <quantidade> <pessoa>
Aposta PadolaCoins com outra pessoa.

- d$doar <quantidade> <pessoa>
Transfere PadolaCoins para outra pessoa.

- d$roleta
Gire a roleta para ganhar PadolaCoins.

- d$lojinha
Uma lojinha para gastar seus PadolaCoins

- d$profile
Verifique seu perfil.

- d$daily
Ganhe seus PadolaCoins diários.

- d$suro, d$fanho, d$reze69
Cada um invoca um GIF diferente.

- d$comprar
Obtenha informações de como comprar PadolaCoins.

- d$jojo <time1> <time2>
Simule uma partida de futebol.

- d$sabio <pergunta>
Deixe o sábio responder a sua pergunta.

- d$battle <fighter1> <fighter2>
Simule uma batalha entre dois oponentes.

- d$rank <xp ou coins>
Calcule os top 5 mais ricos do servidor.

- d$uwu
A-Ative o modo UWU

### Apenas para Mods ###

- d$increasexp <quantidade> <pessoa>
Aumenta a quantidade de XP de uma pessoa.

- d$decreasexp <quantidade> <pessoa>
Diminui a quantidade de XP de uma pessoa.
```
"""
    await ctx.author.send(texto)


# The worst command ever
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def rank(ctx, arg1="coins"):
    if arg1 == "coins":
        the_ranked_array = []
        profiles = os.listdir("profile")
        profiles.remove("727194765610713138")
        for profile in profiles:
            coins = open(f"profile/{profile}/coins", "r+").read()
            the_ranked_array.append({'name': f'{bot.get_user(int(profile))}', 'coins': int(coins)})
        newlist = sorted(the_ranked_array, key=lambda d: d['coins'], reverse=True)
        the_array_to_send = []
        for idx, thing in enumerate(newlist):
            the_array_to_send.append(f"{idx+1} - {thing['name'].split('#')[0]}: {thing['coins']}")
            if idx == 4:
                break
        await ctx.send("Top 5 mais ricos do servidor:")
        for thing in the_array_to_send:
            await ctx.send(thing)
    elif arg1 == "xp":
        the_ranked_array = []
        profiles = os.listdir("profile")
        for profile in profiles:
            checkprofile(profile)
            coins = open(f"profile/{profile}/experience", "r+").read()
            the_ranked_array.append({'name': f'{bot.get_user(int(profile))}', 'coins': int(coins)})
        newlist = sorted(the_ranked_array, key=lambda d: d['coins'], reverse=True)
        the_array_to_send = []
        for idx, thing in enumerate(newlist):
            the_array_to_send.append(f"{idx+1} - {thing['name'].split('#')[0]}: {thing['coins']} XP")
            if idx == 4:
                break
        await ctx.send("Top 5 mais experientes do servidor:")
        for thing in the_array_to_send:
            await ctx.send(thing)
    else:
        await ctx.send("Argumento não suportado. Selecione 'xp' ou 'coins'.")


# Avatar
# See user avatar
@bot.command()
@commands.cooldown(1, cooldown_command, commands.BucketType.user)
async def avatar(ctx, user: discord.Member):
    embed = discord.Embed(title=f"Avatar de {user.display_name}",
                          colour=0x00b0f4)

    embed.set_image(url=user.display_avatar)

    await ctx.send(embed=embed)

bot.run(open(f"token", "r+").read())
