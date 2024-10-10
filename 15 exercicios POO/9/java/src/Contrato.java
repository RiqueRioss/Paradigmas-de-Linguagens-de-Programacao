public class Contrato implements Imprimivel{
    private String texto;

    public Contrato(String partes) {
        this.texto = partes;
    }

    @Override
    public void imprimir(){
        System.out.println("Contrato: " + texto);
    }
}
