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

roleta_cooldown = []

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

    elif "d$roleta" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$roleta" == msgsplit[0]:
            if Path(f"profile/{message.author.id}").exists() == False:
                os.makedirs(f"profile/{message.author.id}")
                with open(f'profile/{message.author.id}/user', 'w') as f:
                    f.write(str(message.author.id))
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write("0")
                await message.channel.send("Seu perfil foi criado! Mande o comando novamente.")
            else:
                pass
            
            roleta_random = [100, 10, 50, 200, 0, 100, 10, 10, 400, 400, 200, 200, 100, 100, 10, 200, 0, 0, 400]
                
            resultado = random.choice(roleta_random)

            if username in roleta_cooldown:
                await message.channel.send("Opaaa pera lá, você já pegou seu giro. Espere mais um tempo para pegar novamente.")

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


    elif "d$lojinha" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$lojinha" == msgsplit[0]:
            if Path(f"profile/{message.author.id}").exists() == False:
                os.makedirs(f"profile/{message.author.id}")
                with open(f'profile/{message.author.id}/user', 'w') as f:
                    f.write(str(message.author.id))
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write("0")
                await message.channel.send("Seu perfil foi criado! Mande o comando novamente.")
            else:
                pass
            if len(msgsplit) == 2:
                if msgsplit[1] == "1":
                    current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                    if int(current_coins) >= 1000:
                        new_coins = int(current_coins)-1000
                        with open(f'profile/{message.author.id}/coins', 'w') as f:
                            f.write(str(new_coins))
                        await message.channel.send("Você comprou o benefício 1.")
                        bought_one.append(username)
                        await asyncio.sleep(2500) # time in seconds
                        bought_one.remove(username)
                    else:
                        await message.channel.send("Ah, mais que triste! você não tem PadolaCoins o suficiente.")

            else:
                embed = discord.Embed(title="Lojinha do Denji",
                                      description="Compre benefícios com seus Padola Coins aqui! - Mande o comando '$lojinha 1' para comprar!",
                                      colour=0x00b0f4)

                embed.add_field(name="I - Special Cooldown",
                                value="Não seja afetado pelo cooldown por 40 minutos - 1000 PadolaCoins",
                                inline=False)

                embed.set_footer(text="Denji-kun Bot",
                                 icon_url=client.user.display_avatar)

                await message.channel.send(embed=embed)

        else:
            pass

    elif "d$profile" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        if "d$profile" == msgsplit[0]:
            if Path(f"profile/{message.author.id}").exists() == False:
                os.makedirs(f"profile/{message.author.id}")
                with open(f'profile/{message.author.id}/user', 'w') as f:
                    f.write(str(message.author.id))
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write("0")
                await message.channel.send("Seu perfil foi criado. Mande o comando novamente.")
            else:
                embed = discord.Embed(title=f"Perfil do {username}",
                      colour=0x00b0f4)

                embed.add_field(name="Padola Coins",
                                value=f"""{open(f"profile/{message.author.id}/coins", "r+").read()}""",
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
                await message.channel.send("Your profile has been created! Try the command again.")
            else:
                pass

            if username in daily_cooldown:
                await message.channel.send("Opaaa pera lá, você já pegou seus Denji Coins diários. Espere mais um tempo para pegar novamente.")

            else:
                current_coins = open(f"profile/{message.author.id}/coins", "r+").read()
                new_coins = int(current_coins)+20
                with open(f'profile/{message.author.id}/coins', 'w') as f:
                    f.write(str(new_coins))
                await message.channel.send(f"Você ganhou 20 PadolaCoins!")
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
            jokes = "P-PEITOS!? aONDE?!?1 *sweats* PEITOS PEITOS PEITOS PEITOS AAAAAAAAAAAAAA UWU"
        else:
            jokes = "PEITOS???? AONDE?????? PEITOS PEITOS PEITOS PEITOS AAAAAAAAAAAAAA"
        await message.channel.send(jokes)
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
    elif "gojo" in user_message.lower() and not username in users_on_cooldown:
        if "d$battle" in user_message.lower():
            pass
        else: 
            jokes = "https://media.discordapp.net/attachments/767851776212336642/1169032788557697244/have-a-break-have-a-kit-kat-v0-gyreqrrlk6wb1.png?ex=6553eda0&is=654178a0&hm=4fd1d5a7f177aff730ea9104d2b72e14a9339483f5b482dce0ffdb3b88463046&=&width=344&height=459"
            await message.channel.send(jokes, reference=message)
        if username not in bought_one:
            users_on_cooldown.append(username)
            await asyncio.sleep(cooldown_command) # time in seconds
            users_on_cooldown.remove(username)
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
    elif "d$jogo" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        rand1 = [0, 1, 2, 3, 4, 5]
        rand2 = [0, 1, 2, 3, 4, 5]
        if "d$jogo" == msgsplit[0]:
            if my_file.exists():
                jokes = f"O wesuwtado da pawtida de {msgsplit[1]} x {msgsplit[2]} vai sew {random.choice(rand1)} x {random.choice(rand1)} UWU"
            else:
                jokes = f"O resultado da partida de {msgsplit[1]} x {msgsplit[2]} vai ser {random.choice(rand1)} x {random.choice(rand1)}"
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
                jokes = f"Cawo/Cawa {msgsplit[1]}, o {username} cowdiawmente te convida pwa fudew."
            else:
                jokes = f"Caro/Cara {msgsplit[1]}, o {username} cordialmente te convida pra fuder."
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
    elif "d$battle" in user_message.lower() and not username in users_on_cooldown:
        msgsplit = user_message.lower().split() 
        rand1 = [0, 1]
        if "d$battle" == msgsplit[0]:
            if "gojo" == msgsplit[1] or "gojo" == msgsplit[2]:
                if my_file.exists():
                    await message.channel.send("Não pwecisa nyem *starts twerking* de pwevisão, o gojo *screams* é buxa dms kkkkkkkkk")
                    if username not in bought_one:
                        users_on_cooldown.append(username)
                        await asyncio.sleep(cooldown_command) # time in seconds
                        users_on_cooldown.remove(username)
                    else:
                        pass
                else:
                    await message.channel.send("Não precisa nem de previsão, o gojo é buxa dms kkkkkkkkk")
                    if username not in bought_one:
                        users_on_cooldown.append(username)
                        await asyncio.sleep(cooldown_command) # time in seconds
                        users_on_cooldown.remove(username)
                    else:
                        pass
            else:
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