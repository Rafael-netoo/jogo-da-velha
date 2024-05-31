#reseta a matriz
def limpar_matriz(matriz):
    for i in range(3):
        for j in range(3):
            matriz[i][j] = "_"
#imprimir a matriz           
def imprimir_matriz(matriz):
    for linha in matriz:
     for elemento in linha:
        print(elemento,end = " ")
     print()
#verifica se uma posição está disponível
def posicao_disponivel(matriz, posicao):
    if posicao == 1:
        if matriz[0][0] == "_":
            return True
        else:
            False
    elif posicao == 2:
        if matriz[0][1] == "_":
            return True
        else:
            return False
    elif posicao == 3:
        if matriz[0][2] == "_":
            return True
        else :
            return False
    elif posicao == 4:
        if matriz[1][0] == "_":
            return True
        else:
            return False
    elif posicao == 5:
        if matriz[1][1] == "_":
            return True
        else:
            return False
    elif posicao == 6:
        if matriz[1][2] == "_":
            return True
        else:
            return False
    elif posicao == 7:
        if matriz[2][0] == "_":
            return True
        else:
            return False
    elif posicao == 8:
        if matriz[2][1] == "_":
          return True
        else:
          return False
    elif posicao == 9:
        if matriz[2][2] == "_":
          return True
        else:
          return False

#função que retorna qual a melhor jogada possível para o computador
def melhor_Jogada(matriz,simbolo):
      #verifica se o jogador pode vencer na próxima rodada
        for posicao in range(1,10):
            if posicao_disponivel(matriz,posicao):
             marcar(matriz,posicao,"X")
             if verificar_vencedor(matriz, "X"):
                marcar(matriz,posicao,"_")
                return posicao
             marcar(matriz,posicao,"_")
       #verifica se o computador pode vencer na próxima rodada
        for posicao in range(1,10):
            if posicao_disponivel(matriz,posicao):
             marcar(matriz,posicao,"O")
             if verificar_vencedor(matriz, "O"):
                marcar(matriz,posicao,"_")
                return posicao
             marcar(matriz,posicao,"_")
        # Jogar no centro se disponível
        if posicao_disponivel(matriz, 5):
           return 5

        # Jogar em um dos cantos se disponível
        for posicao in [1, 3, 7, 9]:
          if posicao_disponivel(matriz, posicao):
            return posicao

        # Jogar em uma das bordas se disponível
        for posicao in [2, 4, 6, 8]:
          if posicao_disponivel(matriz, posicao):
            return posicao



#verifica se o simbolo(x ou o) passado como parâmetro ganhou a partida
def verificar_vencedor(matriz, simbolo):
    for i in range(3):
          if matriz[i][0] == simbolo and matriz[i][1] == simbolo and matriz[i][2] == simbolo:
            return True
    for j in range(3):
          if matriz[0][j] == simbolo and matriz[1][j] == simbolo and matriz[2][j] == simbolo:
            return True
    if matriz[0][0] == simbolo and matriz[1][1] == simbolo and matriz[2][2] == simbolo:
        return True
    if matriz[0][2] == simbolo and matriz[1][1] == simbolo and matriz[2][0] == simbolo:
        return True
    return False

#Marca na posição indicada  
def marcar(matriz,posicao, simbolo):
    if posicao == 1:
        matriz[0][0] = simbolo
    elif posicao == 2:
        matriz[0][1] = simbolo
    elif posicao == 3:
        matriz[0][2] = simbolo
    elif posicao == 4:
        matriz[1][0] = simbolo
    elif posicao == 5:
        matriz[1][1] = simbolo
    elif posicao == 6:
        matriz[1][2] = simbolo
    elif posicao == 7:
        matriz[2][0] = simbolo
    elif posicao == 8:
        matriz[2][1] = simbolo
    elif posicao == 9:
        matriz[2][2] = simbolo
    else:
        print("Posição inválida! Digite um número entre 1 e 9.")
    