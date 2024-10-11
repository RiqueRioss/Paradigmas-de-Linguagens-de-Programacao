class Calculadora:

    def soma2Inteiros(self, a: int, b: int) -> int:
        return a+b
    def soma2Floats(self, a: float, b: float) -> float:
        return a+b
    def soma3Inteiros(self, a: int, b: int, c: int) -> int:
        return a+b+c
    def soma3Floats(self, a: float, b: float, c: float) -> float:
        return a+b+c
    
calculadora = Calculadora()

print("Soma de dois inteiros: ", calculadora.soma2Inteiros(1, 2))
print("Soma de dois floats: ", calculadora.soma2Floats(1.3, 2.23))
print("Soma de três inteiros: ", calculadora.soma3Inteiros(1, 2, 3))
print("Soma de três floats: ", calculadora.soma3Floats(1.1, 2.2, 3.3))