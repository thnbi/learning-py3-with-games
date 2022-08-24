import random

def jogar():
    print("\n*********************************")
    print("Bem-vinde ao jogo da adivinhação!")
    print("*********************************\n")

    numero_secreto = random.randrange(1, 11)
    tentativas_disponiveis = 0
    pontos = 100

    print("escolha a dificuldade")
    print("(1) fácil (2) médio (3) difícil \n(4) escolher quantidade de chances\n")

    nivel = int(input("nível escolhido: "))

    while(tentativas_disponiveis == 0):
        if(nivel == 1):
            tentativas_disponiveis = 8
        elif(nivel == 2):
            tentativas_disponiveis = 4
        elif(nivel == 3):
            tentativas_disponiveis = 2
        elif(nivel == 4):
            tentativas_disponiveis = int(input("Digite a quantidade de chances que você deseja ter: "))
        else:
            print("escolha um nível entre as opções\n")
            nivel = int(input("nível escolhido: "))

    for rodada in range(1, tentativas_disponiveis + 1):
        print("\nTentativa: {} de {}". format(rodada, tentativas_disponiveis))
        chute = int(input("Digite número entre 1 e 10: "))
        pontos_perdidos = numero_secreto - chute
        pontos = pontos - abs(pontos_perdidos)

        
        if(chute < 1 or chute > 10):
            print("Você deve digitar um número entre 1 e 10")
            rodada = rodada + 1
            continue

        if(chute == numero_secreto): 
            print("\nparabéns você acertou o número secreto!")
            print("sua pontuação foi de: {} pontos". format(pontos))
            break
        else:
            if(chute > numero_secreto):
                print("\nVocê errou, o número secreto é menor que", chute, "tente novamente...")
            else:
                print("\nVocê errou, o número secreto é maior que", chute, "tente novamente...")

    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()