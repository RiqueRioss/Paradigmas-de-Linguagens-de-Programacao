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

cachorro = Cachorro("cachorro", "chorro")
cachorro.emitir_som()
