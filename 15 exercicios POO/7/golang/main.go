package main
import "fmt"

type Escola struct{
    nome string
    professores []*Professor
}

type Professor struct{
    nome string
    escolas []*Escola
}

func (esc *Escola) adicionarProfessor(pro *Professor){
    esc.professores = append(esc.professores, pro)
    pro.adicionarEscola(esc)
}
func (pro *Professor) adicionarEscola(esc *Escola){
    pro.escolas = append(pro.escolas, esc)
    esc.adicionarProfessor(pro)
}

func main() {
    eescola := &Escola{nome: "eescola"}
    pofessor := &Professor{nome: "ssor"}

    eescola.adicionarProfessor(pofessor)
}