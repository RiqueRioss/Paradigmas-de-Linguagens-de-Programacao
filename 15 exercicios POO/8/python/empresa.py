class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.empregados = []
    
    def adicionar_empregado(self, empregado):
        self.empregados.append(empregado)

    def listar_empregados(self):
        print(f"Empregados da empresa {self.nome}:")
        for empregado in self.empregados:
            empregado.exibir_detalhes()

class Empregado:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    
    def exibir_detalhes(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}")

presa = Empresa("P P Produções")
prego1 = Empregado("Humano", "Vivo", 88888)
prego2 = Empregado("Criatura", "Mortal", 77777)

presa.adicionar_empregado(prego1)
presa.adicionar_empregado(prego2)

presa.listar_empregados()