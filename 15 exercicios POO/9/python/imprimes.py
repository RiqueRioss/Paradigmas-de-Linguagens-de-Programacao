from typing import Protocol

class Imprimivel(Protocol):
    def Imprimir(self) -> None:
        ...

class Relatorio:
    def __init__(self, texto: str):
        self.texto = texto
    
    def Imprimir(self) -> None:
        print(f"Relatório: {self.texto}")

class Contrato:
    def __init__(self, texto: str):
        self.texto = texto

    def Imprimir(self) -> None:
        print(f"Contrato entre: {self.texto}")

def imprimir_documento(documento: Imprimivel):
    documento.Imprimir()

relatorio1 = Relatorio("Análise.")
contrato1 = Contrato("Humano")

imprimir_documento(relatorio1)
imprimir_documento(contrato1)