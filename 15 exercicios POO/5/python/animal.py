class Animal:
    def __init__(self, especie, nome):
        self.especie = especie
        self.nome = nome

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "AU AU"

class Gato(Animal):
    def emitir_som(self):
        return "MIAU"

def emitir_sons(animais):
    for animal in animais:
        print(f"O {animal.nome} ({animal.especie}) faz: {animal.emitir_som()}")

cachorro = Cachorro("cachorro", "chorro")
gato = Gato("gato", "miau miau")

animais = [cachorro, gato]

emitir_sons(animais)