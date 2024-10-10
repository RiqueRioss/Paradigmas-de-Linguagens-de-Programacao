public class ContaBancaria {

    private double saldo;
    private String titular;

    public double getSaldo() {
        return saldo;
    }
    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }
    public String getTitular() {
        return titular;
    }
    public void setTitular(String titular) {
        this.titular = titular;
    }

    public ContaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public void depositar(double dep){
        this.saldo += dep;
    }
    public void sacar(double sac){
        this.saldo -= sac;
    }
}
