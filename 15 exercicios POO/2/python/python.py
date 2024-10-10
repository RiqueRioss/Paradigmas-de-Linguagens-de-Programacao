class Carro:

    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
    
    def acelerar(self, add):
        self.velocidade += add
    
    def desacelerar(self, add):
        self.velocidade -= add
    
    def exibirVelocidade(self):
        print("Velocidade do veículo: ", carrinho.velocidade)
    
carrinho = Carro("Bonito", "Grande", 166, 100)
print("Marca do veículo: ", carrinho.marca)
print("Modelo do veículo: ", carrinho.modelo)
print("Ano do veículo: ", carrinho.ano)

carrinho.exibirVelocidade()
print("Desacelerando")
carrinho.desacelerar(10)
carrinho.exibirVelocidade()

