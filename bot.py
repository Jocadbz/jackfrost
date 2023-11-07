import discord 
import os
import os.path 
import random
from hentai import Hentai, Format
from pathlib import Path
from discord.ext import commands
import asyncio
users_on_cooldown = []
daily_cooldown = []

bought_one = []
bought_two = []
bought_four = []

roleta_cooldown = []
investir_cooldown = []

rinha_cooldown = []
rinha_resposta_cooldown = []

my_file = Path("uwu")



intents = discord.Intents.all() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT


token = open(f"token", "r+").read()

client = discord.Client(intents=intents)




@client.event 
async def on_ready(): 
    print("Logged in as a bot {0.user}".format(client))


@client.event
@commands.cooldown(1, 200000, commands.BucketType.user) 
async def on_message(message): 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.id) 
    user_message = str(message.content)
#    print(channel)

    if channel == "1164700096668114975":
        cooldown_command = 20
    else:
        cooldown_command = 5 


    if message.author == client.user: 
        return


    elif "d$ajuda" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$ajuda" == msgsplit[0]:
            texto = """Guia de comandos:
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

- d$uwu
A-Ative o modo UWU
"""
            await message.author.send(texto)
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass



    elif "d$duelo" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split()
        if channel == "1164700096668114975":
            if my_file.exists():
                await message.channel.send("O Tiwan- digo, ADM do Sewvew mandou tiwaw esse comando do G-Gewaw. Foi maw?!?1")
            else:
                await message.channel.send("O Tiran- digo, ADM do Server mandou tirar esse comando do Geral. Foi mal!")
        else:
            if "d$duelo" == msgsplit[0]:
                if Path(f"profile/{message.author.id}").exists() == False:
                    os.makedirs(f"profile/{message.author.id}")
                    with open(f'profile/{message.author.id}/user', 'w') as f:
                        f.write(str(message.author.id))
                    with open(f'profile/{message.author.id}/coins', 'w') as f:
                        f.write("0")
                else:
                    pass
                if Path(f"profile/{message.author.id}/duelos").exists() == False:
                    with open(f'profile/{message.author.id}/duelos', 'w') as f:
                        f.write("0")
                else:
                    pass
                if Path(f"profile/{message.author.id}/duelos_vencidos").exists() == False:
                    with open(f'profile/{message.author.id}/duelos_vencidos', 'w') as f:
                        f.write("0")
                else:
                    pass
                if Path(f"profile/{message.author.id}/duelos_perdidos").exists() == False:
                    with open(f'profile/{message.author.id}/duelos_perdidos', 'w') as f:
                        f.write("0")
                else:
                    pass
                if username in rinha_cooldown:
                    if my_file.exists():
                        await message.channel.send("opaaa ÚwÚ pewa *cries* w-wá, você já duelou. Espewe m-mais um tempo pawa pegaw nyovamente. *sweats* (Dica: Você pode puwaw esse coowdown compwando o benyefício 2 nya d$lojinha)")
                    else:
                        await message.channel.send("Opaaa pera lá, você já duelou. Espere o cooldown acabar. (Dica: Você pode pular esse cooldown comprando o benefício 2 na d$lojinha)")
                else:

                    if len(msgsplit) < 2:
                        if my_file.exists():
                            await message.channel.send("opa ÚwÚ patwão, escweve diweito. O comando é 'd$duelo <pessoa>'")
                        else:
                            await message.channel.send("Opa patrão, escreve direito. O comando é 'd$duelo <pessoa>'")

                    else:
                        if 1 == 2:
                            pass
                        else:
                            a = msgsplit[1]
                            a = a.replace("<","")
                            a = a.replace(">","")
                            user_sent = a.replace("@","")
                            if int(user_sent) == message.author.id:
                                if my_file.exists():
                                    await message.channel.send("Você não pode duewaw contwa você mesmo.")
                                else:
                                    await message.channel.send("Você não pode duelar contra você mesmo.")
                            else:
                                try:
                                    client.get_user(int(user_sent))
                                except ValueError:
                                    await message.channel.send(f"Tem certeza de que esse user existe?")
                                else:
                                    if client.get_user(int(user_sent)) is not None: # find ID by right clicking on a user and choosing "copy id" at the bottom
                                        if Path(f"profile/{user_sent}").exists() == False:
                                            os.makedirs(f"profile/{user_sent}")
                                            with open(f'profile/{user_sent}/user', 'w') as f:
                                                f.write(str(user_sent))
                                            with open(f'profile/{user_sent}/coins', 'w') as f:
                                                f.write("0")
                                        else:
                                            pass
                                        if Path(f"profile/{user_sent}/duelos").exists() == False:
                                            with open(f'profile/{user_sent}/duelos', 'w') as f:
                                                f.write("0")
                                        else:
                                            pass
                                        if Path(f"profile/{user_sent}/duelos_vencidos").exists() == False:
                                            with open(f'profile/{user_sent}/duelos_vencidos', 'w') as f:
                                                f.write("0")
                                        else:
                                            pass
                                        if Path(f"profile/{user_sent}/duelos_perdidos").exists() == False:
                                            with open(f'profile/{user_sent}/duelos_perdidos', 'w') as f:
                                                f.write("0")
                                        else:
                                            pass

                                        if 1 == 2:
                                            pass
                                        else:
                                            if my_file.exists():
                                                aposta_message = await message.channel.send(f"**Atenção <@{user_sent}>, *screeches* o {message.author.mention} quew duelaw :3 com você. Weaja a esta mensagem com um e-emoji de e-espada '⚔️' em 15 segundos pawa concowdaw com o d-duelo.**")
                                            else:
                                                aposta_message = await message.channel.send(f"**Atenção <@{user_sent}>, o {message.author.mention} quer duelar com você. Reaja a esta mensagem com um emoji de espada '⚔️' em 15 segundos para concordar com o duelo.**")
                                            await aposta_message.add_reaction('⚔️')

                                            def check(reaction, user):
                                                return user == client.get_user(int(user_sent)) and str(reaction.emoji) == '⚔️'
                                            try:
                                                reaction, user = await client.wait_for('reaction_add', timeout=15.0, check=check)
                                            except asyncio.TimeoutError:
                                                if my_file.exists():
                                                    await message.channel.send("Duelo c-cancewada UWU")
                                                else:
                                                    await message.channel.send("Duelo cancelada")
                                            else:
                                                if my_file.exists():
                                                    await message.channel.send(f"O Ganhadow foi...")
                                                else:
                                                    await message.channel.send(f"O Ganhador foi...")
                                                resultado = random.choice(["win", "lose"])
                                                if resultado == 'win':
                                                    if my_file.exists():
                                                        await message.channel.send(f"{message.author.mention}!!11 Pawabéns, você ganhou o d-duelo!")
                                                    else:
                                                        await message.channel.send(f"{message.author.mention}! Parabéns, você ganhou duelo!")
                                                    current_duels_user = open(f"profile/{message.author.id}/duelos_vencidos", "r+").read()
                                                    new_duels_user = int(current_duels_user)+1
                                                    with open(f'profile/{message.author.id}/duelos_vencidos', 'w') as f:
                                                        f.write(str(new_duels_user))
                                                    current_duels_user = open(f"profile/{user_sent}/duelos_perdidos", "r+").read()
                                                    new_duels_user = int(current_duels_user)+1
                                                    with open(f'profile/{user_sent}/duelos_perdidos', 'w') as f:
                                                        f.write(str(new_duels_user))
                                                    if username not in bought_two:
                                                        rinha_cooldown.append(username)
                                                        await asyncio.sleep(15)
                                                        rinha_cooldown.remove(username)
                                                    else:
                                                        pass

                                                else:
                                                    if my_file.exists():
                                                        await message.channel.send(f"<@{user_sent}>!!11 Pawabéns, você ganhou o d-duelo!")
                                                    else:
                                                        await message.channel.send(f"<@{user_sent}>! Parabéns, você ganhou o duelo!")
                                                    current_duels_user = open(f"profile/{user_sent}/duelos_vencidos", "r+").read()
                                                    new_duels_user = int(current_duels_user)+1
                                                    with open(f'profile/{user_sent}/duelos_vencidos', 'w') as f:
                                                        f.write(str(new_duels_user))
                                                    current_duels_user = open(f"profile/{message.author.id}/duelos_perdidos", "r+").read()
                                                    new_duels_user = int(current_duels_user)+1
                                                    with open(f'profile/{message.author.id}/duelos_perdidos', 'w') as f:
                                                        f.write(str(new_duels_user))
                                                    if username not in bought_two:
                                                        rinha_cooldown.append(username)
                                                        await asyncio.sleep(15)
                                                        rinha_cooldown.remove(username)
                                                    else:
                                                        pass
                                                if username not in bought_one:
                                                    users_on_cooldown.append(username)
                                                    await asyncio.sleep(cooldown_command) # time in seconds
                                                    users_on_cooldown.remove(username)
                                                else:
                                                    pass
                                    else:
                                        if my_file.exists():
                                            await message.channel.send(f"Ops, me pawece que você não cowocou um usew váwido...")
                                        else:
                                            await message.channel.send(f"Ops, me parece que você não colocou um user válido...")



            else:
                pass


    elif "d$rinha" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split()
        if "d$rinha" == msgsplit[0]:
            if Path(f"profile/{message.author.id}").exists() == False:
                os.makedirs(f"profile/{message.author.id}")
                with open(f'profile/{message.author.id}/user', 'w') as f:
                    f.write(str(message.author.id))
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write("0")
            else:
                pass
            if Path(f"profile/{message.author.id}/duelos").exists() == False:
                with open(f'profile/{message.author.id}/duelos', 'w') as f:
                    f.write("0")
            else:
                pass

            if username in rinha_cooldown:
                if my_file.exists():
                    await message.channel.send("opaaa ÚwÚ pewa *cries* w-wá, você já apostou. Espewe m-mais um tempo pawa pegaw nyovamente. *sweats* (Dica: Você pode puwaw esse coowdown compwando o benyefício 2 nya d$wojinha)")
                else:
                    await message.channel.send("Opaaa pera lá, você já apostou. Espere o cooldown acabar. (Dica: Você pode pular esse cooldown comprando o benefício 2 na d$lojinha)")
            else:

                if len(msgsplit) < 3:
                    if my_file.exists():
                        await message.channel.send("opa ÚwÚ patwão, escweve diweito. O comando é 'd$rinha <quantidade> <pessoa>'")
                    else:
                        await message.channel.send("Opa patrão, escreve direito. O comando é 'd$rinha <quantidade> <pessoa>'")

                else:
                    if int(msgsplit[1]) > int(open(f"profile/{message.author.id}/coins", "r+").read()):
                        if my_file.exists():
                            await message.channel.send("Você não tem fundos o s-suficiente pwa apostaw UWU (Dica UWU: d$comprar)")
                        else:
                            await message.channel.send("Você não tem fundos o suficiente pra apostar. (Dica: d$comprar)")
                    else:
                        a = msgsplit[2]
                        a = a.replace("<","")
                        a = a.replace(">","")
                        user_sent = a.replace("@","")
                        if int(user_sent) == message.author.id:
                            if my_file.exists():
                                await message.channel.send("Você não pode apostaw com você mesmo.")
                            else:
                                await message.channel.send("Você não pode apostar com você mesmo.")
                        else:

                            try:
                                client.get_user(int(user_sent))
                            except ValueError:
                                await message.channel.send(f"Tem certeza de que esse user existe?")
                            else:
                                if client.get_user(int(user_sent)) is not None: # find ID by right clicking on a user and choosing "copy id" at the bottom
                                    if Path(f"profile/{user_sent}").exists() == False:
                                        os.makedirs(f"profile/{user_sent}")
                                        with open(f'profile/{user_sent}/user', 'w') as f:
                                            f.write(str(user_sent))
                                        with open(f'profile/{user_sent}/coins', 'w') as f:
                                            f.write("0")
                                    else:
                                        pass
                                    if Path(f"profile/{user_sent}/duelos").exists() == False:
                                        with open(f'profile/{user_sent}/duelos', 'w') as f:
                                            f.write("0")
                                    else:
                                        pass
                                if int(msgsplit[1]) > int(open(f"profile/{user_sent}/coins", "r+").read()):
                                    if my_file.exists():
                                        await message.channel.send("me *screeches* pawece que seu o-oponyente não pode cobwiw essa aposta... (Dica UWU: d$comprar)")
                                    else:
                                        await message.channel.send("Me parece que seu oponente não pode cobrir essa aposta... (Dica: d$comprar)")
                                else:
                                    if my_file.exists():
                                        aposta_message = await message.channel.send(f"**Atenção {msgsplit[2]}, *screeches* o {message.author} quew apostaw {msgsplit[1]} :3 PadowaCoins com você. Weaja a esta mensagem com um e-emoji de d-dedão '👍' em 15 segundos pawa concowdaw com a aposta.**")
                                    else:
                                        aposta_message = await message.channel.send(f"**Atenção {msgsplit[2]}, o {message.author} quer apostar {msgsplit[1]} PadolaCoins com você. Reaja a esta mensagem com um emoji de dedão '👍' em 15 segundos para concordar com a aposta.**")
                                    await aposta_message.add_reaction('👍')

                                    def check(reaction, user):
                                        return user == client.get_user(int(user_sent)) and str(reaction.emoji) == '👍'
                                    try:
                                        reaction, user = await client.wait_for('reaction_add', timeout=15.0, check=check)
                                    except asyncio.TimeoutError:
                                        if my_file.exists():
                                            await message.channel.send("Aposta c-cancewada UWU")
                                        else:
                                            await message.channel.send("Aposta cancelada")
                                    else:
                                        if my_file.exists():
                                            await message.channel.send(f"O Ganhadow foi...")
                                        else:
                                            await message.channel.send(f"O Ganhador foi...")
                                        things = ["win", "lose", "win", "lose", "win", "lose", "win", "lose", "win", "lose"]
                                        resultado = random.choice(things)
                                        if resultado == 'win':
                                            if my_file.exists():
                                                await message.channel.send(f"{message.author}!!11 Pawabéns, você ganhou {msgsplit[1]} :3 PadowaCoins?!?1")
                                            else:
                                                await message.channel.send(f"{message.author}! Parabéns, você ganhou {msgsplit[1]} PadolaCoins!")
                                            current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                                            new_coins = int(current_coins)+int(msgsplit[1])
                                            current_coins_user = open(f"profile/{user_sent}/coins", "r+").read()
                                            new_coins_user = int(current_coins_user)-int(msgsplit[1])
                                            with open(f'profile/{message.author.id}/coins', 'w') as f:
                                                f.write(str(new_coins))
                                            with open(f'profile/{user_sent}/coins', 'w') as f:
                                                f.write(str(new_coins_user))
                                            current_duels_user = open(f"profile/{message.author.id}/duelos", "r+").read()
                                            new_duels_user = int(current_duels_user)+1
                                            with open(f'profile/{message.author.id}/duelos', 'w') as f:
                                                f.write(str(new_duels_user))
                                            if username not in bought_two:
                                                rinha_cooldown.append(username)
                                                await asyncio.sleep(15) # time in seconds
                                                rinha_cooldown.remove(username)
                                            else:
                                                pass

                                        else:
                                            if my_file.exists():
                                                await message.channel.send(f"{msgsplit[2]}!!11 Pawabéns, você ganhou {msgsplit[1]} :3 PadowaCoins?!?1")
                                            else:
                                                await message.channel.send(f"{msgsplit[2]}! Parabéns, você ganhou {msgsplit[1]} PadolaCoins!")
                                            current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                                            new_coins = int(current_coins)-int(msgsplit[1])
                                            current_coins_user = open(f"profile/{user_sent}/coins", "r+").read()
                                            new_coins_user = int(current_coins_user)+int(msgsplit[1])
                                            with open(f'profile/{message.author.id}/coins', 'w') as f:
                                                f.write(str(new_coins))
                                            with open(f'profile/{user_sent}/coins', 'w') as f:
                                                f.write(str(new_coins_user))
                                            current_duels_user = open(f"profile/{user_sent}/duelos", "r+").read()
                                            new_duels_user = int(current_duels_user)+1
                                            with open(f'profile/{user_sent}/duelos', 'w') as f:
                                                f.write(str(new_duels_user))
                                            if username not in bought_two:
                                                rinha_cooldown.append(username)
                                                await asyncio.sleep(15) # time in seconds
                                                rinha_cooldown.remove(username)
                                            else:
                                                pass


                if username not in bought_one:
                    users_on_cooldown.append(username)
                    await asyncio.sleep(cooldown_command) # time in seconds
                    users_on_cooldown.remove(username)
                else:
                    pass
        else:
            pass


    elif "d$doar" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split()

        if "d$doar" == msgsplit[0]:
            if Path(f"profile/{message.author.id}").exists() == False:
                os.makedirs(f"profile/{message.author.id}")
                with open(f'profile/{message.author.id}/user', 'w') as f:
                    f.write(str(message.author.id))
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write("0")
                if my_file.exists():

                    await message.channel.send("seu ^w^ pewfiw ^-^ foi cwiado?!! Mande o comando nyovamente. *sweats*")
                else:
                    await message.channel.send("Seu perfil foi criado! Mande o comando novamente.")
            else:

                if Path(f"profile/{message.author.id}/duelos").exists() == False:
                    with open(f'profile/{message.author.id}/duelos', 'w') as f:
                        f.write("0")
                else:
                    pass
            if len(msgsplit) < 3:
                if my_file.exists():
                    await message.channel.send("opa ÚwÚ patwão, escweve diweito. O comando é 'd$doawr <quantidade> <pessoa>'")
                else:
                    await message.channel.send("Opa patrão, escreve direito. O comando é 'd$doar <quantidade> <pessoa>'")


            else:
                a = msgsplit[2]
                a = a.replace("<","")
                a = a.replace(">","")
                user_sent = a.replace("@","") 
                if int(msgsplit[1]) > int(open(f"profile/{message.author.id}/coins", "r+").read()):
                    if my_file.exists():
                        await message.channel.send("Você não tem fundos o s-suficiente pwa compwetaw essa t-twansação. (Dica UWU: d$comprar)")
                    else:
                        await message.channel.send("Você não tem fundos o suficiente pra completar essa transação. (Dica: d$comprar)")
                else:
                    try:
                        client.get_user(int(user_sent))
                    except ValueError:
                        await message.channel.send(f"Tem certeza de que esse user existe?")
                    else:
                        if client.get_user(int(user_sent)) is not None: # find ID by right clicking on a user and choosing "copy id" at the bottom
                            if Path(f"profile/{user_sent}").exists() == False:
                                os.makedirs(f"profile/{user_sent}")
                                with open(f'profile/{user_sent}/user', 'w') as f:
                                    f.write(str(user_sent))
                                with open(f'profile/{user_sent}/coins', 'w') as f:
                                    f.write("0")
                            else:
                                pass
                            if Path(f"profile/{user_sent}/duelos").exists() == False:
                                with open(f'profile/{user_sent}/duelos', 'w') as f:
                                    f.write("0")
                            else:
                                pass
                            current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                            new_coins = int(current_coins)-int(msgsplit[1])
                            if username in bought_four:
                                imposto = 0
                            else:
                                imposto = round(int(msgsplit[1]) * 0.05)
                            current_coins_user = open(f"profile/{user_sent}/coins", "r+").read()
                            new_coins_user = int(current_coins_user)+int(msgsplit[1])
                            new_coins_user = new_coins_user-imposto
                            joca_coins = int(open(f"profile/727194765610713138/coins", "r+").read())+imposto 
                            with open(f'profile/{message.author.id}/coins', 'w') as f:
                                f.write(str(int(new_coins)))
                            with open(f'profile/{user_sent}/coins', 'w') as f:
                                f.write(str(int(new_coins_user)))
                            with open(f'profile/727194765610713138/coins', 'w') as f:
                                f.write(str(int(joca_coins)))
                            if username not in bought_four:
                                if my_file.exists():
                                    await message.channel.send(f"Você twansfewiu *looks at you* {msgsplit[1]} :3 Padowa *walks away* coins pawa {msgsplit[2]}! (imposto cobwado: {str(int(imposto))} PadowaCoins)")
                                    await message.channel.send(f"compwe >w< o benyefício 4 nya d$wojinha pawa não pagaw ^w^ impostos?!!")
                                else:
                                    await message.channel.send(f"Você transferiu {msgsplit[1]} Padola coins para {msgsplit[2]}! (Imposto cobrado: {str(int(imposto))} PadolaCoins)")
                                    await message.channel.send(f"Compre o benefício 4 na d$lojinha para não pagar impostos!")
                            else:
                                if my_file.exists():
                                    await message.channel.send(f"Você twansfewiu *looks at you* {msgsplit[1]} :3 Padowa *walks away* coins pawa {msgsplit[2]}! (Sem impostos cobwados *notices buldge*)")
                                else:
                                    await message.channel.send(f"Você transferiu {msgsplit[1]} Padola coins para {msgsplit[2]}! (Sem impostos cobrados)")
                        else:
                            await message.channel.send(f"Tem certeza de que esse user existe?")

            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass    

        else:
            pass

    elif "d$roleta" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$roleta" == msgsplit[0]:
            if Path(f"profile/{message.author.id}").exists() == False:
                os.makedirs(f"profile/{message.author.id}")
                with open(f'profile/{message.author.id}/user', 'w') as f:
                    f.write(str(message.author.id))
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write("0")
                if my_file.exists():
                    await message.channel.send("seu ^w^ pewfiw ^-^ foi cwiado?!! Mande o comando nyovamente. *sweats*")
                else:
                    await message.channel.send("Seu perfil foi criado! Mande o comando novamente.")
            else:
                pass
            if Path(f"profile/{message.author.id}/duelos").exists() == False:
                with open(f'profile/{message.author.id}/duelos', 'w') as f:
                    f.write("0")
            else:
                if Path(f"profile/{message.author.id}/duelos").exists() == False:
                    with open(f'profile/{message.author.id}/duelos', 'w') as f:
                        f.write("0")
            roleta_random = [100, 10, 50, 200, 0, 100, 10, 10, 400, 400, 200, 200, 100, 100, 10, 200, 0, 0, 400]
                
            resultado = random.choice(roleta_random)

            if username in roleta_cooldown:
                if my_file.exists():
                    await message.channel.send("opaaa ÚwÚ pewa *cries* w-wá, você já pegou seu giwo. Espewe m-mais um tempo pawa pegaw nyovamente. *sweats* (Dica UWU: d$comprar)")
                else:
                    await message.channel.send("Opaaa pera lá, você já pegou seu giro. Espere mais um tempo para pegar novamente. (Dica: d$comprar)")

            else:
                if my_file.exists():
                    await message.channel.send(f"O wesuwtado da s-s-sua w-woweta foi... {resultado} PadowaCoins?!?1")
                else:
                    await message.channel.send(f"O resultado da sua roleta foi... {resultado} PadolaCoins!")
                current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                new_coins = int(current_coins)+resultado
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write(str(new_coins))
                roleta_cooldown.append(username)
                await asyncio.sleep(2000)
                roleta_cooldown.remove(username)

            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass    

        else:
            pass


    elif "d$investir" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$investir" == msgsplit[0]:
            if Path(f"profile/{message.author.id}").exists() == False:
                os.makedirs(f"profile/{message.author.id}")
                with open(f'profile/{message.author.id}/user', 'w') as f:
                    f.write(str(message.author.id))
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write("0")
            else:
                pass
            if Path(f"profile/{message.author.id}/duelos").exists() == False:
                with open(f'profile/{message.author.id}/duelos', 'w') as f:
                    f.write("0")
            else:
                if Path(f"profile/{message.author.id}/duelos").exists() == False:
                    with open(f'profile/{message.author.id}/duelos', 'w') as f:
                        f.write("0")
            investir_random = ["win", "lose", "lose", "lose", "win", "lose", "win", "lose"]
                
            resultado = random.choice(investir_random)

            if 1 == 2:
                if my_file.exists():
                    await message.channel.send("opaaa ÚwÚ pewa *cries* w-wá, você já investiu. *sees bulge* Espewe m-mais um tempo pawa investiw nyovamente. *sweats* (Dica: d$comprar)")
                else:
                    await message.channel.send("Opaaa pera lá, você já investiu. Espere mais um tempo para investir novamente. (Dica: d$comprar)")

            else:
                if int(msgsplit[1]) > int(open(f"profile/{message.author.id}/coins", "r+").read()):
                    if my_file.exists():
                        await message.channel.send("Você não tem fundos o s-suficiente pwa i-investiw. (Dica UWU: d$comprar)")
                    else:
                        await message.channel.send("Você não tem fundos o suficiente pra investir. (Dica: d$comprar)")
                else:
                    if len(msgsplit) < 2:
                        if my_file.exists():
                            await message.channel.send("opa ÚwÚ patwão, escweve diweito. O comando é 'd$doawr <quantidade>'")
                        else:
                            await message.channel.send("Opa patrão, escreve direito. O comando é 'd$investir <quantidade>'")
                    else:
                        if resultado == "win":
                            win_thing = [4, 10, 2, 2, 4, 5]
                            win_thing = random.choice(win_thing)
                            if my_file.exists():
                                await message.channel.send(f"Você wucwou {str(win_thing).replace('0.', '')}%! seu ^w^ wucwo totaw :3 foi {int(int(msgsplit[1])*win_thing / 100)} PadowaCoins!")
                            else:
                                await message.channel.send(f"Você lucrou {str(win_thing).replace('0.', '')}%! Seu lucro total foi {int(int(msgsplit[1])*win_thing / 100)} PadolaCoins!")
                            current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                            new_coins = int(round(int(msgsplit[1])*win_thing / 100))
                            new_coins = int(int(current_coins)+new_coins)
                            with open(f'profile/{message.author.id}/coins', 'w') as f:
                                f.write(str(new_coins))
    #                        investir_cooldown.append(username)
    #                        await asyncio.sleep(2000)
    #                        investir_cooldown.remove(username)
                        else:
                            win_thing = [4, 10, 2, 2, 4, 5]
                            win_thing = random.choice(win_thing)
                            if my_file.exists():
                                await message.channel.send(f"Você pewdeu {str(win_thing).replace('0.', '')}%! Suas pewdas totais fowam *twerks* {int(round(int(msgsplit[1])*win_thing / 100))} PadowaCoins... Boa sowte nya pwóxima...")
                            else:
                                await message.channel.send(f"Você perdeu {str(win_thing).replace('0.', '')}%! Suas perdas totais foram {int(round(int(msgsplit[1])*win_thing / 100))} PadolaCoins... Boa sorte na próxima...")
                            current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                            new_coins = int(round(int(msgsplit[1])*win_thing / 100))
                            new_coins = int(int(current_coins)-new_coins)
                            with open(f'profile/{message.author.id}/coins', 'w') as f:
                                f.write(str(new_coins))
    #                        investir_cooldown.append(username)
    #                        await asyncio.sleep(2000)
    #                        investir_cooldown.remove(username)


                    if username not in bought_one:
                        users_on_cooldown.append(username)
                        await asyncio.sleep(cooldown_command) # time in seconds
                        users_on_cooldown.remove(username)
                    else:
                        pass


        else:
            pass


    elif "d$lojinha" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$lojinha" == msgsplit[0]:
            if Path(f"profile/{message.author.id}").exists() == False:
                os.makedirs(f"profile/{message.author.id}")
                with open(f'profile/{message.author.id}/user', 'w') as f:
                    f.write(str(message.author.id))
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write("0")
                if my_file.exists():
                    await message.channel.send("seu ^w^ pewfiw ^-^ foi cwiado?!! Mande o comando nyovamente. *sweats*")
                else:
                    await message.channel.send("Seu perfil foi criado! Mande o comando novamente.")
            else:
                pass
            if Path(f"profile/{message.author.id}/duelos").exists() == False:
                with open(f'profile/{message.author.id}/duelos', 'w') as f:
                    f.write("0")
            else:
                pass
            if len(msgsplit) == 2:
                if msgsplit[1] == "1":
                    current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                    if int(current_coins) >= 1000:
                        new_coins = int(current_coins)-1000
                        with open(f'profile/{message.author.id}/coins', 'w') as f:
                            f.write(str(new_coins))
                        if my_file.exists():
                            await message.channel.send("Você compwou o benyefício 1.")
                        else:
                            await message.channel.send("Você comprou o benefício 1.")
                        bought_one.append(username)
                        await asyncio.sleep(2500) # time in seconds
                        bought_one.remove(username)
                    else:
                        if my_file.exists() == False:
                            await message.channel.send("Ah mais que triste. Você não tem PadolaCoins o suficiente. (Dica: d$comprar)")
                        else:
                            await message.channel.send("A-Ah, m-mais que twiste!!11 você não tem PadowaCoins o suficiente. *looks at you* (Dica UWU: d$comprar)")
                elif msgsplit[1] == "2":
                    current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                    if int(current_coins) >= 500:
                        new_coins = int(current_coins)-500
                        with open(f'profile/{message.author.id}/coins', 'w') as f:
                            f.write(str(new_coins))
                        if my_file.exists():
                            await message.channel.send("Você compwou o benyefício 2.")
                        else:
                            await message.channel.send("Você comprou o benefício 2.")
                        bought_two.append(username)
                        await asyncio.sleep(2500) # time in seconds
                        bought_two.remove(username)
                    else:
                        if my_file.exists():
                            await message.channel.send("Ah mais que triste. Você não tem PadolaCoins o suficiente. (Dica: d$comprar)")
                        else:
                            await message.channel.send("A-Ah, m-mais que twiste!!11 você não tem PadowaCoins o suficiente. *looks at you* (Dica UWU: d$comprar)")
                elif msgsplit[1] == "3":
                    current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                    if int(current_coins) >= 100000:
                        if my_file.exists():
                            await message.channel.send("Você compwou o benyefício 3. Wesponda a essa mensagem como você quew o comando.")
                        else:
                            await message.channel.send("Você comprou o benefício 3. Responda a essa mensagem como você quer o comando.")

                        def sus(m):
                            return m.author == message.author

                        try:
                            msg = await client.wait_for('message', check=sus)
                        except asyncio.TimeoutError:
                            await message.channel.send('Compra cancelada. Tente novamente.')
                        else:
                            await message.channel.send('Comando registrado.')
                            new_coins = int(current_coins)-100000
                            with open(f'profile/{message.author.id}/coins', 'w') as f:
                                f.write(str(new_coins))
                            admmasterblaster = await client.fetch_user("727194765610713138")
                            await admmasterblaster.send(f"""Atenção Adm, o {username} comprou um comando personalizado. Ele quer desse jeito: "{msg.content}" """)
                    else:
                        if my_file.exists():
                            await message.channel.send("Ah mais que triste. Você não tem PadolaCoins o suficiente. (Dica: d$comprar)")
                        else:
                            await message.channel.send("A-Ah, m-mais que twiste!!11 você não tem PadowaCoins o suficiente. *looks at you* (Dica UWU: d$comprar)")
                elif msgsplit[1] == "4":
                    current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                    if int(current_coins) >= 1500:
                        new_coins = int(current_coins)-1500
                        with open(f'profile/{message.author.id}/coins', 'w') as f:
                            f.write(str(new_coins))
                        if my_file.exists():
                            await message.channel.send("Você compwou o benyefício 4.")
                        else:
                            await message.channel.send("Você comprou o benefício 4.")
                        bought_four.append(username)
                        await asyncio.sleep(2500) # time in seconds
                        bought_four.remove(username)
                    else:
                        if my_file.exists():
                            await message.channel.send("Ah mais que triste. Você não tem PadolaCoins o suficiente. (Dica: d$comprar)")
                        else:
                            await message.channel.send("A-Ah, m-mais que twiste!!11 você não tem PadowaCoins o suficiente. *looks at you* (Dica UWU: d$comprar)")

            else:
                if my_file.exists():
                    embed = discord.Embed(title="wojinha *huggles tightly* do Denji",
                                          description="compwe >w< benyefícios :3 com seus Padowa *walks away* Coins aqui?!?! - Mande o comando 'd$lojinha <numero>' pawa compwaw!!11 *screeches*",
                                          colour=0x00b0f4)

                    embed.add_field(name="I - Speciaw Coowdown",
                                    value="Não seja afetado pewo coowdown pow 40 m-minyutos - 1000 PadowaCoins",
                                    inline=False)
                    embed.add_field(name="II - Rinha e d-duelo Coowdown Wemuvw UWU",
                                    value="Não seja afetado pewo coowdown das apostas e d-duelo pow 40 m-minyutos - 500 PadowaCoins",
                                    inline=False)
                    embed.add_field(name="III - C-Comando customizado",
                                    value="cowoque :3 um comando customizado com seu usewnyame ;;w;; - 100000 PadowaCoins",
                                    inline=False)
                    embed.add_field(name="IV - Sonyegaw impostos",
                                    value="Seja um fowa da wei e pague zewo impostos nya s-suas twansfewencias pow 40 m-minyutos - 1500 PadowaCoins",
                                    inline=False)

                    embed.set_footer(text="Denji-kun Bot",
                                     icon_url=client.user.display_avatar)
                else:
                    embed = discord.Embed(title="Lojinha do Denji",
                                          description="Compre benefícios com seus Padola Coins aqui! - Mande o comando '$lojinha <numero>' para comprar!",
                                          colour=0x00b0f4)

                    embed.add_field(name="I - Special Cooldown",
                                    value="Não seja afetado pelo cooldown por 40 minutos - 1000 PadolaCoins",
                                    inline=False)
                    embed.add_field(name="II - Rinha e Duelo Cooldown Remover",
                                    value="Não seja afetado pelo cooldown das apostas e duelos por 40 minutos - 500 PadolaCoins",
                                    inline=False)
                    embed.add_field(name="III - Comando customizado",
                                    value="Coloque um comando customizado com seu username - 100000 PadolaCoins",
                                    inline=False)
                    embed.add_field(name="IV - Sonegar impostos",
                                    value="Seja um fora da lei e pague zero impostos na suas transferencias por 40 minutos - 1500 PadolaCoins",
                                    inline=False)

                    embed.set_footer(text="Denji-kun Bot",
                                     icon_url=client.user.display_avatar)

                await message.channel.send(embed=embed)

        else:
            pass

    elif "d$profile" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$profile" == msgsplit[0]:
            if len(msgsplit) >= 2:
                a = msgsplit[1]
                a = a.replace("<","")
                a = a.replace(">","")
                user_sent = a.replace("@","")
                if client.get_user(int(user_sent)) is not None: # find ID by right clicking on a user and choosing "copy id" at the bottom
                    if Path(f"profile/{user_sent}").exists() == False:
                        os.makedirs(f"profile/{user_sent}")
                        with open(f'profile/{user_sent}/user', 'w') as f:
                            f.write(str(user_sent))
                        with open(f'profile/{user_sent}/coins', 'w') as f:
                            f.write("0")
                    else:
                        pass
                    if Path(f"profile/{user_sent}/duelos").exists() == False:
                        with open(f'profile/{user_sent}/duelos', 'w') as f:
                            f.write("0")
                    else:
                         pass
                    if Path(f"profile/{user_sent}/duelos_vencidos").exists() == False:
                        with open(f'profile/{user_sent}/duelos_vencidos', 'w') as f:
                            f.write("0")
                    else:
                        pass
                    if Path(f"profile/{user_sent}/duelos_perdidos").exists() == False:
                        with open(f'profile/{user_sent}/duelos_perdidos', 'w') as f:
                            f.write("0")
                    else:
                        pass
                    the_user = client.get_user(int(user_sent))
                    embed = discord.Embed(title=f"Perfil do {client.get_user(int(user_sent))}",
                          description="*Use d$daily e d$roleta para ganhar PadolaCoins!*",
                          colour=0x00b0f4)

                    embed.add_field(name="Padola Coins",
                                    value=f"""{open(f"profile/{user_sent}/coins", "r+").read()}""",
                                    inline=False)
                    embed.add_field(name="Apostas vencidas",
                                    value=f"""{open(f"profile/{user_sent}/duelos", "r+").read()}""",
                                    inline=False)
                    embed.add_field(name="Duelos Mortalmente Mortais",
                                    value=f"""Ganhou {open(f"profile/{user_sent}/duelos_vencidos", "r+").read()} - Perdeu {open(f"profile/{user_sent}/duelos_perdidos", "r+").read()}""",
                                    inline=False)

                    embed.set_thumbnail(url=the_user.display_avatar)

                    embed.set_footer(text="Denji-kun Bot",
                             icon_url=client.user.display_avatar)
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send(f"Tem certeza de que esse user existe?")

            else:
                if Path(f"profile/{message.author.id}").exists() == False:
                    os.makedirs(f"profile/{message.author.id}")
                    with open(f'profile/{message.author.id}/user', 'w') as f:
                        f.write(str(message.author.id))
                    with open(f'profile/{message.author.id}/coins', 'w') as f:
                        f.write("0")
                    if Path(f"profile/{message.author.id}/duelos").exists() == False:
                        with open(f'profile/{message.author.id}/duelos', 'w') as f:
                            f.write("0")
                    else:
                        pass
                    if Path(f"profile/{message.author.id}/duelos_vencidos").exists() == False:
                        with open(f'profile/{message.author.id}/duelos_vencidos', 'w') as f:
                            f.write("0")
                    else:
                        pass
                    if my_file.exists():
                        await message.channel.send("seu ^w^ pewfiw ^-^ foi cwiado. ^w^ Mande o comando nyovamente. *sweats*")
                    else:
                        await message.channel.send("Seu perfil foi criado. Mande o comando novamente.")
                else:
                    if Path(f"profile/{message.author.id}/duelos").exists() == False:
                        with open(f'profile/{message.author.id}/duelos', 'w') as f:
                            f.write("0")
                    else:
                        pass
                    if Path(f"profile/{message.author.id}/duelos_vencidos").exists() == False:
                        with open(f'profile/{message.author.id}/duelos_vencidos', 'w') as f:
                            f.write("0")
                    else:
                        pass
                    if Path(f"profile/{message.author.id}/duelos_perdidos").exists() == False:
                        with open(f'profile/{message.author.id}/duelos_perdidos', 'w') as f:
                            f.write("0")
                    else:
                        pass
                    embed = discord.Embed(title=f"Perfil do {username}",
                          description="*Use d$daily e d$roleta para ganhar PadolaCoins!*",
                          colour=0x00b0f4)

                    embed.add_field(name="Padola Coins",
                                    value=f"""{open(f"profile/{message.author.id}/coins", "r+").read()}""",
                                    inline=False)
                    embed.add_field(name="Apostas vencidas",
                                    value=f"""{open(f"profile/{message.author.id}/duelos", "r+").read()}""",
                                    inline=False)
                    embed.add_field(name="Duelos Mortalmente Mortais",
                                    value=f"""Ganhou {open(f"profile/{message.author.id}/duelos_vencidos", "r+").read()} - Perdeu {open(f"profile/{message.author.id}/duelos_perdidos", "r+").read()}""",
                                    inline=False)

                    embed.set_thumbnail(url=message.author.display_avatar)

                    embed.set_footer(text="Denji-kun Bot",
                             icon_url=client.user.display_avatar)

                await message.channel.send(embed=embed)
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass

    elif "d$daily" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$daily" == msgsplit[0]:
            if Path(f"profile/{message.author.id}").exists() == False:
                os.makedirs(f"profile/{message.author.id}")
                with open(f'profile/{message.author.id}/user', 'w') as f:
                    f.write(str(message.author.id))
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write("0")
                if Path(f"profile/{message.author.id}/duelos").exists() == False:
                    with open(f'profile/{message.author.id}/duelos', 'w') as f:
                        f.write("0")
                else:
                    pass
                if my_file.exists():
                    await message.channel.send("seu ^w^ pewfiw ^-^ foi cwiado. ^w^ Mande o comando nyovamente. *sweats*")
                else:
                    await message.channel.send("Seu perfil foi criado. Mande o comando novamente.")
            else:
                pass
            if Path(f"profile/{message.author.id}/duelos").exists() == False:
                with open(f'profile/{message.author.id}/duelos', 'w') as f:
                    f.write("0")
            else:
                pass

            if username in daily_cooldown:
                if my_file.exists():
                    await message.channel.send("opaaa ÚwÚ pewa *cries* w-wá, você já pegou seus Denji Coins diáwios. Espewe m-mais um tempo pawa pegaw nyovamente. *sweats* (Dica UWU: d$comprar)")
                else:
                    await message.channel.send("Opaaa pera lá, você já pegou seus Denji Coins diários. Espere mais um tempo para pegar novamente. (Dica: d$comprar)")

            else:
                current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                new_coins = int(current_coins)+100
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write(str(new_coins))
                if my_file.exists():
                    await message.channel.send(f"Você ganhou 100 PadowaCoins?!?1")
                else:
                    await message.channel.send(f"Você ganhou 100 PadolaCoins!")
                daily_cooldown.append(username)
                await asyncio.sleep(2500)
                daily_cooldown.remove(username)

            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass

