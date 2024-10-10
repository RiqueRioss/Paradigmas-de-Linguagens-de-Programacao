package main
import "fmt"

type Empresa struct{
    nome string
    empregados []Empregado
}
type Empregado struct{
    nome string
    cargo string
    salario float64
}

func (e Empregado) ExibirDetalhes() {
	fmt.Printf("Nome: %s, Cargo: %s, Salário: R$%.2f\n", e.nome, e.cargo, e.salario)
}

func (e *Empresa) AdicionarEmpregado(empregado Empregado) {
	e.empregados = append(e.empregados, empregado)
}

func (e Empresa) ListarEmpregados() {
	fmt.Printf("Empregados da empresa %s:\n", e.nome)
	for _, empregado := range e.empregados {
		empregado.ExibirDetalhes()
	}
}

func main() {
    empresa := Empresa{nome: "TTT"}
    emprega1 := Empregado{nome: "Deus", cargo: "O melhor", salario: 66666}
    emprega2 := Empregado{nome: "SSSS", cargo: "O pior", salario: 55555}

    empresa.AdicionarEmpregado(emprega1)
    empresa.AdicionarEmpregado(emprega2)

    empresa.ListarEmpregados()
}