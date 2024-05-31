from classes.jogador import*
from funcoes import*
desisao = 0
while(desisao != 2):
    matriz = [
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]

    print("**Jogo da velha**")
    print("Menu:")
    print("1 - Começar Jogo")
    print("2 - Sair do jogo")
    decisao = int(input("Escolha (1 ou 2) : "))
    print(" ")
    
    if(decisao == 1):
        nome = input("Digite o seu nome :")
        jogador = Jogador(nome,0)
        computador = Jogador("computador",0)
        posicao = None
        contador = 0
        while(posicao != 0):
            imprimir_matriz(matriz)
            print("Pontuação")
            print(f"{jogador.nome}:{jogador.getPontos()}", end = " ")
            print(f"{computador.nome}:{computador.getPontos()}", end = " ")
            print()

            posicao = int(input("Escolha onde deseja marcar(1 a 9) ou 0 para sair:"))
            if posicao_disponivel(matriz,posicao):
               marcar(matriz,posicao, "X")
               contador+=1
               jogadaComputador = melhor_Jogada(matriz,"O")
               marcar(matriz,jogadaComputador,"O")
               contador+=1
               if(contador >=9):
                   print("Empate!")
                   limpar_matriz(matriz)
                   contador = 0
               if verificar_vencedor(matriz,"X"):
                   imprimir_matriz()
                   print(f"Parabéns {jogador.nome} você ganhou!")
                   jogador.setPontos()
                   limpar_matriz(matriz)
                   contador = 0
               elif verificar_vencedor(matriz,"O"):
                   imprimir_matriz(matriz)
                   print("Computador Venceu!")
                   computador.setPontos()
                   limpar_matriz(matriz)
                   contador = 0
            else:
               print("Posição inválida digite outro número")

    else:
        print("Valor inválido!") 
            
            