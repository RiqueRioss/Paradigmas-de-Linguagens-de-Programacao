class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.escolas = []

    def adicionarEscola(self, esc):
        self.escolas.append(esc)
        esc.adicionarProfessor(self)

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []
    
    def adicionarProfessor(self, pro):
        self.professores.append(pro)
        pro.adicionarEscola(self)

eescola = Escola("Eeeeescola")
pofesor = Professor("Posor")

eescola.adicionarProfessor(pofesor)