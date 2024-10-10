import java.util.ArrayList;
import java.util.List;

public class Professor {
    private String nome;
    private List<Escola> escolas;

    public Professor(String nome) {
        this.nome = nome;
        this.escolas = new ArrayList<>();
    }

    public void adicionaEscola(Escola escola){
        escolas.add(escola);
        escola.adicionaProfessor(this);
    }
}
