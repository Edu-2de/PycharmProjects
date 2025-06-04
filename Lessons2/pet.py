import random
class AnimalEstimacao:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.estado = 'comendo'
        self.acao = [' ']

        if self.especie == 'cachorro' or self.especie == 'Cachorro':
            self.acao = ['latiu', ' ']
        elif self.especie == 'gato' or self.especie == 'Gato':
            self.acao = ['miou', ' ']
        else:
            self.acao = ['nadou', ' ']
    def comer(self):
        print(f'O animal {self.especie} do nome: {self.nome} comeu')
        self.estado = 'comendo'
    def dormir(self):
        print(f'O animal {self.especie} do nome: {self.nome} dormiu')
        self.estado = 'dormindo'
    def brincar(self):
        print(f'O animal {self.especie} do nome: {self.nome} brincou')
        self.estado = 'brincando'
    def listar(self):
        print(f'O animal {self.especie} do nome: {self.nome} da idade: {self.idade} anos, está: {self.estado} ')
        print(f'{random.choice(self.acao)}')

animal = AnimalEstimacao("Rex", "gato", 5)

animal.dormir()
animal.brincar()
animal.comer()
animal.listar()