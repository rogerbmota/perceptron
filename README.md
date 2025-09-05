# Atividade Prática – Disciplina de Inteligência Artificial - UNIBH

Este repositório contém o código e as respostas para a atividade prática sobre o Perceptron.

---

## 1. Conceito

Explique, com suas palavras, o que é um Perceptron e qual a sua importância histórica para o desenvolvimento da Inteligência Artificial.

Pelo que entendi, o Perceptron é o modelo mais básico de um neurônio artificial. Ele foi desenvolvido por Frank Rosenblatt e funciona de forma bem simples: recebe várias entradas, cada uma com um peso, que representa sua importância, soma tudo e, se o resultado atingir um certo limite, ele ativa e retorna 1. Se não, ele retorna 0. A importância histórica dele é gigante, pois foi um dos primeiros algoritmos que conseguia aprender com dados. A ideia de que uma máquina poderia ajustar seus próprios pesos para classificar informações corretamente, deu o pontapé inicial para o campo das redes neurais, que usamos hoje em tecnologias muito mais complexas.

---

## 2. Funcionamento

O Perceptron é considerado um classificador linear. O que isso significa? Quais são as limitações desse tipo de modelo?

Ele é chamado de classificador linear porque, na prática, ele só consegue separar dados em duas categorias se for possível traçar uma única linha reta entre elas. Essa é justamente a sua maior limitação. Se os dados não forem lineares, o Perceptron simplesmente não consegue encontrar uma solução.

---

## 3. Código

Ao analisar o código que você executou, quais foram as etapas principais do processo de treinamento do Perceptron?

Analisando o código da atividade, percebi que ele não mostra o processo de treinamento, e sim o de predição. Ou seja, como um Perceptron já treinado calcula um resultado, não sendo possível inserir posteriormente imputs no terminal. Os passos que o código executa são: A primeira parte do código multiplica cada valor de entrada pelo seu respectivo peso e, no final, soma um valor de bias. Isso gera um único número que representa a combinação das entradas. Esse número é então usado para tomar a decisão final. O código usa uma função que se a soma for positiva ou zero, a saída é 1; se for negativa, a saída é 0. É isso que transforma o cálculo em uma classificação.

---

## 4. Aplicação prática

Dê um exemplo real em que o uso de um modelo simples como o Perceptron poderia ser útil. Justifique sua escolha.

Verificar peças em uma fábrica. Podemos usar um Perceptron para decidir na hora se um parafuso que acabou de ser fabricado está "Aprovado" (1) ou "Com Defeito" (0).  
Justificativa: É uma boa escolha porque a regra para aprovar uma peça é simples. O Perceptron recebe duas medidas básicas, como o comprimento e o peso do parafuso. Se a peça for muito grande, pequena, leve ou pesada, ela é rejeitada. O modelo é perfeito para isso, pois aprende essa questão entre o bom e o ruim de forma muito eficiente. Além disso, ele é extremamente rápido e leve, ideal para o ritmo de uma fábrica, onde as decisões precisam ser instantâneas.
