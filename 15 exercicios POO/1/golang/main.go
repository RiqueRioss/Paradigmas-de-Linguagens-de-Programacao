package main

import "fmt"

// Definindo a struct Carro
type Carro struct {
	Marca  string
	Modelo string
	Ano    int
}

func main() {
	// Criando uma instância de Carro
	carrinho := Carro{
		Marca:  "Bonito",
		Modelo: "Grande",
		Ano:    166,
	}

	// Imprimindo os atributos do carro
	fmt.Println("Marca do veículo:", carrinho.Marca)
	fmt.Println("Modelo do veículo:", carrinho.Modelo)
	fmt.Println("Ano do veículo:", carrinho.Ano)
}