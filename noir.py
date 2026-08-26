# Requisitos jogo
#• O jogo deve seguir o mesmo tema dos slides (mesma história, personagens, itens, locais e fatos).
#• A conclusão é fixa.
#• Randomização: sorteio de nomes e características com locais e com itens (se possível, dependendo do tema) para variar as partidas.
#• Regras de jogo:
#o pontuação;
#o ganhos/perdas por acertos e erros;
#o decisões do jogador (ex.: “arriscar o culpado”, “pedir dica”) com impacto na pontuação.
#• Término explícito: mensagem/tela final (vitória/derrota/estatísticas).


import random
from threading import local
import time ################# colocamos o time avise a professora



#--------------------    <| VARIAVEIS |>    --------------------

gameOn = True


nomes = ["Salvatore","Giovanni","Luciano","Joshef","Matteo","Michele"]
nomesAleatoriesados = []

mauHumorado1 = ""
mauHumorado2 = ""
verdadeiro1 = ""
verdadeiro2 = ""

## objetos, quem usa quando e para que 


objetos = ["Cartola", "Mala", "Pistola", "Charuto", "Pizza de alho", "Papel com código Morse", "Óculos"]
objetosAleatoriesados = []

quantidadeItensEncontrados = 0


quantidadePremissasEncontradas = 6
listaPremissasEncontradas = []

premissaItem = []

locais = ["Jardim", "Corredor 1", "Corredor 2", "Corredor 3", "Escada 1", "Escada 2", "Cozinha", "Sala de estar", "Sala de jogos"]
localAtual = "Sala de estar"
locaisAleatoriesados = []


estado = ["Investigando", "Parado", "Vendo relógio de bolso", "Vendo Mapa1", "Vendo Mapa2"] # mostra o que o detetive esta fazendo no momento

textosInvestigacao = ["Rossi olha ao seu redor e começa a procurar...                     ",
"Rossi respira fundo e inicia a busca...                           ",
"Rossi dá o primeiro passo e começa a investigar...                ",
"Rossi ajusta o chapéu e inicia a procura...                       ",
"Rossi observa o ambiente e começa a busca...                      ",
"Rossi avança em silêncio e inicia a investigação...               ",
"Rossi começa a examinar cada detalhe ao seu redor...              ",
"Rossi entra em ação e inicia a procura...                         ",
"Rossi começa a seguir pistas sem perder tempo...                  ",
"Rossi inicia a análise do local com atenção...                    ",
"Rossi começa a caminhar lentamente, atento a tudo...              ",
"Rossi inicia sua busca com passos firmes...                       ",
"Rossi examina o espaço e começa a investigar...                   ",
"Rossi se concentra e inicia a procura...                          ",
"Rossi observa cada canto antes de começar a busca...              ",
"Rossi inicia a busca com calma e precisão...                      ",
"Rossi começa a investigar sem hesitar...                          ",
"Rossi avança e inicia a busca pelo que precisa...                 ",
"Rossi olha atentamente e dá início à investigação...              ",
"Rossi começa a procurar por qualquer sinal útil...                "
]


## ---- Horário
hora = 22
minuto = 00


tempoAndar = 1 # minutos que leva para andar de um lugar para outro
tempoInvestigar = 15 # minutos que leva para investigar um local
tempoConversar = 10 # minutos que leva para conversar com alguem


## ---- Pontuação
pontos = 0

## ---- Traidor

traidor = ""


#--------------------    <| FUNCOES (MSG) |>    --------------------

def preparativosIniciais():
    global nomesAleatoriesados
    global objetosAleatoriesados
    global listaItensEncontrados
    global premissaItem
    global listaPremissasEncontradas
    global locaisAleatoriesados
    global mauHumorado1
    global mauHumorado2
    global verdadeiro1
    global verdadeiro2
    global traidor


    aleatorizarNomes()
    aleatorizarObjetos()
    aleatorizarLocais()
        
    ## ---- Traidor

    traidor = nomesAleatoriesados[0]

    listaItensEncontrados = [False] * len(objetosAleatoriesados) # aqui deixa cada posicao do array como False
    premissaItem = [False] * len(objetosAleatoriesados) # aqui deixa cada posicao do array como False
    listaPremissasEncontradas = [False] * len(nomesAleatoriesados) # de acordo com a quantidade de pessoas suspeitas ele deixa as primissas falsas


    mauHumorado1 = random.choice(nomesAleatoriesados)
    mauHumorado2 = random.choice(nomesAleatoriesados)
    nomesParaVerdadeiro = [nome for nome in nomesAleatoriesados if nome != mauHumorado1 and nome != mauHumorado2 and nome != traidor]
    verdadeiro1 = random.choice(nomesParaVerdadeiro)
    verdadeiro2 = random.choice(nomesParaVerdadeiro)






    




