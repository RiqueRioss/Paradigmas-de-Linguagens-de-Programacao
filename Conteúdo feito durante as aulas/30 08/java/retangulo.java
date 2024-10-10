public class retangulo {
    private double comprimento;
    private double largura;
    public retangulo(double comp, double lar){
        this.comprimento = comp;
        this.largura = lar;
    }
    public double calcularArea(){
        return comprimento*largura;
    }
    public double calcularPerimetro(){
        return (comprimento+largura)*2;
    }
    public void ex3(){
        // Criando uma instância da classe Retângulo
        retangulo ret = new retangulo(200,300);
        System.out.println("Área: " + ret.calcularArea());
        System.out.println("Perímetro: " + ret.calcularPerimetro());
    }
}
