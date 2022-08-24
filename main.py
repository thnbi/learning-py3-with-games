import numero_secreto

print("\naprendendo python com joguinhos\n")

print("escolha o seu jogo: ")

print("(1) numero secreto")

opcao = int(input("escolha a opção: "))

falta_escolher = True

while(falta_escolher):
   if(opcao == 1):
      falta_escolher = False
      numero_secreto.jogar()
   else:
      print("não temos esta opçao")
      opcao = int(input("escolha a opção: "))