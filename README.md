# Raízes e Gráficos

Este é um projeto simples, desenvolvido para calcular as raízes de equações de primeiro e segundo grau e exibir seus gráficos. O objetivo principal é proporcionar um aprendizado prático sobre o uso de interfaces gráficas e gráficos em Python.

## Funcionalidade

Este programa tem como objetivo:

1. **Calcular as raízes** de uma equação do segundo grau da forma `ax² + bx + c = 0`, utilizando a fórmula de Bhaskara.
2. **Exibir um gráfico** da função `f(x) = ax² + bx + c`, destacando as raízes da equação no gráfico.

### Tipos de Raízes

- **Raízes Reais**: Quando o discriminante (`Δ = b² - 4ac`) é maior ou igual a zero, as raízes são reais e podem ser:
  - **Duas raízes distintas**, caso `Δ > 0`.
  - **Raiz única**, caso `Δ = 0`.

- **Raízes Complexas**: Quando `Δ < 0`, as raízes são complexas e serão exibidas no formato `x₁ = a + bi` e `x₂ = a - bi`.

### Como Usar

1. **Abrir a Interface**: Execute o programa e uma janela gráfica será aberta.
2. **Inserir os Coeficientes**: Na interface, insira os valores de `a`, `b` e `c` nos campos correspondentes. Esses valores representam os coeficientes da equação quadrática `ax² + bx + c = 0`.
3. **Calcular e Visualizar o Gráfico**: Ao clicar no botão "Calcular Raízes e Exibir Gráfico", o programa irá:
   - Calcular as raízes da equação.
   - Exibir o gráfico da função `f(x) = ax² + bx + c` com as raízes plotadas.
   
   Se as raízes forem complexas, o gráfico exibirá uma mensagem explicativa.

### Interface Gráfica

A interface foi desenvolvida utilizando a biblioteca `Tkinter` e permite a inserção dos coeficientes diretamente. O resultado, além de ser mostrado na interface com o cálculo das raízes, é apresentado visualmente em um gráfico gerado com `matplotlib`.

---

## Estrutura do Projeto

A estrutura do projeto é composta por quatro arquivos principais:

1. **`calc_raizes.py`**: Contém a função `calcular_raizes`, que calcula as raízes da equação quadrática (e linear, caso `a == 0`).
   
2. **`graficos.py`**: Responsável pela criação do gráfico da função `f(x) = ax² + bx + c` e pela exibição das raízes no gráfico.

3. **`interface.py`**: Implementa a interface gráfica utilizando `Tkinter`. O código permite que o usuário insira os coeficientes da equação e visualize o cálculo das raízes e o gráfico.

4. **`main.py`**: Arquivo principal que inicia a execução do programa e abre a interface gráfica.

---

## Ferramentas Utilizadas

Abaixo estão as principais linguagens e pacotes utilizados no desenvolvimento deste projeto:

### Linguagens

- **Python**: Linguagem de programação principal utilizada para desenvolver o código.
  
### Pacotes e Bibliotecas

- **Tkinter**: Biblioteca padrão de Python para criação de interfaces gráficas.
  
- **Matplotlib**: Biblioteca para criação de gráficos e visualizações em Python. Usada para gerar o gráfico da função `f(x) = ax² + bx + c`.

- **NumPy**: Utilizado para manipulação de arrays e cálculos numéricos (embora em uma forma simples no projeto, a biblioteca `NumPy` facilita operações como criação de vetores e cálculos em grande escala).

### Conceitos

- **Equação Quadrática**: A solução de equações do tipo `ax² + bx + c = 0` é resolvida utilizando a fórmula de Bhaskara.
  
- **Raízes Complexas e Reais**: O programa consegue lidar com as duas situações, dependendo do valor do discriminante `Δ`.

---

## Como Rodar o Projeto

Para rodar o projeto, siga as etapas abaixo:

### 1. Instalar Dependências

Primeiro, instale as dependências necessárias:

```bash
pip install matplotlib numpy

### 2. Rodar o Programa

Após instalar as dependências, execute o arquivo main.py para abrir a interface gráfica:

python main.py

Isso abrirá a janela para inserir os coeficientes e visualizar as raízes e o gráfico da equação.