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

## [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)
O código resolve o problema de mesclar k listas encadeadas ordenadas em uma única lista, utilizando o paradigma de dividir e conquistar. Primeiro, verifica se a lista de entrada está vazia e, caso não esteja, combina as listas aos pares em um laço, reduzindo pela metade a quantidade a cada iteração. Para mesclar dois pares, utiliza a função recursiva mergeTwoLists, que compara os nós e conecta o menor ao próximo resultado recursivo. O processo se repete até restar apenas uma lista resultante. Essa abordagem garante desempenho eficiente com complexidade O(N log k), onde N é o número total de nós e k é o número de listas iniciais.

## [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)
O código resolve o problema de encontrar a subarray com a maior soma em um array de inteiros, usando dividir e conquistar. A função findMaxSubArray divide o array ao meio recursivamente até que reste apenas um elemento. Em cada divisão, calcula a maior soma do lado esquerdo, do lado direito e uma soma cruzando o centro, utilizando a função auxiliar findCrossMax, que percorre os dois lados a partir do meio acumulando os maiores valores. Por fim, retorna o maior entre os três resultados. Essa abordagem possui complexidade O(n log n).


## [1569. Number of Ways to Reorder Array to Get Same BST](https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/) - Difícil

![Print da Resolução 1569](/Questoes/assets/img1569.jpg)

## [2343. Query Kth Smallest Trimmed Number](https://leetcode.com/problems/query-kth-smallest-trimmed-number/description/) - Média 

![Print da Resolução 2343](/Questoes/assets/img2343.jpg)
