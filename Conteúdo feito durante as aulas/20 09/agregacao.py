class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = None
    
    def adicionar_endereco(self, endereco):