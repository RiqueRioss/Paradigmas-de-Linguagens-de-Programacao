package main
import "fmt"

type Imprimivel interface{
    Imprimir()
}

type Relatorio struct{
    texto string
}
func (r Relatorio) Imprimir(){
    fmt.Println("Relatório: ", r.texto)
}

type Contrato struct{
    texto string
}
func (c Contrato) Imprimir(){
    fmt.Println("Contrato: ", c.texto)
}

func main() {

    var relatorio Imprimivel
    rel := Relatorio{texto: "Análise-"}
    relatorio = rel

    var contrato Imprimivel
    con := Contrato{texto: "Sujeito bom"}
    contrato = con

    relatorio.Imprimir()
    contrato.Imprimir()


}