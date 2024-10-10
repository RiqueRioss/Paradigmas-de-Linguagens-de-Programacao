public class Main {

    public static void emitirSons(Animal[] animais) {
        for (Animal animal : animais) {
            System.out.println(animal.emitir_som());
        }
    }

    public static void main(String[] args) {
        Cachorro cachorro = new Cachorro("chorro");
        Gato gato = new Gato("to");

        Animal[] animais = {cachorro, gato};

        emitirSons(animais);
    }
}