package main
import "fmt"

type Motor struct{
    tipo string
    potencia int
}
func (m Motor) Ligar(){
    fmt.Println("Motor ligado.")
}

type Carro struct{
    marca string
    modelo string
    motor Motor
}

func (c Carro) TipoMotor() {
	fmt.Printf("O tipo do motor é: %s\n", c.motor.tipo)
}

func main() {
    carro := Carro{
		marca:  "Toyora",
		modelo: "corolla",
		motor:  Motor{tipo: "Gasolina", potencia: 150},
	}

    carro.TipoMotor()

}