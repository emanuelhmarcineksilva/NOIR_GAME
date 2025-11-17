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


nomes = ["Salvatore","Giovanni","Rossi","Don Vito","Luciano","Policial","Matteo","Michele",]
nomesAleatoriesados = []


objetos = ["Cartola", "Mala", "Pistola", "Charuto", "Pizza de alho", "Papel com código Morse"]


locais = ["Jardim","Corredor", "Cozinha", "Sala de estar", "Quarto de Don Vito", "Quarto de Luciano", "Quarto de Salvatore", "Quarto de Michele", "Quarto de Giovanni", "Quarto de Rossi", "Quarto de Matteo"]
localAtual = "Sala de estar"

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
    print("║                          [ Pizza de alho ]                            ║")
    print("║                                                                       ║")
    print("║                            Itens da Máfia                             ║")
    print("║                                                                       ║")
    print("║                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                          ║")
    print("║                          █▀     ▄▄ ▄ ▄ ▄▄   █                         ║")
    print("║                          █ ▄▄  ▄▄ ▄ ▄▄ ▄    █                         ║")
    print("║                          █   ▄▄ ▄▄ ▄▄ ▄▄    █                         ║")
    print("║                          █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀                          ║")
    print("║                                                                       ║")
    print("║                       [ PAPEL COM CÓDIGO MORSE ]                      ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

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
    print("║              █▀▀▀▀▀▀▀▀▀▀▀▀▀█  █▀▀  ▀▀█  █▀▀▀▀▀▀▀▀▀▀█                  ║")
    print("║              █ Q. Giovanni ▒▒▒▒  (2) ▒▒▒▒ Q. Vaziu █                  ║")
    print("║              █▄▄▄▄▄▄▄▄▄▄▄▄▄█  █▄▄  ▄▄█  █▄▄▄▄▄▄▄▄▄▄█                  ║")
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
    print("║  Descubra quem é o capanga que está no restaurante lavando dinheiro.  ║")
    print("║                                                                       ║")
    print("║  Seja rápido, pois o tempo é curto. Você tem até 00:00.               ║")
    print("║                                                                       ║")
    print("║  Atenciosamente,                                                      ║")
    print("║  Don Vito                                                             ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")



## ---- Transições


def transicao():
    for i in range(5):
        print(".")
        
def miniTransicao():
    for i in range(2):
        print(".")


## ---- Painel de decisões

def painelDeDecisoes():
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                         O que devo fazer?                             ║")
    print("║               ╔══════════════════════════════════════╗                ║")
    print("║               ║   1) Andar                           ║                ║")
    print("║               ║   2) Investigar                      ║                ║")
    print("║               ║   3) Ver mapa                        ║                ║")
    print("║               ║   4) Ver carta                       ║                ║")
    print("║               ║   5) Checar horário                  ║                ║")
    print("║               ║                                      ║                ║")
    print("║               ╚══════════════════════════════════════╝                ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")

    respostaDecisao = input("Resposta: ")

    if respostaDecisao == "1":
        andar()
    elif respostaDecisao == "2":
        investigar()
    elif respostaDecisao == "3":
        verMapa()
    elif respostaDecisao == "4":
        verCarta()
    elif respostaDecisao == "5":
        checarHorario()
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

            #conversaComMichele()
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

            #conversaComMatteo()
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
        print("║               ║   3) Quarto Vaziu                    ║                ║")
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
            localAtual = "Corredor 2"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Quarto trancado...                                                   ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")
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

            #conversaComGiovanni()
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
            print("║  Rossi entrou no quarto do Don Vito...                                ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            #conversaComDonVito()
            miniTransicao()
            painelDeDecisoes()
        elif respostaDecisaoLocal == "3":
            localAtual = "Quarto Luciano"
            print("╔═══════════════════════════════════════════════════════════════════════╗")
            print("║                                                                       ║")
            print("║  Rossi entrou no quarto de Luciano...                                 ║")
            print("║                                                                       ║")
            print("╚═══════════════════════════════════════════════════════════════════════╝")

            #conversaComLuciano()
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

            #conversaComSalvatore()
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

    if localAtual == "Quarto Giovanni":

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║           Eu estou no Quarto do Giovanni para onde devo ir?           ║")
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
    global fraseInvestigando
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
    global localAtual
    global pontos
    global minuto
    global hora

    if localAtual == "Cozinha":
        tempoInvestigando = random.randint(2,15)
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║                           Item encontrado!                            ║")
        print("║                                                                       ║")
        print("║                            Itens da Máfia                             ║")
        print("║                                                                       ║")
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
        print("║                            [ + 20 pontos ]                            ║")
        print("║                     [ tempo perdido = "+str(tempoInvestigando).zfill(2)+" minutos ]                    ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        minuto += tempoInvestigando
        pontos += 20


    elif localAtual == "Sala de jogos":
        tempoInvestigando = random.randint(2,15)
        
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║                           Item encontrado!                            ║")
        print("║                                                                       ║")
        print("║                            Itens da Máfia                             ║")
        print("║                                                                       ║")
        print("║                                                                       ║")
        print("║                     █   ███████      ███████   █                      ║")
        print("║                     █  █       █    █       █  █                      ║")
        print("║                      ██         ████         ██                       ║")
        print("║                       █        █    █        █                        ║")
        print("║                        █      █      █      █                         ║")
        print("║                         ██████        ██████                          ║")
        print("║                                                                       ║")
        print("║                              [ ÓCULOS ]                               ║")
        print("║                            [ + 10 pontos ]                            ║")
        print("║                     [ tempo perdido = "+str(tempoInvestigando).zfill(2)+" minutos ]                    ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        minuto += tempoInvestigando
        pontos += 10

    elif localAtual == "Jardim":
        tempoInvestigando = random.randint(2,15)
        
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║                           Item encontrado!                            ║")
        print("║                                                                       ║")
        print("║                            Itens da Máfia                             ║")
        print("║                                                                       ║")
        print("║                                                                       ║")
        print("║                            ▄█████████████▄                            ║")
        print("║                            ██           ██                            ║")
        print("║                            ██           ██                            ║")
        print("║                            ██           ██                            ║")
        print("║                            ██▄▄▄▄▄▄▄▄▄▄▄██                            ║")
        print("║                         █████████████████████                         ║")
        print("║                                                                       ║")
        print("║                              [ CARTOLA ]                              ║")
        print("║                            [ + 10 pontos ]                            ║")
        print("║                     [ tempo perdido = "+str(tempoInvestigando).zfill(2)+" minutos ]                    ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        minuto += tempoInvestigando
        pontos += 10

    elif localAtual == "Corredor 1":
        tempoInvestigando = random.randint(2,15)
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║                           Item encontrado!                            ║")
        print("║                                                                       ║")
        print("║                            Itens da Máfia                             ║")
        print("║                                                                       ║")
        print("║                                                                       ║")
        print("║                                 ▄█████▄                               ║")
        print("║                                ▄▀   ▄▄▀                               ║")
        print("║                              ▄▀ ▄▄▀▀                                  ║")
        print("║                              ▀▀▀                                      ║")
        print("║                                                                       ║")
        print("║                          [ Pizza de alho ]                            ║")
        print("║                     [ tempo perdido = "+str(tempoInvestigando).zfill(2)+" minutos ]                    ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        minuto += tempoInvestigando

    elif localAtual == "Corredor 2":
        tempoInvestigando = random.randint(2,15)

        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║                           Item encontrado!                            ║")
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
        print("║                             [ + 10 pontos ]                           ║")
        print("║                     [ tempo perdido = "+str(tempoInvestigando).zfill(2)+" minutos ]                    ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        minuto += tempoInvestigando
        pontos += 10

    elif localAtual == "Corredor 3":
        tempoInvestigando = random.randint(2,15)
        
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║                           Item encontrado!                            ║")
        print("║                                                                       ║")
        print("║                            Itens da Máfia                             ║")
        print("║                                                                       ║")
        print("║                                                                       ║")
        print("║                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                          ║")
        print("║                          █▀     ▄▄ ▄ ▄ ▄▄   █                         ║")
        print("║                          █ ▄▄  ▄▄ ▄ ▄▄ ▄    █                         ║")
        print("║                          █   ▄▄ ▄▄ ▄▄ ▄▄    █                         ║")
        print("║                          █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀                          ║")
        print("║                                                                       ║")
        print("║                       [ PAPEL COM CÓDIGO MORSE ]                      ║")
        print("║                            [ + 30 pontos ]                            ║")
        print("║                     [ tempo perdido = "+str(tempoInvestigando).zfill(2)+" minutos ]                    ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        minuto += tempoInvestigando
        pontos += 30

    elif localAtual == "Escada 1" or localAtual == "Escada 2":
        tempoInvestigando = random.randint(2,15)
        
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║                           Item encontrado!                            ║")
        print("║                                                                       ║")
        print("║                            Itens da Máfia                             ║")
        print("║                                                                       ║")
        print("║                                                                       ║")
        print("║                             ▄▌         ▄                              ║")
        print("║                            ████████████▄                              ║")
        print("║                                    ▄▐████                             ║")
        print("║                                       ▐███                            ║")
        print("║                                                                       ║")
        print("║                               [ PISTOLA ]                             ║")
        print("║                             [ + 20 pontos ]                           ║")
        print("║                     [ tempo perdido = "+str(tempoInvestigando).zfill(2)+" minutos ]                    ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")

        minuto += tempoInvestigando
        pontos += 20

    else: 
        tempoInvestigando = random.randint(2,15)
        print("╔═══════════════════════════════════════════════════════════════════════╗")
        print("║                                                                       ║")
        print("║                      Nada foi encontrado aqui                         ║")
        print("║                     Tempo perdido = "+ str(tempoInvestigando).zfill(2)+" minutos                        ║")
        print("║                                                                       ║")
        print("╚═══════════════════════════════════════════════════════════════════════╝")
    

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
    painelDeDecisoes()







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


## ---- Gamer Over

def gameOver():
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║                     O tempo acabou - GAME OVER                        ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")
    exit()





#--------------------    <| FUNCOES (calculos) |>    --------------------

def aleatorizarNomes():
    for i in nomes:
        
        nomeAleatorio = random.choice(nomes)

        nomesAleatoriesados.append(nomeAleatorio)
        nomes.remove(nomeAleatorio)
        


## ---- Tempo passando
if hora >= 24:
    gameOver()

if minuto >= 60: # Criando relogio
    hora += 1
    minuto -= 60


## ---- texto investigando

fraseInvestigando = random.choice(textosInvestigacao)



#--------------------    <| INTRODUCAO |>    --------------------



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







