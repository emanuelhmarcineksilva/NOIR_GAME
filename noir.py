

import random



#--------------------    <| VARIAVEIS |>    --------------------

gameOn = True


nomes = ["Salvatore","Giovanni","Rossi","Don Vito","Luciano","Policial","Matteo","Michele",]
nomesAleatoriesados = []




#--------------------    <| FUNCOES (MSG) |>    --------------------

def msgBemVindo():
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  A noite chovia como se o céu quisesse lavar os pecados da cidade.    ║")
    print("║  Don Vito, o velho chefe da máfia, sentia o cheiro da traição no ar.  ║")
    print("║  Alguém dentro da família andava falando demais...                    ║")
    print("║  e ele me contratou para descobrir quem. Eu sou Rossi.                ║")
    print("║  Detetive particular. E, naquela noite, nada era o que parecia.       ║")
    print("║                                                                       ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

def arteItens():
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║                            Itens da Máfia                             ║")
    print("║                                                                       ║")
    print("║                     █   ███████      ███████   █                      ║")
    print("║                     █  █       █    █       █  █                      ║")
    print("║                      ██         ████         ██                       ║")
    print("║                       █        █    █        █                        ║")
    print("║                        █      █      █      █                         ║")
    print("║                         ██████        ██████                          ║")
    print("║                                                                       ║")
    print("║                              [ ÓCULOS ]                               ║")
    print("║                                                                       ║")
    print("║                            Itens da Máfia                             ║")
    print("║                                                                       ║")
    print("║                            ▄█████████████▄                            ║")
    print("║                            ██           ██                            ║")
    print("║                            ██           ██                            ║")
    print("║                            ██           ██                            ║")
    print("║                            ██▄▄▄▄▄▄▄▄▄▄▄██                            ║")
    print("║                         █████████████████████                         ║")
    print("║                                                                       ║")
    print("║                              [ CARTOLA ]                              ║")
    print("║                                                                       ║")
    print("║                            Itens da Máfia                             ║")
    print("║                                                                       ║")
    print("║                               ▄▄▄▄▄▄▄▄                                ║")
    print("║                               █      █                                ║")
    print("║                         ▄██████████████████▄                          ║")
    print("║                         ██                ██                          ║")
    print("║                         ██                ██                          ║")
    print("║                         ██                ██                          ║")
    print("║                         ▀██████████████████▀                          ║")
    print("║                                                                       ║")
    print("║                               [ MALA ]                                ║")
    print("║                                                                       ║")
    print("║                            Itens da Máfia                             ║")
    print("║                                                                       ║")
    print("║                             ▄▌         ▄                              ║")
    print("║                            ████████████▄                              ║")
    print("║                                    ▄▐████                             ║")
    print("║                                       ▐███                            ║")
    print("║                                                                       ║")
    print("║                               [ PISTOLA ]                             ║")
    print("║                                                                       ║")
    print("║                            Itens da Máfia                             ║")
    print("║                                                                       ║")
    print("║                                                                       ║")
    print("║                                        ▀                              ║")
    print("║                                      ▀  ▀                             ║")
    print("║                                                                       ║")
    print("║                                ███████▒█                              ║")
    print("║                                                                       ║")
    print("║                               [ CHARUTO ]                             ║")
    print("║                                                                       ║")
    print("║                                                                       ║")
    print("║                            Itens da Máfia                             ║")
    print("║                                                                       ║")
    print("║                                 ▄█████▄                               ║")
    print("║                                ▄▀   ▄▄▀                               ║")
    print("║                              ▄▀ ▄▄▀▀                                  ║")
    print("║                              ▀▀▀                                      ║")
    print("║                                                                       ║")
    print("║                               [ Pizza ]                               ║")
    print("║                                                                       ║")
    print("║                            Itens da Máfia                             ║")
    print("║                                                                       ║")
    print("║                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                         ║")
    print("║                          █▀     ▄▄ ▄ ▄ ▄▄   █                         ║")
    print("║                          █ ▄▄  ▄▄ ▄ ▄▄ ▄    █                         ║")
    print("║                          █   ▄▄ ▄▄ ▄▄ ▄▄    █                         ║")
    print("║                          █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀                          ║")
    print("║                                                                       ║")
    print("║                       [ PAPEL COM CÓDIGO MORSE ]                      ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")


arteItens()

def msgPreposicoesAleatorias():

    aleatorizarNomes()
    

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  O capanga ",nomesAleatoriesados[0]," estava no restaurante lavando dinheiro;")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  ",nomesAleatoriesados[1]," estava no restaurante lavando dinheiro;")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  ",nomesAleatoriesados[2]," estava ocupado escoltando o chefe;")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  ",nomesAleatoriesados[3]," estava livre durante a noite;")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  ",nomesAleatoriesados[3]," se encontrou com o policial na calada na noite;")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

#--------------------    <| FUNCOES (calculos) |>    --------------------

def aleatorizarNomes():
    for i in nomes:
        
        nomeAleatorio = random.choice(nomes)

        nomesAleatoriesados.append(nomeAleatorio)
        nomes.remove(nomeAleatorio)
        






#--------------------    <| INTRODUCAO |>    --------------------



msgBemVindo()
msgPreposicoesAleatorias()



#--------------------    <| JOGO |>    --------------------
#
#while gameOn == True:
#
#    print("loop")
#    gameOn = False








