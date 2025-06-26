# Dividir e Conquistar - PA

**Número da Lista**: 4<br>
**Conteúdo da Disciplina**: Dividir e Conquistar<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 20/2015868 |  Alexandre Lema Xavier Júnior |
| 21/1039671  |  Pedro Lopes da Cunha |

## Sobre 
Resolução de questões do LeetCode (2 difíceis e 2 médias) pelos integrantes do grupo com o objetivo de demonstrar o conhecimento adquirido nesse módulo (Dividir e Conquistar) da disciplina.

## Questões

|Questão | Dificuldade |
| -- | -- |
| [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/) | Difícil |
| [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/) | Média |
| [1569. Number of Ways to Reorder Array to Get Same BST](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/) |   Difícil |
| [2343. Query Kth Smallest Trimmed Number](https://leetcode.com/problems/query-kth-smallest-trimmed-number/description/) |   Média |

## Screenshots

## [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/) - Difícil
O código resolve o problema de mesclar k listas encadeadas ordenadas em uma única lista, utilizando o paradigma de dividir e conquistar. Primeiro, verifica se a lista de entrada está vazia e, caso não esteja, combina as listas aos pares em um laço, reduzindo pela metade a quantidade a cada iteração. Para mesclar dois pares, utiliza a função recursiva mergeTwoLists, que compara os nós e conecta o menor ao próximo resultado recursivo. O processo se repete até restar apenas uma lista resultante. Essa abordagem garante desempenho eficiente com complexidade O(N log k), onde N é o número total de nós e k é o número de listas iniciais.

![Print da Resolução 23](/Questoes/assets/img23.png)

## [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/) - Média
O código resolve o problema de encontrar a subarray com a maior soma em um array de inteiros, usando dividir e conquistar. A função findMaxSubArray divide o array ao meio recursivamente até que reste apenas um elemento. Em cada divisão, calcula a maior soma do lado esquerdo, do lado direito e uma soma cruzando o centro, utilizando a função auxiliar findCrossMax, que percorre os dois lados a partir do meio acumulando os maiores valores. Por fim, retorna o maior entre os três resultados. Essa abordagem possui complexidade O(n log n).

![Print da Resolução 53](/Questoes/assets/img53.png)


## [1569. Number of Ways to Reorder Array to Get Same BST](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/) - Difícil
A questão pede para encontrar quantas maneiras diferentes é possível reordenar um vetor de forma que, ao inserir os elementos na nova ordem em uma árvore binária de busca, o resultado seja exatamente o mesmo da árvore construída com a ordem original. Para resolver isso utilizei o algoritmo de dividir e conquistar. A ideia é separar os elementos em dois grupos: os que iriam para a subárvore esquerda (menores que a raiz) e os da direita (maiores que a raiz). A função é chamada recursivamente para cada lado, e o número de formas de intercalar os elementos das duas subárvores é calculado por meio de combinações. No final, o número total de reordenações possíveis que mantêm a mesma árvore binária de busca é retornado, descontando a ordem original.
![Print da Resolução 1569](/Questoes/assets/img1569.jpg)

## [2343. Query Kth Smallest Trimmed Number](https://leetcode.com/problems/query-kth-smallest-trimmed-number/description/) - Média 
A questão trata de um vetor composto por strings numéricas e uma lista de consultas queries. Cada consulta pede para recortar os últimos dígitos de cada número, ordenar esses números recortados e retornar a posição original do k-ésimo menor número. Utilizei o algoritmo Merge Sort, que aplica dividir e conquistar ao ordenar manualmente os números recortados com base em seu valor e, em caso de empate, pela posição original. Cada consulta recorta os números conforme o valor de trim, ordena as tuplas (recorte, índice) com Merge Sort e retorna a posição do k-ésimo menor recorte. O resultado final é uma lista com as posições correspondentes de todas as consultas.
![Print da Resolução 2343](/Questoes/assets/img2343.jpg)
