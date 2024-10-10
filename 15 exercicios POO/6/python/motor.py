class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    def ligar(self):
        print("O motor está ligado.")
    def desligar(self):
        print("O motor está desligado.")

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("Gasolina", 150)
    def ligar(self):
        self.motor.ligar()
        print("O carro está pronto para rodar.")
    def desligar(self):
        self.motor.desligar()
        print("O carro foi desligado.")

carro = Carro("Toyora", "corolla")
carro.ligar()
carro.desligar()
