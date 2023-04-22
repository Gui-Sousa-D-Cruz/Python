class Vendedor():
    def __init__(self, nome):
        self.nome= nome
        self.vendas=0
    def venda(self, vendas):
        self.vendas=vendas
    def meta(self,meta):
        self.meta = meta
        
    def info(self):
        print(f'''Informações sobre o vendedor
Nome do vendedor: {self.nome}
Vendas: {self.vendas}
Meta: {self.meta}''')
        if self.vendas >= self.meta:
            print(f'{self.nome} bateu a meta!')
        else:
            print(f'{self.nome} Não bateu a meta!')