#    if user_message.lower() == "jojo" or user_message.lower() == "yoshikage kira":
#        if my_file.exists():
#            await message.channel.send("""meu *screams* nyome é Yoshikage Kiwa. ^-^ Tenho 33 anyos. Minha casa fica nya pawte OwO nyowdeste de Mowioh, *runs away* onde *looks at you* todas ;;w;; as casas estão, e eu não sou :3 casado. eu *huggles tightly* twabawho *boops your nose* como funcionáwio das wojas de depawtamentos *screams* Kame Yu *screeches* e chego em casa todos os dias às oito da nyoite, nyo máximo. *sees bulge* eu *huggles tightly* não fumo, mas ocasionyawmente bebo. Estou nya c-cama às 23 :3 howas e me cewtifico de tew oito howas de sonyo, não impowta o que aconteça. ^w^ Depois de tomaw um copo de weite mownyo e fazew c-c-cewca de vinte m-minyutos de awongamentos antes de iw pawa a cama, gewawmente não tenho pwobwemas pawa dowmiw até de manhã. Assim como um bebê, eu acowdo sem nyenhum cansaço ou estwesse pewa *cries* manhã. Foi-me dito que não houve pwobwemas nyo meu úwtimo check-up. Estou t-t-tentando expwicaw que sou :3 uma pessoa que deseja vivew uma vida ^w^ muito twanquiwa. eu *huggles tightly* cuido pawa não me incomodaw com inyimigos, como ganhaw e pewdew, *walks away* isso me fawia pewdew o sonyo à nyoite. É assim que eu wido com a sociedade e sei que é isso que me twaz fewicidade. E-Embowa, se eu fosse wutaw, não pewdewia pawa nyinguém.""") 
#        else:
#            await message.channel.send("""Meu nome é Yoshikage Kira. Tenho 33 anos. Minha casa fica na parte nordeste de Morioh, onde todas as casas estão, e eu não sou casado. Eu trabalho como funcionário das lojas de departamentos Kame Yu e chego em casa todos os dias às oito da noite, no máximo. Eu não fumo, mas ocasionalmente bebo. Estou na cama às 23 horas e me certifico de ter oito horas de sono, não importa o que aconteça. Depois de tomar um copo de leite morno e fazer cerca de vinte minutos de alongamentos antes de ir para a cama, geralmente não tenho problemas para dormir até de manhã. Assim como um bebê, eu acordo sem nenhum cansaço ou estresse pela manhã. Foi-me dito que não houve problemas no meu último check-up. Estou tentando explicar que sou uma pessoa que deseja viver uma vida muito tranquila. Eu cuido para não me incomodar com inimigos, como ganhar e perder, isso me faria perder o sono à noite. É assim que eu lido com a sociedade e sei que é isso que me traz felicidade. Embora, se eu fosse lutar, não perderia para ninguém.""")
#        return
#    elif user_message.lower() == "eu vim fazer um anuncio":
#        if my_file.exists(): 
#            await message.channel.send("""S-S-Shadow o ouwiço é um fiwha da puta do cawawho, >w< ewe mijou nya powwa da minha esposa, isso mesmo, ewe pegou a powwa do pinto e-espinhoso dewe e mijou nya powwa da minha esposa *screams* e disse que o pau *screams* dewe ewa dessa tamanho x3 e eu disse "Cwedo, que nyojo" então estou fazendo um exposed nyo meu twittew.com. S-S-Shadow o ouwiço, você tem um pau *screams* pequenyo, que é do tamanho x3 desta UwU n-nyoz só *cries* que muito menyow, e adivinha, owha o tamanho x3 do meu piwocão. Isso mesmo bebê, pontas *screams* awtas, sem pewos, sem espinhos, owha só, pawecem 2 bowas e 1 towpedo. Ewe fodeu a minha esposa, então adivinhem, eu vou fodew a tewwa, isso mesmo, isso que você ganha, meu supew *cries* w-w-wasew de mijo. Exceto que eu não vou mijaw nya tewwa, eu vou mijaw nya wua, OwO você gostou *runs away* disto Wuwa, *blushes* eu mijei nya wua, OwO faz *cries* o W agowa. v-vocês tem 23 :3 howas antes que os meus pewdigotos *twerks* de mijo atinjam *walks away* a Tewwa. Agowa saiam da powwa da minha fwente, antes que eu mije em v-vocês também""") 
#        else:
#            await message.channel.send("""Shadow o ouriço é um filha da puta do caralho, ele mijou na porra da minha esposa, isso mesmo, ele pegou a porra do pinto espinhoso dele e mijou na porra da minha esposa e disse que o pau dele era dessa tamanho e eu disse "Credo, que nojo" então estou fazendo um exposed no meu twitter.com. Shadow o ouriço, você tem um pau pequeno, que é do tamanho desta noz só que muito menor, e adivinha, olha o tamanho do meu pirocão. Isso mesmo bebê, pontas altas, sem pelos, sem espinhos, olha só, parecem 2 bolas e 1 torpedo. Ele fodeu a minha esposa, então adivinhem, eu vou foder a terra, isso mesmo, isso que você ganha, meu super laser de mijo. Exceto que eu não vou mijar na terra, eu vou mijar na lua, você gostou disto Lula, eu mijei na lua, faz o L agora. vocês tem 23 horas antes que os meus perdigotos de mijo atinjam a Terra. Agora saiam da porra da minha frente, antes que eu mije em vocês também""")            
    elif "peitos" in user_message.lower() and not username in users_on_cooldown:
        if my_file.exists(): 
            jokes = ["PEITOS?!?! aONDE?!?1 *sweats* PEITOS PEITOS PEITOS PEITOS AAAAAAAAAAAAAA", "São >w< tão macios... quewia pegaw em uns peitos...", "EU QUEWO PEITOOOOOOOOOOS", "Sou o maiow fã de peitos do mundo"]
        else:
            jokes = ["PEITOS???? AONDE?????? PEITOS PEITOS PEITOS PEITOS AAAAAAAAAAAAAA", "São tão macios... queria pegar em uns peitos...", "EU QUERO PEITOOOOOOOOOOS", "Sou o maior fã de peitos do mundo"]
        await message.channel.send(random.choice(jokes))
        if username not in bought_one:
            users_on_cooldown.append(username)
            await asyncio.sleep(cooldown_command) # time in seconds
            users_on_cooldown.remove(username)
        else:
            pass
    elif "calcinha" in user_message.lower() and not username in users_on_cooldown:
        if my_file.exists(): 
            jokes = "Quewia tanto OwO tew uma..."
        else:
            jokes = "Queria tanto ter uma..."
        await message.channel.send(jokes)
        if username not in bought_one:
            users_on_cooldown.append(username)
            await asyncio.sleep(cooldown_command) # time in seconds
            users_on_cooldown.remove(username)
        else:
            pass
