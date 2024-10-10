package main
import "fmt"

type Animal struct{
    especie string
    nome string
}
func (a Animal) EmitirSom() string{
    return ""
}

type Cachorro struct{
    Animal
}

func (c Cachorro) EmitirSom() string {
    return "AU AU"
}

type Gato struct {
    Animal
}

func (g Gato) EmitirSom() string {
    return "MIAU"
}

func main() {
    cachorro := Cachorro{Animal{"cachorro", "chorro"}}
    fmt.Println(cachorro.EmitirSom()) // AU AU

    gato := Gato{Animal{"gato", "miau"}}
    fmt.Println(gato.EmitirSom()) // MIAU
}