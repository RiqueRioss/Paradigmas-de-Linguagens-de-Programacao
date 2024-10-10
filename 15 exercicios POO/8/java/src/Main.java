public class Main {

    public static void main(String[] args) {
        Empresa enpesa = new Empresa("Presa");

        Empregado preg = new Empregado("Paulo", "Paulador", 99999);
        Empregado preg2 = new Empregado("Paulo2", "Paulador2", 999992);

        enpesa.adicionaEmpregado(preg);
        enpesa.adicionaEmpregado(preg2);

        enpesa.listarEmpregados();
    }
}