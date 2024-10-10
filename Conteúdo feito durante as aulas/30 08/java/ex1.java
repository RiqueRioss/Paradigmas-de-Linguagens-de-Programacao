// Exemplo de Vetor 2 em Java - calculando a média dos elementos do vetor
// mais a o maior elemento do vetor e o menor elemento do vetor.
public class ex1 {
    public void ex1(){
        funcoes funcoes = new funcoes();

        // Cria um vetor de 10 elementos inteiros
        int[] vetor = {5, 12, 7, 20, 15, 8, 3, 11, 6, 9};

        // Calcula a média, a maior valor e o menor
        int soma = 0;
        int maiorValor = vetor[0];
        int menorValor = vetor[0];

        for (int i=0; i<vetor.length; i++){
            soma += vetor[i];
            if (vetor[i] > maiorValor)
                maiorValor = vetor[i];
            if (vetor[i] < menorValor)
                menorValor = vetor[i];
        }

        double media = (double) soma / vetor.length;

        // Exibe os Resultados
        funcoes.mostraResultados(media, maiorValor, menorValor);
    }
}
