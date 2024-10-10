public class Main {
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria("Henrique", 1000);
        System.out.println("Meu saldo atual: " + conta.getSaldo());
        System.out.println("Depositando 500 reais.");
        conta.depositar(500);
        System.out.println("Meu saldo atual: " + conta.getSaldo());
    }
}