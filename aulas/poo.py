class Cachorros:
    def __init__(self, nome, cor, idade, tamanho):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.tamanho = tamanho
    def latir(self):
        print('au au')
    def correr(self):
        print(f'{self.nome} está correndo!')

c1 = Cachorros('Lola', 'preto', '3', 'pequeno')
c2 = Cachorros('Puppy', 'preto', '6', 'médio')
c1.latir()
c1.correr()
c2.correr()
c2.latir()