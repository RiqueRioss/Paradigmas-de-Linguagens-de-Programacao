package main
import "fmt"

type Animal interface{
    EmitirSom() string
}

type Cachorro struct{
    nome string
}
func (c Cachorro) EmitirSom() string {
    return "AU AU"
}

type Gato struct {
    nome string
}
func (g Gato) EmitirSom() string {
    return "MIAU"
}

func emitirSons(animais []Animal){
    for _, animal := range animais {
        fmt.Println(animal.EmitirSom())
    }
}

func main() {
    cachorro := Cachorro{nome: "chorro"}

    gato := Gato{nome: "to"}

    animais := []Animal{cachorro, gato}

    emitirSons(animais)

}