public class Relatorio implements Imprimivel{
    private String texto;

    public Relatorio(String texto){
        this.texto = texto;
    }

    @Override
    public void imprimir(){
        System.out.println("Relatório: " + texto);
    }
}
