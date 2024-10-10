package main

import "fmt"

// Definindo a struct Carro
type ContaBancaria struct {
	Titular  string
	Saldo float64
}

func (c *ContaBancaria) depositar(dep float64){
	c.Saldo += dep
}
func (c *ContaBancaria) sacar(sac float64){
	c.Saldo -= sac
}

func main() {
	conta := ContaBancaria{
		Titular: "Henrique",
		Saldo: 1000,
	}
	fmt.Println("Meu nome: ", conta.Titular)
	fmt.Println("Meu saldo: ", conta.Saldo)
	conta.depositar(500)
	fmt.Println("Meu saldo após depósito de 500: ", conta.Saldo)

	
}