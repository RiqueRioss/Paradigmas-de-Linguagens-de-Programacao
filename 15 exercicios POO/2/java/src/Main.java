public class Main {
    public static void main(String[] args) {
        Carro carrinho = new Carro();
        carrinho.marca = "Bonito";
        carrinho.modelo = "Grande";
        carrinho.ano = "1666";

        System.out.println(
                "Marca do veículo: "+carrinho.marca+
                        "\nModelo do veículo: "+carrinho.modelo+
                        "\nAno do veículo: "+carrinho.ano
        );

        carrinho.velocidade = 100;
        carrinho.exibirVelocidade();
        System.out.println("Desacelerando.");
        carrinho.desacelerar(10);
        carrinho.exibirVelocidade();
    }
}