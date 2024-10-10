import java.util.ArrayList;
import java.util.List;

public class Empresa {
    private String nome;
    private List<Empregado> empregados;

    public Empresa(String nome){
        this.nome = nome;
        this.empregados = new ArrayList<>();
    }
    public void adicionaEmpregado(Empregado empreg){
        empregados.add(empreg);
    }
    public void listarEmpregados() {
        System.out.println("Empregados da empresa " + nome + ":");
        for (Empregado empregado : empregados) {
            empregado.exibirDetalhes();
        }
    }
}
