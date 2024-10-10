public class Main {

    public static void main(String[] args) {

        Carro carrinho = new Carro("Lindo", "Largo");

        Motor mt = carrinho.getMotor();

        System.out.println("Tipo do motor do veículo: " + mt.getTipo());
    }
}