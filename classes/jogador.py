class Jogador():
    def __init__(self,nome,pontos):
        self.nome =  nome
        self.pontos = pontos
    def setPontos(self):
        self.pontos +=1
    def getPontos(self):
        return self.pontos