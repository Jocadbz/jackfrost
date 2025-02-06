# What

import random

cargos_uma_estrela = [
    {"nome": "Dalva", "ID": 1261155110067769445},
    {"nome": "Ausente", "ID": 1261155229684990043},
    {"nome": "Standless", "ID": 1261155188950175847},
    {"nome": "Buxa", "ID": 1261155266653851668},
    {"nome": "Vascaíno", "ID": 1261155249096495244},
    {"nome": "Newbie", "ID": 1261155060885487656},
    {"nome": "Piadista", "ID": 1261154976168673290},
    {"nome": "Anti-CLT", "ID": 1261154714104365106},
    {"nome": "Aspirante", "ID": 1261154765543309393},
    {"nome": "Coringando", "ID": 1261155007911170093},
    {"nome": "Safada", "ID": 1261154863556071539},
    {"nome": "Analfabeto", "ID": 1261154897949097984},
    {"nome": "Combatente", "ID": 1261154831800864838},
    {"nome": "Investidor", "ID": 1261154741698957415},
    {"nome": "Sonhador", "ID": 1261154881683722372},
    {"nome": "Rapariga", "ID": 1261154681212899430}
]

cargos_uma_estrela_m = [
    {"nome": "Subuxa", "ID": 1261155473911054376},
    {"nome": "Flamenguista", "ID": 1261155440130130041},
    {"nome": "Coringa", "ID": 1261155373549883543},
    {"nome": "Hey investidor", "ID": 1261155283367891137}
]

cargos_duas_estrelas = [
    {"nome": "Casca de bala", "ID": 1261157521054371981},
    {"nome": "Cavalo", "ID": 1261157302556164200},
    {"nome": "Jogador mobile", "ID": 1261157174806183977},
    {"nome": "Mercenário", "ID": 1261156914910462022},
    {"nome": "Habilidoso", "ID": 1261156983424290817},
    {"nome": "Gamer", "ID": 1261157460497141881},
    {"nome": "Osso duro de roer", "ID": 1261157252463857685},
    {"nome": "Duelista", "ID": 1261157009340764160},
    {"nome": "Ganancioso", "ID": 1261156945365303376},
    {"nome": "Otaku", "ID": 1261157475516813402},
    {"nome": "Maluco", "ID": 1261157145974411284},
    {"nome": "Jogador PC", "ID": 1261157225179910214},
    {"nome": "Fã do Ney", "ID": 1261157090735689758},
    {"nome": "Jogador console", "ID": 1261157201628893257},
    {"nome": "Leitor", "ID": 1261157490490478594}
]

cargos_duas_estrelas_m = [
    {"nome": "Fã do CR7", "ID": 1261157644522094634},
    {"nome": "Fã do Messi", "ID": 1261157569876070502},
    {"nome": "Jogador bactéria", "ID": 1261157676466049176}
]

cargos_tres_estrelas = [
    {"nome": "JoJofag", "ID": 1261160265592999996},
    {"nome": "Hétero", "ID": 1261160182277472379},
    {"nome": "Viado", "ID": 1261160213097218190},
    {"nome": "Programmer", "ID": 1261160307309543434},
    {"nome": "Urubu do PIX", "ID": 1261160053168279655},
    {"nome": "Sábio", "ID": 1261160137045971065},
    {"nome": "Femboy", "ID": 1261160158394847312},
    {"nome": "Consumidor", "ID": 1261159648145313812},
    {"nome": "Louco das ideia", "ID": 1261160028916678717},
    {"nome": "Nitendista", "ID": 1261158904113528883},
    {"nome": "Caixista", "ID": 1261158943325950065},
    {"nome": "Comediante", "ID": 1261159972067344464},
    {"nome": "Gado", "ID": 1261160109665419354},
    {"nome": "Presente", "ID": 1261159901036548199},
    {"nome": "Em aprendizado", "ID": 1261159997639757824},
    {"nome": "I am fan", "ID": 1261159948021399573},
    {"nome": "Sonysta", "ID": 1261159632810934383},
    {"nome": "Robloxiano", "ID": 1261160426373386363}
]

cargos_tres_estrelas_m = [
    {"nome": "Robloxiano", "ID": 1261160426373386363},
    {"nome": "Doutor Fran", "ID": 1261160455934709831},
    {"nome": "Don comédia", "ID": 1261160479221350400},
    {"nome": "I am atomic", "ID": 1261160342973845524}
]

cargos_quatro_estrelas = [
    {"nome": "Amostradinho", "ID": 1261163138137718844},
    {"nome": "Stand User", "ID": 1261163118709571645},
    {"nome": "Incansável", "ID": 1261163100350971945},
    {"nome": "Experiente", "ID": 1261162242292977686},
    {"nome": "Criminoso", "ID": 1261162224257470496},
    {"nome": "Luxuoso", "ID": 1261163033972183100},
    {"nome": "Ciborgue", "ID": 1261163066121261106},
    {"nome": "Caçador de recompensas", "ID": 1261162410010742885},
    {"nome": "Eu sabo", "ID": 1261162347955748905},
    {"nome": "Feiticeiro", "ID": 1261162373386080339},
    {"nome": "Sith", "ID": 1261162926023249990},
    {"nome": "Jedi", "ID": 1261162863712796692},
    {"nome": "Elfo", "ID": 1261162939293896704},
    {"nome": "Maldição", "ID": 1261162461164212265},
    {"nome": "Implacável", "ID": 1261162317819940906},
    {"nome": "Anão", "ID": 1261162978053591161}
]

