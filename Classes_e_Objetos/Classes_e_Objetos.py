jogador_loteria={
    'nome':'Pedro',
    'numeros':(13,4,54,23,67,82)
}
jogador_loteria2={
    'nome':'Pedro',
    'numeros':(13,4,54,23,67,82)
}
print(jogador_loteria==jogador_loteria2)
#Classe é um modelo ou uma representação de um objeto
#Objeto é uma instância de classe
class jogadorLoteria:
    def __init__(self,nome):
        self.nome=nome
        self.numeros=(13,4,54,23,67,82)
    def total(self):
        sum(self.numeros)
        
jogador_1=jogadorLoteria('Ana')
jogador_2=jogadorLoteria('Felipe')
print(jogador_1.nome)
print(jogador_2.nome)
print(jogador_1.numeros)
print(jogador_1.total())
print(jogador_1==jogador_2)