from random import randint
class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        ano_nascimento = self.ano_atual - self.idade
        return ano_nascimento
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa.por_ano_nascimento('Igor', 1991)

#print(p1)
print(f'Nome: {p1.nome}\nIdade:{p1.idade}\nAno de Nascimento: {p1.get_ano_nascimento()}\nID: {p1.gera_id()}')