cargos_quatro_estrelas_m = [
    {"nome": "Double Stand User", "ID": 1261163486353035365},
    {"nome": "Restrição celestial", "ID": 1261163426122563584},
    {"nome": "O mais forte", "ID": 1261163399006388234},
    {"nome": "Rei das maldições", "ID": 1261163301048418364},
    {"nome": "Mago patolino", "ID": 1261163246551961694}
]

cargos_cinco_estrelas = [
    {"nome": "Formiga quimera", "ID": 1261399702641967115},
    {"nome": "Bora Bill", "ID": 1261399845248303124},
    {"nome": "Pênis.com", "ID": 1261399814344675338},
    {"nome": "Marinheiro", "ID": 1261399758128550058},
    {"nome": "Revolucionário", "ID": 1261399785294794752},
    {"nome": "Xerecofóbico", "ID": 1261398895284588682},
    {"nome": "PIX caio17635gmail.com", "ID": 1261399161748586638},
    {"nome": "Cyberpunk", "ID": 1261399645775724595},
    {"nome": "Pirata", "ID": 1261399725463179427},
    {"nome": "Magnata", "ID": 1261399280749510707},
    {"nome": "Hunter", "ID": 1261399671343939626},
    {"nome": "Vampiro", "ID": 1261399526275547137},
    {"nome": "Skywalker", "ID": 1261399307823874159},
    {"nome": "Android", "ID": 1261399559511212184},
    {"nome": "Grande mago", "ID": 1261399607716352061},
    {"nome": "Cantor", "ID": 1261399485234544811},
    {"nome": "Baixista", "ID": 1261399435154423871},
    {"nome": "Guitarrista", "ID": 1261399344427565197},
    {"nome": "Baterista", "ID": 1261399364446851142}
]

cargos_cinco_estrelas_m = [
    {"nome": "Receba", "ID": 1261401098615259258},
    {"nome": "Nen-especialização", "ID": 1261400612206284880},
    {"nome": "Milionário", "ID": 1261400331531849859},
    {"nome": "Shichibukai", "ID": 1261400658830164010},
    {"nome": "Multi-instrumental", "ID": 1261399974898303037},
    {"nome": "Nen-aprimoramento", "ID": 1261400535794188412},
    {"nome": "Nen-manipulação", "ID": 1261400435051466774},
    {"nome": "Nen-transmutação", "ID": 1261400049519296572},
    {"nome": "Nen-emissão", "ID": 1261400386112065557},
    {"nome": "Pacifista", "ID": 1261401141997080678},
    {"nome": "Yonkou", "ID": 1261400721790599228},
    {"nome": "Iluminado", "ID": 1261400004841439254},
    {"nome": "Rei quimera", "ID": 1261403330274660553},
    {"nome": "Almirante", "ID": 1261400973159698533},
    {"nome": "Almirante de frota", "ID": 1261400994185740400},
    {"nome": "Flor preta", "ID": 1261401018638405752},
    {"nome": "Nen-conjuração", "ID": 1261400486272172072}
]

cargos_seis_estrelas = [
    {"nome": "EL MACHO", "ID": 1261404840282685552},
    {"nome": "Sr. Insônia", "ID": 1261404743289409536},
    {"nome": "Carlinhos", "ID": 1261403945503293560},
    {"nome": "Corvinal", "ID": 1261404130308653067},
    {"nome": "Lufa-lufa", "ID": 1261404041238548500},
    {"nome": "Papa-pintos", "ID": 1261403970438434918},
    {"nome": "Berseker", "ID": 1261403996426342490},
    {"nome": "Sonserina", "ID": 1261404170750267412},
    {"nome": "Grifinória", "ID": 1261404101183410217},
    {"nome": "Hollow", "ID": 1261404278375841874},
    {"nome": "Shinigami", "ID": 1261404313994133514},
    {"nome": "Quincy", "ID": 1261404194246758441},
    {"nome": "Arquimago", "ID": 1261404675471573064},
    {"nome": "Kessoku Band", "ID": 1261404436488650784},
    {"nome": "JoJo's", "ID": 1261404649479737464},
    {"nome": "Congelado", "ID": 1261404408575430758}
]

cargos_seis_estrelas_m = [
    {"nome": "Falcão Branco", "ID": 1261405098362277949},
    {"nome": "Gorousei", "ID": 1261404892065693827},
    {"nome": "Rei pirata", "ID": 1261404990979707020},
    {"nome": "Hogyoku", "ID": 1261405287672189110},
    {"nome": "Arrancar", "ID": 1261405226099802254},
    {"nome": "Sternritter", "ID": 1261405255900598273},
    {"nome": "Serafim", "ID": 1261405478273945681},
    {"nome": "Over Heaven", "ID": 1261405185566052353},
    {"nome": "Gala Seca", "ID": 1261405065667809402}
]

