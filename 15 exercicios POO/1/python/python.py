class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
carrinho = Carro("Bonito", "Grande", 166)
print("Marca do veículo: ", carrinho.marca)
print("Modelo do veículo: ", carrinho.modelo)
print("Ano do veículo: ", carrinho.ano)