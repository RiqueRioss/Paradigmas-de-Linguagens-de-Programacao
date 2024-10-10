public class Carro {
    private String marca;
    private String modelo;
    private Motor motor;

    public Carro(String marca, String modelo) {
        this.marca = marca;
        this.modelo = modelo;
        this.motor = new Motor("Gasolina", 150);
    }
    public Motor getMotor(){
        return this.motor;
    }
}