cargos_sete_estrelas = [
    {"nome": "THE TERMINATOR", "ID": 1261408325531209728},
    {"nome": "Bladerunner", "ID": 1261408299631247450},
    {"nome": "Boccher", "ID": 1261408403214041160},
    {"nome": "Revolucionista Generoso", "ID": 1261408044299059242},
    {"nome": "Hacker", "ID": 1261407991450566757},
    {"nome": "Pró CLT", "ID": 1261407950648639529},
    {"nome": "Filhos de R1ck", "ID": 1261408431777124484},
    {"nome": "juju", "ID": 1261408360444596264},
    {"nome": "Fanhista", "ID": 1261408021507084289},
    {"nome": "End Game", "ID": 1261408193053986908}
]

cargos_sete_estrelas_m = [
    {"nome": "Basilisco de Roko", "ID": 1261408684672548885},
    {"nome": "NEXT STAGE", "ID": 1261408595501912134},
    {"nome": "Onipresente", "ID": 1261408536567746646},
    {"nome": "Deus dragão", "ID": 1261408636698099712},
    {"nome": "CLThanos", "ID": 1261408468548714630},
    {"nome": "Súditos de Soul", "ID": 1263306902780117077}
]

cargo_especial_uma_estrela = {"nome": "P★", "ID": 1261153826354892840}
cargo_especial_duas_estrelas = {"nome": "P★★", "ID": 1261154053421928491}
cargo_especial_tres_estrelas = {"nome": "P★★★", "ID": 1261154085919395893}
cargo_especial_quatro_estrelas = {"nome": "P★★★★", "ID": 1261154101140394036}
cargo_especial_cinco_estrelas = {"nome": "P★★★★★", "ID": 1261154117078876259}
cargo_especial_seis_estrelas = {"nome": "P★★★★★★", "ID": 1261154134619590728}
cargo_especial_sete_estrelas = {"nome": "P★★★★★★★", "ID": 1261154151610449952}

preco_1 = 150
preco_1m = 275
preco_2 = 400
preco_2m = 550
preco_3 = 600
preco_3m = 650
preco_4 = 700
preco_4m = 750
preco_5 = 800
preco_5m = 850
preco_6 = 900
preco_6m = 950
preco_7 = 1000
preco_7m = 1500

def return_random_role():
    # Actually
    if random.choice(range(1,5)) == 3:
        is_m = True
    else:
        is_m = False

    rarity = random.choice(range(1,100))
    if rarity >= 1 and rarity <= 30:
        if is_m:
            cargo = random.choice(cargos_uma_estrela_m)
            preco = preco_1m
        else:
            cargo = random.choice(cargos_uma_estrela)
            preco = preco_1
        cargo_especial = cargo_especial_uma_estrela
    elif rarity >= 31 and rarity <= 55:
        if is_m:
            cargo = random.choice(cargos_duas_estrelas_m)
            preco = preco_2m
        else:
            cargo = random.choice(cargos_duas_estrelas)
            preco = preco_2
        cargo_especial = cargo_especial_duas_estrelas
    elif rarity >= 56 and rarity <= 70:
        if is_m:
            cargo = random.choice(cargos_tres_estrelas_m)
            preco = preco_3m
        else:
            cargo = random.choice(cargos_tres_estrelas)
            preco = preco_3
        cargo_especial = cargo_especial_tres_estrelas
    elif rarity >= 71 and rarity <= 80:
        if is_m:
            cargo = random.choice(cargos_quatro_estrelas_m)
            preco = preco_4m
        else:
            cargo = random.choice(cargos_quatro_estrelas)
            preco = preco_4
        cargo_especial = cargo_especial_quatro_estrelas
    elif rarity >= 81 and rarity <= 86:
        if is_m:
            cargo = random.choice(cargos_cinco_estrelas_m)
            preco = preco_5m
        else:
            cargo = random.choice(cargos_cinco_estrelas)
            preco = preco_5
        cargo_especial = cargo_especial_cinco_estrelas
    elif rarity >= 87 and rarity <= 93:
        if is_m:
            cargo = random.choice(cargos_seis_estrelas_m)
            preco = preco_6m
        else:
            cargo = random.choice(cargos_seis_estrelas)
            preco = preco_6
        cargo_especial = cargo_especial_seis_estrelas
    elif rarity >= 94 and rarity <= 100:
        if is_m:
            cargo = random.choice(cargos_sete_estrelas_m)
            preco = preco_7m
        else:
            cargo = random.choice(cargos_sete_estrelas)
            preco = preco_7
        cargo_especial = cargo_especial_sete_estrelas
    else:
        cargo = ""
        preco = ""
        cargo_especial = ""

    return { "is_m": is_m, "preco": preco, "cargo": cargo, "cargo_especial": cargo_especial}
