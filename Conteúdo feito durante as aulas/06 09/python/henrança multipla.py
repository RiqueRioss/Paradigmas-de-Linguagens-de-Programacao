class Animal:
    def __init__(self, nome):
        self.nome = nome
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def amamentar(self):
        print(f"{self.nome} está amamentando.")

class Ave(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    def voar(self):
        print(f"{self.nome} está voando.")

class Morcego(Mamifero, Ave):
    def __init__(self, nome):
        super().__init__(nome)
    def emitir_som(self):
        return "sssssssss"

morcego = Morcego("cego")
morcego.emitir_som()
morcego.amamentar()
morcego.voar()
