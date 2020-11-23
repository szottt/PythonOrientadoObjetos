class Produto:

    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual /100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$',''))

        self._preco = valor


desconto = 10
p1 = Produto('CAMISETA', 50)
p1.desconto(desconto)
print(f'{p1.nome} com o desconto de R${desconto} fica no valor de R${p1.preco}')

p2 = Produto('CANECA', 'R$15')
p2.desconto(desconto)
print(f'{p2.nome} com o desconto de R${desconto} fica no valor de R${p2.preco}')