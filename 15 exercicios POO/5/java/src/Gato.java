public class Gato implements Animal{
    private String nome;
    private String especie;

    public Gato(String nome) {
        this.nome = nome;
    }
    @Override
    public String emitir_som() {
        return "MIAUU";
    }
}

