public class Main {

    public static void main(String[] args) {
        Calculadora calc = new Calculadora();
        int a = 1;
        int b = 2;
        double c = 1.5;
        double d = 2.5;
        float e = 4;
        float f = 5;

        System.out.println(calc.somar(a,b));
        System.out.println(calc.somar(c,d));
        System.out.println(calc.somar(e,f));
    }
}