#    elif "gojo" in user_message.lower() and not username in users_on_cooldown:
#        if "d$battle" in user_message.lower():
#            pass
#        else: 
#            jokes = "https://media.discordapp.net/attachments/767851776212336642/1169032788557697244/have-a-break-have-a-kit-kat-v0-gyreqrrlk6wb1.png?ex=6553eda0&is=654178a0&hm=4fd1d5a7f177aff730ea9104d2b72e14a9339483f5b482dce0ffdb3b88463046&=&width=344&height=459"
#            await message.channel.send(jokes, reference=message)
#        if username not in bought_one:
#            users_on_cooldown.append(username)
#            await asyncio.sleep(cooldown_command) # time in seconds
#            users_on_cooldown.remove(username)
#        else:
#            pass
    elif "d$lana" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$lana" == msgsplit[0]:
            await message.channel.send("https://tenor.com/view/himeno-himmy-himeno-chainsaw-man-banging-headbanging-gif-6931555360158583987")
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass
    elif "d$skyte" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$skyte" == msgsplit[0]:
            await message.channel.send("https://tenor.com/view/ronaldo-win-ronaldo-award-ronaldo-gif-24123234")
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass
    elif "d$kaishl" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$kaishl" == msgsplit[0]:
            await message.channel.send("https://tenor.com/view/bom-dia-valtatui-valtatui-bom-dia-gif-25587386")
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass
    elif "d$dani2" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$dani2" == msgsplit[0]:
            await message.channel.send("https://tenor.com/view/choso-choso-jjk-choso-jujutsu-kaisen-choso-anime-jujutsu-kaisen-gif-10037971888755283102")
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass
    elif "d$dani" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$dani" == msgsplit[0]:
            await message.channel.send("https://tenor.com/view/gojo-gojo-satoru-dancing-jjk-jujutsu-kaisen-gif-25819377")
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass
    elif "d$suro" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$suro" == msgsplit[0]:
            await message.channel.send("https://media.discordapp.net/attachments/804443142879182871/941984752603398154/image0-156.gif")
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass
    elif "d$reze69" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$reze69" == msgsplit[0]:
            await message.channel.send("https://tenor.com/view/rolando-ronaldo-cristiano-gif-26255427")
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass
    elif "d$fanho2" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$fanho2" == msgsplit[0]:
            await message.channel.send("https://cdn.discordapp.com/attachments/1164692508668862515/1171207341488750714/image0.gif?ex=655bd6d6&is=654961d6&hm=e139f0b8fefedde2b29d3a57212c3111a23db7cfe529ae4e931aac42d11349bb&")
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass
    elif "d$fanho" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$fanho" == msgsplit[0]:
            await message.channel.send("https://tenor.com/view/makima-bean-beans-chainsaw-man-gif-25992235")
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass

    elif "d$comprar" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$comprar" == msgsplit[0]:
            thing = """Ficou sem dinheiro apostando com o ADM? Agora você pode realizar a compra de PadolaCoins!
Comprar PadolaCoins é um jeito de ajudar o bot a continuar online, ajuda o criador a pagar as contas, e principalmente,
nos ajuda a continuar desenvolvendo!

Para comprar, chame o criador do DenjiBot (@jocadbz) na DM. O valor é negociável."""
            await message.channel.send(thing)
            await message.channel.send("https://tenor.com/view/mlem-silly-goofy-cat-silly-cat-goofy-gif-27564930")
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass
    elif "d$jogo" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        rand1 = [0, 1, 2, 3, 4, 5]
        rand2 = [0, 1, 2, 3, 4, 5]
        if "d$jogo" == msgsplit[0]:
            if my_file.exists():
                jokes = f"O wesuwtado da pawtida de {msgsplit[1]} x {msgsplit[2]} vai sew {random.choice(rand1)} x {random.choice(rand1)} UWU"
            else:
                jokes = f"O resultado da partida de {msgsplit[1]} x {msgsplit[2]} vai ser {random.choice(rand1)} x {random.choice(rand1)}"
            await message.channel.send(jokes)
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass
    elif "d$ppt" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$ppt" == msgsplit[0]:
            if my_file.exists():
                jokes = f"Cawo/Cawa {msgsplit[1]}, o {username} gostawia de d-decwawaw seus sentimentos a você."
            else:
                jokes = f"Caro/Cara {msgsplit[1]}, o {username} gostaria de declarar seus sentimentos a você."
            await message.channel.send(jokes)
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass
    elif "d$sabio" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$sabio" == msgsplit[0]:
            if my_file.exists():
                jokes = ["SIM, C-C-COM TODA CEWTEZA", "Sim, >w< com cewteza.", "Sim.", "Pwovavewmente.", "Não sei dizew.", "Pwovavewmente não.", "Não.", 'Com c-cewteza n-não.', "NÃO, C-C-COM TODA CEWTEZA NÃO", "O Padowa é-é quem decide UWU"]
            else:
                jokes = ["SIM, COM TODA CERTEZA", "Sim, com certeza.", "Sim.", "Provavelmente.", "Não sei dizer.", "Provavelmente não.", "Não.", 'Com certeza não.', "NÃO, COM TODA CERTEZA NÃO", "O Padola decide."]
            await message.channel.send(random.choice(jokes))
            if username not in bought_one:
                users_on_cooldown.append(username)
                await asyncio.sleep(cooldown_command) # time in seconds
                users_on_cooldown.remove(username)
            else:
                pass
        else:
            pass

    elif "d$cancelamento" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        rand1 = [0, 1]
        if "d$cancelamento" == msgsplit[0]:
            if my_file.exists():
                motivos = ["sew ;;w;; atwaente d-demais", "tew chawme d-demais", "sew ;;w;; uma pessoa howwívew", "sew ;;w;; uma gwande gostosa", "sew ;;w;; boy wixo", "sew ;;w;; comunyista", "debochaw *blushes* demais sew intewigente d-demais", "sew ;;w;; p-padwãozinho", "pediw ^w^ muito biscoito", "sew ;;w;; cownyo sew uma dewícia", "sew ;;w;; gado d-demais", "não sew nyinguém", "sew ;;w;; posew", "sew ;;w;; insupowtávew", "sew ;;w;; insensívew", "não fazew nyada", "sew ;;w;; twouxa", "se atwasaw", "sempwe sew impaciente d-demais", "tew viwado o Cowonga", "sew ;;w;; BV", "tew muita pweguiça", "sew ;;w;; inútiw", "sew ;;w;; inyadimpwente >w< nyo S-Sewasa", "contaw muita piada wuim", "pwocwastinyaw d-demais", "pow se considewaw incancewávew"]
                await message.channel.send(f"{message.author} foi cancewado pow {random.choice(motivos)}")
            else:
                motivos = ["ser atraente demais", "ter charme demais", "ser uma pessoa horrível", "ser uma grande gostosa", "ser boy lixo", "ser comunista", "debochar demais ser inteligente demais", "ser padrãozinho", "pedir muito biscoito", "ser corno ser uma delícia", "ser gado demais", "não ser ninguém", "ser poser", "ser insuportável", "ser insensível", "não fazer nada", "ser trouxa", "se atrasar", "sempre ser impaciente demais", "ter virado o Coronga", "ser BV", "ter muita preguiça", "ser inútil", "ser inadimplente no Serasa", "contar muita piada ruim", "procrastinar demais", "por se considerar incancelável"]
                await message.channel.send(f"{message.author} foi cancelado por {random.choice(motivos)}")
        else:
            pass

    elif "d$battle" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        rand1 = [0, 1]
        if "d$battle" == msgsplit[0]:
            if my_file.exists():
                if random.choice(rand1) == 0:
                    comeco = ["Foi pow pouco, mas ", "E com gwande fowga ", "Foi uma wuta justa, mas "]
                    fim = ["esmagando seu c-cwânyio", "abwindo um buwaco em seu peito.", "decepando s-s-sua cabeça."]
                    jokes = f"{random.choice(comeco)}{msgsplit[1]} ganhow a l-luta contwa {msgsplit[2]} {random.choice(fim)}"
                    await message.channel.send(jokes)
                    if username not in bought_one:
                       users_on_cooldown.append(username)
                       await asyncio.sleep(cooldown_command) # time in seconds
                       users_on_cooldown.remove(username)
                    else:
                        pass
                else:
                    comeco = ["Foi pow pouco, mas ", "E com gwande fowga ", "Foi uma wuta justa, mas "]
                    fim = ["esmagando seu c-cwânyio", "abwindo um buwaco em seu peito.", "decepando s-s-sua cabeça.", "desintegwando seu cowpo.", "sewwando seu c-cowpo ao meio."]
                    jokes = f"{random.choice(comeco)}{msgsplit[2]} ganhow a l-luta contwa {msgsplit[1]} {random.choice(fim)}"
                    await message.channel.send(jokes)
                    if username not in bought_one:
                        users_on_cooldown.append(username)
                        await asyncio.sleep(cooldown_command) # time in seconds
                        users_on_cooldown.remove(username)
                    else:
                        pass
            else:
                if random.choice(rand1) == 0:
                    comeco = ["Foi por pouco, mas ", "E com grande folga, ", "Foi uma luta justa, mas "]
                    fim = ["esmagando seu crânio.", "abrindo um buraco em seu peito.", "decepando sua cabeça."]
                    jokes = f"{random.choice(comeco)}{msgsplit[1]} ganhou a luta contra {msgsplit[2]} {random.choice(fim)}"
                    await message.channel.send(jokes)
                    if username not in bought_one:
                        users_on_cooldown.append(username)
                        await asyncio.sleep(cooldown_command) # time in seconds
                        users_on_cooldown.remove(username)
                    else:
                        pass
                else:
                    comeco = ["Foi por pouco, mas ", "E com grande folga, ", "Foi uma luta justa, mas "]
                    fim = ["esmagando seu crânio.", "abrindo um buraco em seu peito.", "decepando sua cabeça.", "desintegrando seu corpo.", "serrando seu corpo ao meio."]
                    jokes = f"{random.choice(comeco)}{msgsplit[2]} ganhou a luta contra {msgsplit[1]} {random.choice(fim)}"
                    await message.channel.send(jokes)
                    if username not in bought_one:
                        users_on_cooldown.append(username)
                        await asyncio.sleep(cooldown_command) # time in seconds
                        users_on_cooldown.remove(username)
                    else:
                        pass    
        else:
            pass
    elif "d$uwu" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$uwu" == msgsplit[0]:
            if my_file.exists():
                os.remove("uwu")
                await message.channel.send("UwU mode deactivated!")
            else:
                with open('uwu', 'w') as f:
                    f.write('Create a new text file!') 
                await message.channel.send("UwU mode activated!")
        else:
            pass

client.run(token)