def msgBemVindo():
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  A noite chovia como se o céu quisesse lavar os pecados da cidade.    ║")
    print("║  Don Vito, o velho chefe da máfia, sentia o cheiro da traição no ar.  ║")
    print("║  Alguém dentro da família andava falando demais...                    ║")
    print("║  e ele me contratou para descobrir quem. Eu sou Rossi.                ║")
    print("║  Detetive particular. E, naquela noite, nada era o que parecia.       ║")
    print("║                                                                       ║")
    print("║   Estou nesse belo jardim... mas devo entar e começar a investigar!   ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    miniTransicao()


def entradaNaCasa():

    input("Pressione Enter para continuar...")

    miniTransicao()

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  Rossi entrou na casa...                                              ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    localAtual == "Sala de estar"
    
    transicao()


    ## ---- Pegando os mapas

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  Quando entrei na casa um homem de chapeu alto me entregou três       ║")
    print("║  papeis e saiu rapidamente. Não foi possivel identificar quem era.    ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    pergunta = input("Ver papeis? (s/n)")
    if pergunta == "s":
        mapaPrimeiroAndar()
        mapaSegundoAndar()

        miniTransicao()
    
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║  Parecem ser dois mapas do primeiro e segundo andar do edificio.      ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        miniTransicao()

        cartaDonVito()

        miniTransicao()

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║  Rossi: Até meia noite? Ele deve estar brincando comigo.              ║")
        print("║                                                                       ║")
        print("║  Após se acalmar, Rossi pindura seu guardachuva e diz:                ║")
        print("║                                                                       ║")
        print("║  Rossi: Preciso começar.                                              ║")
        print("║                                                                       ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        transicao()


    else:
        
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║  Não tenho tempo para isso....                                        ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        transicao()
    
    


    miniTransicao()

## ---- Mapas

def mapaPrimeiroAndar():
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                          Mapa Primeiro Andar                          ║")
    print("║                                                                       ║")
    print("║                          █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█                           ║")
    print("║                          █                █                           ║")
    print("║                          █    Cozinha     █                           ║")
    print("║                          █                █                           ║")
    print("║                          █▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄█                           ║")
    print("║                                 █  █                                  ║")
    print("║                                 █  █                                  ║")
    print("║                                 █  █                                  ║")
    print("║                        █▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█                         ║")
    print("║                        █                    █     ▒▒▒▒▒▒▒▒▒▒▒▒        ║")
    print("║                        █    Sala de estar   ▒▒▒▒▒▒▒ Jardim ▒▒▒        ║")
    print("║                        █                    █     ▒▒▒▒▒▒▒▒▒▒▒▒        ║")
    print("║                        █▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█                         ║")
    print("║                                 █  █                                  ║")
    print("║                                 █  █                                  ║")
    print("║                                 █  █                                  ║")
    print("║                        █▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█                         ║")
    print("║                        █                    █                         ║")
    print("║                        █    Sala de jogos   █                         ║")
    print("║                        █                    █                         ║")
    print("║                        █▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█                         ║")
    print("║                                 █  █                                  ║")
    print("║                                 █  █                                  ║")
    print("║                                 █  █                                  ║")
    print("║                            █▀▀▀▀▀  ▀▀▀▀▀█                             ║")
    print("║                            █   Escada   █                             ║")
    print("║                            █▄▄▄▄▄▄▄▄▄▄▄▄█                             ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    input("Pressione enter para continuar...")


def mapaSegundoAndar():
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                          Mapa Segundo Andar                           ║")
    print("║                                                                       ║")
    print("║                            █▀▀▀▀▀▀▀▀▀▀▀▀▀█                            ║")
    print("║                            █ Q. Don Vito █                            ║")
    print("║                            █▄▄▄▄▄  ▄▄▄▄▄▄█                            ║")
    print("║                                  ▒▒                                   ║")
    print("║             █▀▀▀▀▀▀▀▀▀▀▀▀▀▀█  █▀▀  ▀▀█  █▀▀▀▀▀▀▀▀▀▀▀▀█                ║")
    print("║             █ Q. Salvatore ▒▒▒▒  (3) ▒▒▒▒ Q. Luciano █                ║")
    print("║             █▄▄▄▄▄▄▄▄▄▄▄▄▄▄█  █▄▄  ▄▄█  █▄▄▄▄▄▄▄▄▄▄▄▄█                ║")
    print("║                                 █  █                                  ║")
    print("║                                 █  █                                  ║")
    print("║              █▀▀▀▀▀▀▀▀▀▀▀▀▀█  █▀▀  ▀▀█  █▀▀▀▀▀▀▀▀▀▀▀█                 ║")
    print("║              █ Q. Giovanni ▒▒▒▒  (2) ▒▒▒▒ Q. Joshef █                 ║")
    print("║              █▄▄▄▄▄▄▄▄▄▄▄▄▄█  █▄▄  ▄▄█  █▄▄▄▄▄▄▄▄▄▄▄█                 ║")
    print("║                                 █  █                                  ║")
    print("║                                 █  █                                  ║")
    print("║                █▀▀▀▀▀▀▀▀▀▀▀█  █▀▀  ▀▀█  █▀▀▀▀▀▀▀▀▀▀▀█                 ║")
    print("║                █ Q. Matteo ▒▒▒▒  (1) ▒▒▒▒ Q.Michele █                 ║")
    print("║                █▄▄▄▄▄▄▄▄▄▄▄█  █▄▄  ▄▄█  █▄▄▄▄▄▄▄▄▄▄▄█                 ║")
    print("║                                 █  █                                  ║")
    print("║                                 █  █                                  ║")
    print("║                                 █  █                                  ║")
    print("║                            █▀▀▀▀▀  ▀▀▀▀▀█                             ║")
    print("║                            █   Escada   █                             ║")
    print("║                            █▄▄▄▄▄▄▄▄▄▄▄▄█                             ║")
    print("║                                                                       ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    input("Pressione enter para continuar...")
    transicao()

## ---- Carta Don Vito

def cartaDonVito():
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  Carta do Don Vito                                                    ║")
    print("║                                                                       ║")
    print("║  Boa Noite Rossi.                                                     ║")
    print("║                                                                       ║")
    print("║  Descubra quem é o capanga que está vazando informações...            ║")
    print("║                                                                       ║")
    print("║  Seja rápido, pois o tempo é curto. Você tem até 00:00.               ║")
    print("║                                                                       ║")
    print("║  Atenciosamente,                                                      ║")
    print("║  Don Vito                                                             ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

## ---- Itens

def itensImagem(nome):
    if nome == "Mala":
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

    if nome == "Cartola":
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

    if nome == "Charuto":  
        print("║                                                                       ║")
        print("║                                        ▀                              ║")
        print("║                                      ▀  ▀                             ║")
        print("║                                                                       ║")
        print("║                                ███████▒█                              ║")
        print("║                                                                       ║")
        print("║                               [ CHARUTO ]                             ║")
        print("║                                                                       ║")

    if nome == "Pizza de alho":  
        print("║                                                                       ║")
        print("║                                 ▄█████▄                               ║")
        print("║                                ▄▀   ▄▄▀                               ║")
        print("║                              ▄▀ ▄▄▀▀                                  ║")
        print("║                              ▀▀▀                                      ║")
        print("║                                                                       ║")
        print("║                          [ Pizza de alho ]                            ║")
        print("║                                                                       ║")

    if nome == "Papel com código Morse":  
        print("║                                                                       ║")
        print("║                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                          ║")
        print("║                          █▀     ▄▄ ▄ ▄ ▄▄   █                         ║")
        print("║                          █ ▄▄  ▄▄ ▄ ▄▄ ▄    █                         ║")
        print("║                          █   ▄▄ ▄▄ ▄▄ ▄▄    █                         ║")
        print("║                          █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀                          ║")
        print("║                                                                       ║")
        print("║                       [ PAPEL COM CÓDIGO MORSE ]                      ║")
        print("║                                                                       ║")

    if nome == "Pistola":  
        print("║                                                                       ║")
        print("║                             ▄▌         ▄                              ║")
        print("║                            ████████████▄                              ║")
        print("║                                    ▄▐████                             ║")
        print("║                                       ▐███                            ║")
        print("║                                                                       ║")
        print("║                               [ PISTOLA ]                             ║")
        print("║                                                                       ║")

    if nome == "Óculos":
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

## ---- Transições


def transicao():
    for i in range(5):
        print(".")
        
def miniTransicao():
    for i in range(2):
        print(".")


## ---- Painel de decisões

def painelDeDecisoes():
    global hora
    
    if hora == 24:
        gameOver()

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                         O que devo fazer?                             ║")
    print("║               ╔══════════════════════════════════════╗                ║")
    print("║               ║   1) Andar                           ║                ║")
    print("║               ║   2) Investigar                      ║                ║")
    print("║               ║   3) Ver mapa                        ║                ║")
    print("║               ║   4) Ver carta                       ║                ║")
    print("║               ║   5) Checar horário                  ║                ║")
    print("║               ║   6) Itens encontrados               ║                ║")
    print("║               ║   7) Premiças                        ║                ║")
    print("║               ║   8) Encerar caso                    ║                ║")
    print("║               ╚══════════════════════════════════════╝                ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")


    respostaDecisao = input("Resposta: ")

    if respostaDecisao == "1":
        if hora == 24:
            gameOver()
        else:
            andar()
    elif respostaDecisao == "2":
        if hora == 24:
            gameOver()
        else:
            investigar()
    elif respostaDecisao == "3":
        if hora == 24:
            gameOver()
        else:
            verMapa()
    elif respostaDecisao == "4":
        if hora == 24:
            gameOver()
        else:
            verCarta()
    elif respostaDecisao == "5":
        if hora == 24:
            gameOver()
        else:
            checarHorario()
    elif respostaDecisao == "6":
        if hora == 24:
            gameOver()
        else:
            verItensEncontrados()
    elif respostaDecisao == "7":
        if hora == 24:
            gameOver()
        else:
            verPremissas()
    elif respostaDecisao == "8":
        if hora == 24:
            gameOver()
        else:
            encerarCaso()
    else:
        miniTransicao()
        print("Estou pensando de mais... preciso tomar uma decisão certa!")
        miniTransicao()
        painelDeDecisoes()


## ---- Ações ANDAR

def andar():
    global localAtual
    global minuto
    global tempoAndar
    global tempoInvestigar
    global tempoConversar

    if localAtual == "Jardim":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                 Eu estou no Jardim para onde devo ir?                 ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Entrar na casa                  ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Sala de estar"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou na casa...                                              ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()

    if localAtual == "Sala de estar":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║             Eu estou na Sala de estar para onde devo ir?              ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Cozinha                         ║                ║")
        print("║               ║   2) Sala de jogos                   ║                ║")
        print("║               ║   3) Jardim                          ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Cozinha"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou na cozinha...                                           ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            print("somou")
            painelDeDecisoes()
        elif respostaDecisaoLocal == "2":
            localAtual = "Sala de jogos"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou na sala de jogos...                                     ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()

        elif respostaDecisaoLocal == "3":
            localAtual = "Jardim"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi foi para o Jardim...                                           ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()

    if localAtual == "Cozinha":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                Eu estou na Cozinha para onde devo ir?                 ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Sala de estar                   ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Sala de estar"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou na sala de estar...                                     ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()


    if localAtual == "Sala de jogos":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║             Eu estou na Sala de jogos para onde devo ir?              ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Sala de estar                   ║                ║")
        print("║               ║   2) Escada                          ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Sala de estar"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou na sala de estar...                                     ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        elif respostaDecisaoLocal == "2":
            localAtual = "Escada 1"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi foi para a escada...                                           ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()

    if localAtual == "Escada 1":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║         Eu estou na Escada do segundo andar para onde devo ir?        ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Subir para segundo andar        ║                ║")
        print("║               ║   2) Sala de jogos                   ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Escada 2"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi subiu as escadas...                                            ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        elif respostaDecisaoLocal == "2":
            localAtual = "Sala de jogos"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou na sala de jogos...                                     ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()



    if localAtual == "Escada 2":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║         Eu estou na Escada no segundo andar para onde devo ir?        ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Descer para primeiro andar      ║                ║")
        print("║               ║   2) andar pelo corredor (1)         ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Escada 1"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi desceu para o primeiro andar...                                ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        elif respostaDecisaoLocal == "2":
            localAtual = "Corredor 1"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi andou pelo corredor...                                         ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()



    if localAtual == "Corredor 1":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║              Eu estou no Corredor (1) para onde devo ir?              ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Andar pelo corredor (2)         ║                ║")
        print("║               ║   2) Quarto Michele                  ║                ║")
        print("║               ║   3) Quarto Matteo                   ║                ║")
        print("║               ║   4) Escada                          ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Corredor 2"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi andou pelo corredor...                                         ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        elif respostaDecisaoLocal == "2":
            localAtual = "Quarto Michele"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou no Quarto da Michele...                                 ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            conversa("Michele")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        elif respostaDecisaoLocal == "3":
            localAtual = "Quarto Matteo"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou no quarto da Matteo...                                  ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            conversa("Matteo")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        elif respostaDecisaoLocal == "4":
            localAtual = "Escada 2"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi foi para a escada...                                           ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()


    if localAtual == "Corredor 2":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║              Eu estou no Corredor (2) para onde devo ir?              ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Andar pelo corredor (3)         ║                ║")
        print("║               ║   2) Andar pelo corredor (1)         ║                ║")
        print("║               ║   3) Quarto Joshef                   ║                ║")
        print("║               ║   4) Quarto Giovanni                 ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Corredor 3"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi andou pelo corredor...                                         ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        elif respostaDecisaoLocal == "2":
            localAtual = "Corredor 1"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi andou pelo corredor...                                         ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        elif respostaDecisaoLocal == "3":
            localAtual = "Quarto Joshef"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou no quarto do Joshef...                                  ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            conversa("Joshef")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        elif respostaDecisaoLocal == "4":
            localAtual = "Quarto Giovanni"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou no quarto do Giovanni...                                ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            conversa("Giovanni")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()

    if localAtual == "Corredor 3":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║              Eu estou no corredor (3) para onde devo ir?              ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Andar pelo corredor (2)         ║                ║")
        print("║               ║   2) Quarto Don Vito                 ║                ║")
        print("║               ║   3) Quarto Luciano                  ║                ║")
        print("║               ║   4) Quarto Salvatore                ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Corredor 2"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi andou pelo corredor...                                         ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        elif respostaDecisaoLocal == "2":
            localAtual = "Quarto Don Vito"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi bateu na porta...                                              ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            conversa("Don Vito")
            miniTransicao()
            painelDeDecisoes()
        elif respostaDecisaoLocal == "3":
            localAtual = "Quarto Luciano"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou no quarto de Luciano...                                 ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            conversa("Luciano")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        elif respostaDecisaoLocal == "4":
            localAtual = "Quarto Salvatore"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou no quarto do Salvatore...                               ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            conversa("Salvatore")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()


    if localAtual == "Quarto Michele" or localAtual == "Quarto Matteo":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║           Eu estou no " + localAtual + " para onde devo ir?           ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Sair do Quarto                  ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Corredor 1"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi saiu do quarto...                                              ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()

    if localAtual == "Quarto Giovanni" or localAtual == "Quarto Joshef":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║           Eu estou no " + localAtual + " para onde devo ir?           ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Sair do Quarto                  ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Corredor 2"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi saiu do quarto...                                              ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()

    if localAtual == "Quarto Salvatore" or localAtual == "Quarto Luciano" or localAtual == "Quarto Don Vito":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║           Eu estou no " + localAtual + " para onde devo ir?           ║")
        print("║               ╔══════════════════════════════════════╗                ║")
        print("║               ║   1) Sair do Quarto                  ║                ║")
        print("║               ║   0) Tomar outra descisão            ║                ║")
        print("║               ╚══════════════════════════════════════╝                ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        miniTransicao()
        respostaDecisaoLocal = input("Resposta: ")
        transicao()
        if respostaDecisaoLocal == "1":
            localAtual = "Corredor 3"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi saiu do quarto...                                              ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
            miniTransicao()
            minuto += tempoAndar
            painelDeDecisoes()
        else:
            miniTransicao()
            painelDeDecisoes()


## ---- Ações INVESTIGAR


def investigar():
    global textosInvestigacao
    fraseInvestigando = random.choice(textosInvestigacao)
    global minuto

    transicao()
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  " + fraseInvestigando + "   ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")
    transicao()

    itemEncontrado()
    miniTransicao()

    painelDeDecisoes()

def itemEncontrado():
    global quantidadeItensEncontrados
    global objetosAleatoriesados
    global listaItensEncontrados
    global premissaItem
    global locaisAleatoriesados
    global localAtual
    global pontos
    global minuto
    global hora

    encontrou = False
    
    for i in range(len(listaItensEncontrados)): # range percorre todos os itens da lista e len retorna o tamanho da lista
        if localAtual == locaisAleatoriesados[i] and listaItensEncontrados[i] == False:

            tempoInvestigando = random.randint(2,15)
            pontosItem = random.choice([10,20,30])

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║                           Item encontrado!                            ║")
            print("║                                                                       ║")
            print("║                            Itens da Máfia                             ║")
            print("║                                                                       ║")
            itensImagem(objetosAleatoriesados[i])
            print("║                             [ + " + str(pontosItem) + " pontos ]                           ║")
            print("║                     [ tempo perdido = "+str(tempoInvestigando).zfill(2)+" minutos ]                    ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            minuto += tempoInvestigando
            pontos += pontosItem
            listaItensEncontrados[i] = True
            quantidadeItensEncontrados += 1
            encontrou = True

            premissaItem[i] = True


    if encontrou == False: 
        tempoInvestigando = random.randint(2,15)
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║                      Nada foi encontrado aqui                         ║")
        print("║                     Tempo perdido = "+ str(tempoInvestigando).zfill(2)+" minutos                        ║")
        print("║                                                                       ║")
        print("║                            [ - 5 pontos ]                             ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        minuto += tempoInvestigando
        pontos -= 5


## ---- Ver Itens Encontrados

def verItensEncontrados():
    global listaItensEncontrados
    global quantidadeItensEncontrados

    if quantidadeItensEncontrados == 0:
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║                      Nenhum item encontrado...                        ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        painelDeDecisoes()

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║                          " + str(quantidadeItensEncontrados) + " Item encontrado!                           ║")
    
    if listaItensEncontrados[0] == True:  
        itensImagem(objetosAleatoriesados[0])
        premissaItem[0] == True

    if listaItensEncontrados[1] == True: 
        itensImagem(objetosAleatoriesados[1])

    if listaItensEncontrados[2] == True:  
        itensImagem(objetosAleatoriesados[2])
    
    if listaItensEncontrados[3] == True:  
        itensImagem(objetosAleatoriesados[3])

    if listaItensEncontrados[4] == True:  
        itensImagem(objetosAleatoriesados[4])

    if listaItensEncontrados[5] == True:  
        itensImagem(objetosAleatoriesados[5])

    if listaItensEncontrados[6] == True:  
        itensImagem(objetosAleatoriesados[6])

    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    painelDeDecisoes()


## ---- Ações VER MAPA

def verMapa():
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                             Qual mapa?                                ║")
    print("║               ╔══════════════════════════════════════╗                ║")
    print("║               ║   1) Primeiro andar                  ║                ║")
    print("║               ║   2) Segundo andar                   ║                ║")
    print("║               ║   0) Tomar outra descisão            ║                ║")
    print("║               ╚══════════════════════════════════════╝                ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")
    miniTransicao()
    respostaDecisaoMapa = input("Mapa: ")
    transicao()
    if respostaDecisaoMapa == "1":
        mapaPrimeiroAndar()
        miniTransicao()
        painelDeDecisoes()
    elif respostaDecisaoMapa == "2":
        mapaSegundoAndar()
        miniTransicao()
        painelDeDecisoes()
    else:
        miniTransicao()
        painelDeDecisoes()


## ---- Ações VER CARTA

def verCarta():
    transicao()
    cartaDonVito()
    miniTransicao()
    painelDeDecisoes()


## ---- Ações CHECAR HORARIO

def checarHorario():
    global minuto
    global hora

    if minuto >= 60: # usando Relogio
        hora += 1
        minuto -= 60

    horario = str(hora).zfill(2) + ":" + str(minuto).zfill(2)

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║  Agora são " + horario +"                                                      ║") # ta certo
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")
    transicao()
    if hora == 24:
        gameOver()
    painelDeDecisoes()


## ---- Ações VER PREMISSAS

def conversa(nome):
    global localAtual
    global hora
    global minuto
    global traidor
    global listaPremissasEncontradas
    global quantidadePremissasEncontradas
    global mauHumorado1
    global mauHumorado2
    global verdadeiro1
    global verdadeiro2
    
    if nome == "Don Vito":
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║  Don Vito: Entre, Rossi...                                            ║")
        print("║                                                                       ║")
        print("║  Rossi: Desculpe incomodar, Don Vito.                                 ║")
        print("║                                                                       ║")
        print("║  Don Vito: Não se preocupe. Diga-me... como está avançando o caso?    ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        status = input("Responda: ")

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print(f"  Rossi: {status}                                                      ")
        print("║                                                                       ║")
        print("║  Don Vito: Hm... Entendo.                                             ║")
        print("║  Don Vito: Rossi, seu tempo está se esgotando...                      ║")
        print("║                                                                       ║")
        print("║  Rossi ergue os olhos e encara o relógio na parede...                 ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        minuto += random.randint(5, 10)

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║  O relógio marca " + str(hora) + ":" + str(minuto) + "                                               ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║  Rossi Preocupado diz: Entendi... Vou acelerar isso.                  ║")
        print("║                                                                       ║")
        print("║  Don Vito: Faça isso. Espero resultados, Rossi.                       ║")
        print("║                                                                       ║")
        print("║  Don Vito gira a cadeira lentamente em direção à janela…              ║")
        print("║  Sem olhar para trás, leva o drink à boca em silêncio...              ║")
        print("║  Rossi sai do escritório e fecha a porta atrás de si.                 ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        localAtual = "Corredor 3"

        input("Pressione Enter para continuar...")


# ------ LUCIANO
    if nome == "Luciano":

        if (traidor == "Luciano" or mauHumorado1 == "Luciano" or mauHumorado2 == "Luciano"):

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi: Olá Luciano, como vai?                                        ║")
            print("║                                                                       ║")
            print("║  Luciano: Não tenho nada para falar com você Rossi!                   ║")
            print("║                                                                       ║")
            print("║  Rossi vira as costas e sai do quarto...                              ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi para na porta e diz: Muito suspeito!                           ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            minuto += random.randint(2, 4)

            localAtual = "Corredor 3"

        elif (verdadeiro1 == "Luciano" or verdadeiro2 == "Luciano"):

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Luciano: Olá Rossi! O que faz Aqui?                                  ║")
            print("║                                                                       ║")
            print("║  Rossi: Venho buscar informações...                                   ║")
            print("║                                                                       ║")
            print("║  Luciano: O que está procurando detetive?                             ║")
            print("║                                                                       ║")
            print("║  Rossi: Imagino que tenha percebido uma movimentação estranha na      ║")
            print("║  mansão... Alguém esta vazando informaçães por baixo dos panos...     ║")
            print("║                                                                       ║")
            print("║  Luciano: Não sei se acredito nessa conversa... Conheço muito bem     ║")
            print("║  meus colegas!                                                        ║")
            print("║                                                                       ║")
            print("║  Rossi: Lhe garanto que alguém esta traindo a todos aqui... As        ║")
            print("║  informações correm e não param!                                      ║")
            print("║                                                                       ║")
            print("║  Luciano olha no fundo dos olhos de Rossi...                          ║")
            print("║                                                                       ║")
            print("║  Luciano suspira e fala: Certo detetive... Tem algo acontecendo...    ║")
            print("║                                                                       ║")
            print("║  Rossi se inclica para escurtar melhor.                               ║")
            print("║                                                                       ║")
            print("  Luciano: "+locaisAleatoriesados[0]+". Vi algo ou alguém... "+nomesAleatoriesados[0]+" ou talvez "+nomesAleatoriesados[4]+"...    ")
            print("  Quem sabe?.. Levava algo... "+objetosAleatoriesados[0]+" ou "+objetosAleatoriesados[5]+"... Vai saber...        ")
            print("║                                                                       ║")
            print("║  Rossi se vira e vai até a porta e diz: Era disso que precisava!      ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[0] = True
            quantidadePremissasEncontradas += 1

        
        else:

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Luciano: Olá Rossi! O que faz Aqui?                                  ║")
            print("║                                                                       ║")
            print("║  Rossi: Venho buscar informações...                                   ║")
            print("║                                                                       ║")
            print("║  Luciano: O que está procurando detetive?                             ║")
            print("║                                                                       ║")
            print("║  Rossi: Imagino que tenha percebido uma movimentação estranha na      ║")
            print("║  mansão... Alguém esta vazando informaçães por baixo dos panos...     ║")
            print("║                                                                       ║")
            print("║  Luciano: Não sei se acredito nessa conversa... Conheço muito bem     ║")
            print("║  meus colegas!                                                        ║")
            print("║                                                                       ║")
            print("║  Rossi: Lhe garanto que alguém esta traindo a todos aqui... As        ║")
            print("║  informações correm e não param!                                      ║")
            print("║                                                                       ║")
            print("║  Luciano olha no fundo dos olhos de Rossi...                          ║")
            print("║                                                                       ║")
            print("║  Luciano suspira e fala: Certo detetive... Tem algo acontecendo...    ║")
            print("║                                                                       ║")
            print("║  Rossi se inclica para escurtar melhor.                               ║")
            print("║                                                                       ║")
            print("  Luciano: "+locaisAleatoriesados[2]+". Vi algo ou alguém... "+nomesAleatoriesados[0]+" ou talvez "+nomesAleatoriesados[2]+"...    ")
            print("  Quem sabe?.. Levava algo... "+objetosAleatoriesados[3]+" ou "+objetosAleatoriesados[0]+"... Vai saber...        ")
            print("║                                                                       ║")
            print("║  Rossi se vira e vai até a porta e diz: Era disso que precisava!      ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[2] = True
            quantidadePremissasEncontradas += 1

# ------ SALVATORE
    if nome == "Salvatore":

        if (traidor == "Salvatore" or mauHumorado1 == "Salvatore" or mauHumorado2 == "Salvatore"):

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi: Salvatore... posso falar com você?                            ║")
            print("║                                                                       ║")
            print("║  Salvatore: Não tenho nada para conversar com você, detetive.         ║")
            print("║                                                                       ║")
            print("║  Rossi observa o tom seco e dá um passo para trás...                  ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi murmura enquanto sai: Muito suspeito...                        ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            minuto += random.randint(2, 4)
            localAtual = "Corredor 3"

        elif (verdadeiro1 == "Salvatore" or verdadeiro2 == "Salvatore"):
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Salvatore: Ah… você é o detetive, certo?                             ║")
            print("║                                                                       ║")
            print("║  Rossi: Só estou recolhendo alguns detalhes...                        ║")
            print("║                                                                       ║")
            print("║  Salvatore: Detalhes sobre o quê exatamente?                          ║")
            print("║                                                                       ║")
            print("║  Rossi: Há alguém passando informações para fora da mansão.           ║")
            print("║  Não sabemos quem é… ainda.                                           ║")
            print("║                                                                       ║")
            print("║  Salvatore olha discretamente para o corredor antes de responder…     ║")
            print("║                                                                       ║")
            print("║  Salvatore: Se isso é verdade… então você vai querer saber disso.     ║")
            print("║                                                                       ║")
            print("║  Rossi inclina a cabeça, atento.                                      ║")
            print("║                                                                       ║")
            print("  Salvatore: "+locaisAleatoriesados[0]+", vi alguém… "+nomesAleatoriesados[4]+" ou talvez "+nomesAleatoriesados[0]+".   ")
            print("  Ele carregava algo estranho… "+objetosAleatoriesados[0]+" ou talvez "+objetosAleatoriesados[4]+"… Difícil dizer.           ")
            print("║                                                                       ║")
            print("║  Rossi: Isso já ajuda muito. Obrigado.                                ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[0] = True
            quantidadePremissasEncontradas += 1


        else:

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Salvatore: Ah… você é o detetive, certo?                             ║")
            print("║                                                                       ║")
            print("║  Rossi: Só estou recolhendo alguns detalhes...                        ║")
            print("║                                                                       ║")
            print("║  Salvatore: Detalhes sobre o quê exatamente?                          ║")
            print("║                                                                       ║")
            print("║  Rossi: Há alguém passando informações para fora da mansão.           ║")
            print("║  Não sabemos quem é… ainda.                                           ║")
            print("║                                                                       ║")
            print("║  Salvatore olha discretamente para o corredor antes de responder…     ║")
            print("║                                                                       ║")
            print("║  Salvatore: Se isso é verdade… então você vai querer saber disso.     ║")
            print("║                                                                       ║")
            print("║  Rossi inclina a cabeça, atento.                                      ║")
            print("║                                                                       ║")
            print("  Salvatore: "+locaisAleatoriesados[1]+", vi alguém… "+nomesAleatoriesados[4]+" ou talvez "+nomesAleatoriesados[1]+".   ")
            print("  Ele carregava algo estranho… "+objetosAleatoriesados[0]+" ou talvez "+objetosAleatoriesados[4]+"… Difícil dizer.           ")
            print("║                                                                       ║")
            print("║  Rossi: Isso já ajuda muito. Obrigado.                                ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[1] = True
            quantidadePremissasEncontradas += 1

# ------ GIOVANNI
    if nome == "Giovanni":

        if (traidor == "Giovanni" or mauHumorado1 == "Giovanni" or mauHumorado2 == "Giovanni"):

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi: Giovanni... preciso de um minuto.                             ║")
            print("║                                                                       ║")
            print("║  Giovanni: Não agora, detetive. Vá incomodar outra pessoa.            ║")
            print("║                                                                       ║")
            print("║  Rossi percebe a hostilidade e inclina a cabeça, analisando-o.        ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi sussurra enquanto se afasta: Muito suspeito…                   ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            minuto += random.randint(2, 4)
            localAtual = "Corredor 2"

        elif (verdadeiro1 == "Giovanni" or verdadeiro2 == "Giovanni"):

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Giovanni: Ah… o detetive. Está procurando algo específico?           ║")
            print("║                                                                       ║")
            print("║  Rossi: Apenas tentando juntar algumas peças…                         ║")
            print("║                                                                       ║")
            print("║  Giovanni: Peças? Isto soa… sério.                                    ║")
            print("║                                                                       ║")
            print("║  Rossi: Alguém está vazando informações.                              ║")
            print("║                                                                       ║")
            print("║  Giovanni ergue a sobrancelha desconfiado.                            ║")
            print("║                                                                       ║")
            print("║  Giovanni: Se quer saber… algo passou pelos meus olhos mais cedo.     ║")
            print("║                                                                       ║")
            print("║  Rossi fica atento, inclinando a cabeça.                              ║")
            print("║                                                                       ║")
            print("  Giovanni: "+locaisAleatoriesados[0]+", vi alguém… "+nomesAleatoriesados[0]+" ou talvez "+nomesAleatoriesados[2]+".")
            print("  Ele segurava algo estranho… "+objetosAleatoriesados[0]+" ou "+objetosAleatoriesados[1]+"… bem suspeito.")
            print("║                                                                       ║")
            print("║  Rossi: Isso pode ser útil. Obrigado.                                 ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[0] = True
            quantidadePremissasEncontradas += 1

        else:

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Giovanni: Ah… o detetive. Está procurando algo específico?           ║")
            print("║                                                                       ║")
            print("║  Rossi: Apenas tentando juntar algumas peças…                         ║")
            print("║                                                                       ║")
            print("║  Giovanni: Peças? Isto soa… sério.                                    ║")
            print("║                                                                       ║")
            print("║  Rossi: Alguém está vazando informações.                              ║")
            print("║                                                                       ║")
            print("║  Giovanni ergue a sobrancelha desconfiado.                            ║")
            print("║                                                                       ║")
            print("║  Giovanni: Se quer saber… algo passou pelos meus olhos mais cedo.     ║")
            print("║                                                                       ║")
            print("║  Rossi fica atento, inclinando a cabeça.                              ║")
            print("║                                                                       ║")
            print("  Giovanni: "+locaisAleatoriesados[3]+", vi alguém… "+nomesAleatoriesados[3]+" ou talvez "+nomesAleatoriesados[2]+".")
            print("  Ele segurava algo estranho… "+objetosAleatoriesados[5]+" ou "+objetosAleatoriesados[1]+"… bem suspeito.")
            print("║                                                                       ║")
            print("║  Rossi: Isso pode ser útil. Obrigado.                                 ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[3] = True
            quantidadePremissasEncontradas += 1


# ------ JOSHEF
    if nome == "Joshef":

        if (traidor == "Joshef" or mauHumorado1 == "Joshef" or mauHumorado2 == "Joshef"):

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi: Joshef… preciso falar com você.                               ║")
            print("║                                                                       ║")
            print("║  Joshef: Hmph… não estou interessado em conversar, detetive.          ║")
            print("║                                                                       ║")
            print("║  Rossi sente o clima pesado e estreita os olhos…                      ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi murmura enquanto se afasta: Muito suspeito…                    ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            minuto += random.randint(2, 4)
            localAtual = "Corredor 2"

        elif (verdadeiro1 == "Joshef" or verdadeiro2 == "Joshef"):
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Joshef: Ah… o detetive finalmente chegou.                            ║")
            print("║                                                                       ║")
            print("║  Rossi: Só estou colhendo pistas…                                     ║")
            print("║                                                                       ║")
            print("║  Joshef: Pistas? Isso está ficando interessante.                      ║")
            print("║                                                                       ║")
            print("║  Rossi: Alguém aqui dentro está repassando informações.               ║")
            print("║                                                                       ║")
            print("║  Joshef esfrega o queixo, pensativo…                                  ║")
            print("║                                                                       ║")
            print("║  Joshef: Talvez eu tenha visto algo… você decide se serve ou não.     ║")
            print("║                                                                       ║")
            print("║  Rossi mantém o olhar firme, atento.                                  ║")
            print("║                                                                       ║")
            print("  Joshef: No(a) "+locaisAleatoriesados[0]+", alguém estava lá… "+nomesAleatoriesados[0]+" ou talvez "+nomesAleatoriesados[3]+".")
            print("  E segurava algo que chamou atenção… "+objetosAleatoriesados[0]+" ou "+objetosAleatoriesados[4]+"… não parecia normal.")
            print("║                                                                       ║")
            print("║  Rossi: Isso ajuda bastante. Obrigado.                                ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[0] = True
            quantidadePremissasEncontradas += 1

        else:

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Joshef: Ah… o detetive finalmente chegou.                            ║")
            print("║                                                                       ║")
            print("║  Rossi: Só estou colhendo pistas…                                     ║")
            print("║                                                                       ║")
            print("║  Joshef: Pistas? Isso está ficando interessante.                      ║")
            print("║                                                                       ║")
            print("║  Rossi: Alguém aqui dentro está repassando informações.               ║")
            print("║                                                                       ║")
            print("║  Joshef esfrega o queixo, pensativo…                                  ║")
            print("║                                                                       ║")
            print("║  Joshef: Talvez eu tenha visto algo… você decide se serve ou não.     ║")
            print("║                                                                       ║")
            print("║  Rossi mantém o olhar firme, atento.                                  ║")
            print("║                                                                       ║")
            print("  Joshef: No(a) "+locaisAleatoriesados[4]+", alguém estava lá… "+nomesAleatoriesados[4]+" ou talvez "+nomesAleatoriesados[2]+".")
            print("  E segurava algo que chamou atenção… "+objetosAleatoriesados[2]+" ou "+objetosAleatoriesados[3]+"… não parecia normal.")
            print("║                                                                       ║")
            print("║  Rossi: Isso ajuda bastante. Obrigado.                                ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[4] = True
            quantidadePremissasEncontradas += 1

        
# ------ MATTEO
    if nome == "Matteo":

        if (traidor == "Matteo" or mauHumorado1 == "Matteo" or mauHumorado2 == "Matteo"):

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi: Matteo… precisa dizer algo.                                   ║")
            print("║                                                                       ║")
            print("║  Matteo: Não estou com paciência, detetive. Volte outra hora.         ║")
            print("║                                                                       ║")
            print("║  Rossi observa o tom ríspido, desconfiado…                            ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi murmura enquanto sai: Muito suspeito…                          ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            minuto += random.randint(2, 4)
            localAtual = "Corredor 1"

        elif (verdadeiro1 == "Matteo" or verdadeiro2 == "Matteo"):

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Matteo: Hm… o detetive. Imagino que esteja investigando algo sério.  ║")
            print("║                                                                       ║")
            print("║  Rossi: Apenas juntando possíveis pistas.                             ║")
            print("║                                                                       ║")
            print("║  Matteo: Entendo… e sei que coisas estranhas estão acontecendo.       ║")
            print("║                                                                       ║")
            print("║  Rossi: Alguém está vazando informações de dentro da mansão.          ║")
            print("║                                                                       ║")
            print("║  Matteo estreita os olhos, ponderando…                                ║")
            print("║                                                                       ║")
            print("║  Matteo: Então talvez isso interesse você.                            ║")
            print("║                                                                       ║")
            print("║  Rossi inclina a cabeça, atento ao que vem.                           ║")
            print("║                                                                       ║")
            print("  Matteo: "+locaisAleatoriesados[0]+", havia alguém… "+nomesAleatoriesados[0]+" ou talvez "+nomesAleatoriesados[2]+".")
            print("  E carregava algo suspeito… "+objetosAleatoriesados[0]+" ou "+objetosAleatoriesados[5]+"… parecia importante.")
            print("║                                                                       ║")
            print("║  Rossi: Isso pode ajudar bastante. Agradeço.                          ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[0] = True
            quantidadePremissasEncontradas += 1

        else:

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Matteo: Hm… o detetive. Imagino que esteja investigando algo sério.  ║")
            print("║                                                                       ║")
            print("║  Rossi: Apenas juntando possíveis pistas.                             ║")
            print("║                                                                       ║")
            print("║  Matteo: Entendo… e sei que coisas estranhas estão acontecendo.       ║")
            print("║                                                                       ║")
            print("║  Rossi: Alguém está vazando informações de dentro da mansão.          ║")
            print("║                                                                       ║")
            print("║  Matteo estreita os olhos, ponderando…                                ║")
            print("║                                                                       ║")
            print("║  Matteo: Então talvez isso interesse você.                            ║")
            print("║                                                                       ║")
            print("║  Rossi inclina a cabeça, atento ao que vem.                           ║")
            print("║                                                                       ║")
            print("  Matteo: "+locaisAleatoriesados[5]+", havia alguém… "+nomesAleatoriesados[5]+" ou talvez "+nomesAleatoriesados[2]+".")
            print("  E carregava algo suspeito… "+objetosAleatoriesados[4]+" ou "+objetosAleatoriesados[0]+"… parecia importante.")
            print("║                                                                       ║")
            print("║  Rossi: Isso pode ajudar bastante. Agradeço.                          ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[5] = True
            quantidadePremissasEncontradas += 1


# ------ MICHELE
    if nome == "Michele":

        if (traidor == "Michele" or mauHumorado1 == "Michele" or mauHumorado2 == "Michele"):

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi: Michele… preciso de algumas palavras.                         ║")
            print("║                                                                       ║")
            print("║  Michele: Não estou disposta a conversar agora, detetive.             ║")
            print("║                                                                       ║")
            print("║  Rossi sente o clima frio e observa a expressão rígida…               ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi murmura ao sair: Muito suspeito…                               ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            minuto += random.randint(2, 4)
            localAtual = "Corredor 1"

        elif (verdadeiro1 == "Michele" or verdadeiro2 == "Michele"):

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Michele: Ah… o detetive. Está procurando algo específico?            ║")
            print("║                                                                       ║")
            print("║  Rossi: Apenas colhendo pequenos detalhes…                            ║")
            print("║                                                                       ║")
            print("║  Michele: Imagino. Tenho visto coisas estranhas ultimamente.          ║")
            print("║                                                                       ║")
            print("║  Rossi: Alguém está vazando informações dentro da mansão.             ║")
            print("║                                                                       ║")
            print("║  Michele respira fundo, olhando para os lados…                        ║")
            print("║                                                                       ║")
            print("║  Michele: Então talvez isso seja útil para você.                      ║")
            print("║                                                                       ║")
            print("║  Rossi observa em silêncio, esperando mais.                           ║")
            print("║                                                                       ║")
            print("  Michele: "+locaisAleatoriesados[0]+", percebi alguém… "+nomesAleatoriesados[0]+" ou talvez "+nomesAleatoriesados[1]+".")
            print("  E parecia esconder algo… "+objetosAleatoriesados[0]+" ou "+objetosAleatoriesados[2]+"… algo que não deveria estar ali.")
            print("║                                                                       ║")
            print("║  Rossi: Isso é exatamente o que eu precisava. Obrigado.               ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[0] = True
            quantidadePremissasEncontradas += 1

        else:

            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Michele: Ah… o detetive. Está procurando algo específico?            ║")
            print("║                                                                       ║")
            print("║  Rossi: Apenas colhendo pequenos detalhes…                            ║")
            print("║                                                                       ║")
            print("║  Michele: Imagino. Tenho visto coisas estranhas ultimamente.          ║")
            print("║                                                                       ║")
            print("║  Rossi: Alguém está vazando informações dentro da mansão.             ║")
            print("║                                                                       ║")
            print("║  Michele respira fundo, olhando para os lados…                        ║")
            print("║                                                                       ║")
            print("║  Michele: Então talvez isso seja útil para você.                      ║")
            print("║                                                                       ║")
            print("║  Rossi observa em silêncio, esperando mais.                           ║")
            print("║                                                                       ║")
            print("  Michele: "+locaisAleatoriesados[1]+", percebi alguém… "+nomesAleatoriesados[5]+" ou talvez "+nomesAleatoriesados[1]+".")
            print("  E parecia esconder algo… "+objetosAleatoriesados[4]+" ou "+objetosAleatoriesados[0]+"… algo que não deveria estar ali.")
            print("║                                                                       ║")
            print("║  Rossi: Isso é exatamente o que eu precisava. Obrigado.               ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            listaPremissasEncontradas[1] = True
            quantidadePremissasEncontradas += 1


    

        


def verPremissas():
    global listaPremissasEncontradas
    global quantidadePremissasEncontradas
    global quantidadeItensEncontrados
    global objetosAleatoriesados
    global locaisAleatoriesados
    global nomesAleatoriesados


    
    if quantidadePremissasEncontradas == 0:
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║                        Nenhuma premissa...                            ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        painelDeDecisoes()

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║                              Premissas:                               ║")
    

    ## Se estiver se perguntando o porque dos "i + 1", é para melhorar a aleatoriedade, só que tem que pensar bem nas quantidades de cada coisa para funcionar
    ## Coloquei as 3 situações que pude prevenir um possivel problema com o traidor e ele aparecer denovo ou aparecer com a primissa errada

    # 1 se só tiver o traidor nas premissas encontradas
    if quantidadePremissasEncontradas == 1 and listaPremissasEncontradas[0] == True:
        print("║                                                                       ║")
        print("║  Se "+ str(objetosAleatoriesados[0]) +" estiver "+ str(locaisAleatoriesados[0]) +" então "+ str(nomesAleatoriesados[0]) +" é o traidor!  ")
        print("║                                                                       ║")

    # 2 se tiver mais de 1 premissa encontrada e a premissa do traidor foi encontrada também
    if quantidadePremissasEncontradas > 1 and listaPremissasEncontradas[0] == True:
        print("║                                                                       ║")
        print("║  Se "+ str(objetosAleatoriesados[0]) +" estiver "+ str(locaisAleatoriesados[0]) +" então "+ str(nomesAleatoriesados[0]) +" é o traidor!  ")
        print("║                                                                       ║")

        for i in range(len(listaPremissasEncontradas) - 1):
            if listaPremissasEncontradas[i + 1] == True:  

                print("║                                                                       ║")
                print("║  Se "+ str(objetosAleatoriesados[i + 1]) +" estiver "+ str(locaisAleatoriesados[i]) +" então "+ str(nomesAleatoriesados[i + 1]) +" é o traidor!  ")
                print("║                                                                       ║")

    # 3 se tiver mais de 1 premissa encontrada e a do traidor ainda não
    if quantidadePremissasEncontradas > 1 and listaPremissasEncontradas[0] == False:
        for i in range(len(listaPremissasEncontradas) - 1):
            if listaPremissasEncontradas[i + 1] == True:  

                print("║                                                                       ║")
                print("║  Se "+ str(objetosAleatoriesados[i - 1]) +" estiver "+ str(locaisAleatoriesados[i + 1]) +" então "+ str(nomesAleatoriesados[i + 1]) +" é o traidor!  ")
                print("║                                                                       ║")

    ## -- Colocando premissas dos itens

    if quantidadeItensEncontrados >= 1:
        for i in range(len(premissaItem)):
            if premissaItem[i] == True:
                
                print("║                                                                       ║")
                print("║  "+ str(objetosAleatoriesados[i]) +"... local: "+ str(locaisAleatoriesados[i]))
                print("║                                                                       ║")
                      
        
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    painelDeDecisoes()

## ---- Encerra o caso
def encerarCaso():
    global traidor

    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║    Rossi... finalmente... descide acabar com o caso...........        ║")
    print("║                                                                       ║")
    print("║     Rossi diz: O traidor é o                                          ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")
    miniTransicao()
    
    respostaNomeTraidor = input("NOME DO TRAIDOR: ")

    if respostaNomeTraidor.lower() == traidor.lower():
        transicao()
        venceu()
    else:
        transicao()
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("                ERRROU! O TRAIDOR ERA " + traidor.upper() + " !                 ")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
        gameOver()




## ---- Mensagens preposições aleatórias

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


## ---- Venceu

def venceu():
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║                     PARABÉNS! VOCÊ VENCEU O JOGO!                     ║")
    print("║                                                                       ║")
    print("║                          PONTOS TOTAIS: " + str(pontos).zfill(2) + "                            ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")
    exit()



## ---- Gamer Over

def gameOver():
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║                     O tempo acabou - GAME OVER                        ║")
    print("║                                                                       ║")
    print("║                       PONTOS TOTAIS: " + str(pontos).zfill(2) + "                               ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")
    exit()



#--------------------    <| FUNCOES (calculos) |>    --------------------

def aleatorizarNomes():
    global nomes
    global nomesAleatoriesados

    quantidadeNomes = len(nomes)

    for i in range(quantidadeNomes):
        
        nomeAleatorio = random.choice(nomes)

        nomesAleatoriesados.append(nomeAleatorio)
        nomes.remove(nomeAleatorio)
    
    

        
        
def aleatorizarObjetos():
    global objetos
    global objetosAleatoriesados

    objetosAleatoriesados = []

    while objetos:
        
        objetoAleatorio = random.choice(objetos)

        objetosAleatoriesados.append(objetoAleatorio)
        objetos.remove(objetoAleatorio)

def aleatorizarLocais():
    global locais
    global locaisAleatoriesados

    locaisAleatoriesados = []

    while locais:
        
        localAleatorio = random.choice(locais)

        locaisAleatoriesados.append(localAleatorio)
        locais.remove(localAleatorio)

## ---- Tempo passando

if minuto >= 60: # Criando relogio
    hora += 1
    minuto -= 60

if hora == 24:
    gameOver()



#--------------------    <| INTRODUCAO |>    --------------------

preparativosIniciais() # Deixar itens aleatórios
msgBemVindo()
entradaNaCasa()
#msgPreposicoesAleatorias()

painelDeDecisoes()





#--------------------    <| JOGO |>    --------------------
#
#while gameOn == True:
#
#    print("loop")
#    gameOn = False







