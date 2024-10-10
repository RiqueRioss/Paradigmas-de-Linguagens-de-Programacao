public class Carro {
    String marca;
    String modelo;
    String ano;
    float velocidade;
    public void acelerar(int add){
        this.velocidade += add;
    }
    public void desacelerar(int add){
        this.velocidade -= add;
    }

    public void exibirVelocidade(){
        System.out.println("Velocidade atual do veículo: "+velocidade);
    }
}

