public class Motor {
    public String getTipo() {
        return tipo;
    }

    private String tipo;
    private int potencia;

    public Motor(String tipo, int potencia){
        this.tipo = tipo;
        this.potencia = potencia;
    }

    public void ligar() {
        System.out.println("O motor está ligado.");
    }

    public void desligar() {
        System.out.println("O motor está desligado.");
    }
}
