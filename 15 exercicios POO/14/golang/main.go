package main

import "fmt"

func SomarDoisInteiros(a int, b int) int {
	return a + b
}
func SomarDoisFloats(a float64, b float64) float64 {
	return a + b
}
func SomarTresInteiros(a int, b int, c int) int {
	return a + b + c
}
func SomarTresFloats(a float64, b float64, c float64) float64 {
	return a + b + c
}

func main() {
	fmt.Println("Soma de dois inteiros:", SomarDoisInteiros(1, 2))
	fmt.Println("Soma de dois floats:", SomarDoisFloats(1.5, 2.3))
	fmt.Println("Soma de três inteiros:", SomarTresInteiros(1, 2, 3))
	fmt.Println("Soma de três floats:", SomarTresFloats(1.5, 2.3, 3.2))
}
