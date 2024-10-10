public class Main {
    public static void main(String[] args) {
        Cachorro cachorro = new Cachorro();
        cachorro.especie = "cachorro";
        cachorro.nome = "chorro";
        cachorro.emitir_som();

        Gato gato = new Gato();
        gato.especie = "gato";
        gato.nome = "to";
        gato.emitir_som();
    }
}