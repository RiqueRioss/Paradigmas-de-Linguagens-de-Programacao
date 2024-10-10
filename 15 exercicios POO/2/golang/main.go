package main

import "fmt"

// Definindo a struct Carro
type Carro struct {
	Marca  string
	Modelo string
	Ano    int
	Velocidade float64
}

func (c *Carro) Acelerar(add float64){
	c.Velocidade += add
}

func (c *Carro) Desacelerar(add float64){
	c.Velocidade -= add
}

func (c *Carro) ExibirVelocidade() {
	fmt.Println("Velocidade do veículo:", c.Velocidade)
}

func main() {
	carrinho := Carro{
		Marca:  "Bonito",
		Modelo: "Grande",
		Ano:    166,
		Velocidade: 100,
	}

	fmt.Println("Marca do veículo:", carrinho.Marca)
	fmt.Println("Modelo do veículo:", carrinho.Modelo)
	fmt.Println("Ano do veículo:", carrinho.Ano)

	carrinho.ExibirVelocidade()
	fmt.Println("Desacelerando.")
	carrinho.Desacelerar(10)
	carrinho.ExibirVelocidade()
}