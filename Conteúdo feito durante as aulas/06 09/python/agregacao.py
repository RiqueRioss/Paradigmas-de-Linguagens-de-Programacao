class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = None

    def adicionar_endereco(self, endereco):
        self.endereco = endereco

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
        if self.endereco:
            print("Endereço: ")
            self.endereco.mostrar_endereco()
        else:
            print("Endereço não disponível.")

class Endereco:
    def __init__(self, rua, cidade, estado, cep):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def mostrar_endereco(self):
        print(f"Rua: {self.rua}, Cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}")

class Empresa:
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.funcionarios = []

    def contratar_funcionarios(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"Funcionários da empresa {self.nome}")
        for funcionario in self.funcionarios:
            print(funcionario.nome)

#exemplo de uso
endereco1 = Endereco("Av. Principal", "Codade A", "Estado A", "11236-342")
pessoa1 = Pessoa("Maria", 25)
pessoa1.adicionar_endereco(endereco1)

endereco2 = Endereco("Av. dois", "Codade B", "Estado Y", "99999-342")
pessoa2 = Pessoa("JÕAO", 25)
pessoa2.adicionar_endereco(endereco2)

empresa = Empresa("Empresa ABC", "12345457")
empresa.contratar_funcionarios(pessoa1)
empresa.contratar_funcionarios(pessoa2)

empresa.listar_funcionarios()
