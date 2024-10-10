public class Cachorro implements Animal{
    private String nome;
    private String especie;

    public Cachorro(String nome) {
        this.nome = nome;
    }
    @Override
    public String emitir_som() {
        return "AU AU";
    }
}
