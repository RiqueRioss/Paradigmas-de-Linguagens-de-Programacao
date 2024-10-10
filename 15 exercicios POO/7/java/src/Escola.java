import java.util.ArrayList;
import java.util.List;

public class Escola {
    private String nome;
    private List<Professor> professores;

    public Escola(String nome) {
        this.nome = nome;
        this.professores = new ArrayList<>();
    }

    public void adicionaProfessor(Professor prof){
        professores.add(prof);
        prof.adicionaEscola(this);
    }
}
