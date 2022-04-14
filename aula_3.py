'''
CARACTERÍSTICAS
- 1991 por Guido Van Rossum
- Linguagem interpretada
- Prioriza a legibilidade do código
- Tipagem dinâmica
- Multiparadigma
- Versátil e de uso geral
- Computação científica
- Licença livre aprovada pelo OSI e compatível com GPL
- Desenvolvimento comunitário, aberto e gerenciado pela Python Software Foundation

1º lugar na Index Tiobe (abril 2022)
https://www.tiobe.com/tiobe-index/

TRILHAS
- Inteligência Artificial
- Data Science
- Machine Learning
- Internet das Coisas (IoT)
MicroPython
- Desenvolvimento Web
- Jogos (PyGame)
- Mobile (KiVy)

PRINCIPAIS FRAMEWORS WEB
- Flask
- Jinja
- Django
- Web2py

ALGUMAS BIBLIOTECAS
- NumPy: processamento número com vetores e matrizes.
- SciPy: processamento de sinasis, equações diferenciais, álgebra linear, otimização, funções matemáticas e estatística.
- Pandas: combina alto desempenho de processamento de vetores da NumPy com manipulação de planilhas de banco de dados relacionais.
- Matplotlib: mais popular biblioteca para visualização de dados bidimensionais e plotagens.
- Scikit-learn e TensorFlow: ferramenta para machine learning.
- Stasmodels: estatística clássica, regressão linear, séries temporais.

AMBIENES DE DESENVOLVIMENTO
- Ipython e Jupyter: Ipython é um interpretador interetivo (Kernel), 
sendo o Jupyter notebook um aplicativo web que permite criar e compartilhar documentos com códito ativo.
- Spyder (IDE que acompanha o projeto Anaconda): https://www.spyder-ide.org/
Ver depois: https://www.anaconda.com/
 
 OUTRAS IDES
 - PyDev: incluído na plataforma Eclipse (gratuito)
 - Python Tools para Visual Studio
 - Komodo
 - Pycharm: https://www.jetbrains.com/pycharm/download/download-thanks.html
 
 PROJETO ANACONDA
 - Ferramentas, bibliotecas e utilitários para construir, distribuir, instalar, atualizar e gerenciar softwares.
 - Integração com outras linguagens e ambientes.
 - Construído por cientistas para cientistas.
 - Mais de 20 milhões de usuários em todo o mundo.
 
VARIÁVEIS
São espaços na memória para a realização de operações.
Ex.: soma = valor1 + valor2 

Todas as variáveis são consideradas um objeto em python

Cada variável possui um endereço de memória, o nome atribuído a ela trata-se apenas de uma referência para o desenvolvedor. 
Ao estudar uma nova linguagem de programação, consulte sempre a documentação para verificar quais são os tipos de variáveis disponíveis
'''

#TIPOS DE VARIÁVEIS (ESTRUTURAS DE DADOS)

#EXEMPLO 1

#int: números inteiros
valorInt = 1
print(("valorInt é uma variável do tipo {}".format(type(valorInt))))

#float: números reais (ponto flutuante)
valorFloat = 1.576
print(("valorFloat é uma variável do tipo {}".format(type(valorFloat))))

#str (string): texto
valorString = "nome"
print(("valorString é uma variável do tipo {}".format(type(valorString))))

#bool: valores booleanos true ou false (tipos lógicos)
valorBool = True
print(("valorBool é uma variável do tipo {}".format(type(valorBool))))

#complex: número complexo
#valorComplex = 5gh
#print(("valorComplex é uma variável do tipo {}".format(type(valorComplex))))

#set: conjunto de elementos (list)
valorList = ("Emerson", 1, 1.576)
print(("valorList é uma variável do tipo {}".format(type(valorList))))

#tuple: semelhantes ao tipo set, entretanto, imutável
#valorTuple = tuple.(valorList)
#print(("valorTuple é uma variável do tipo {}".format(type(valorTuple))))

#dict: elementos que serão recuperados por uma chave
valorDict = {'Emerson': 1}
print(("valorDict é uma variável do tipo {}".format(type(valorDict))))

#none: valor do tipo nulo
valorNulo = None
print(("valorNulo é uma variável do tipo {}".format(type(valorNulo))))
 
#EXEMPLO
ano = 1989
nome = "Luke Skywalker"
saldo = 50.30
print(("O tipo de variável ano é {}".format(type(ano)))) #int
print(("O tipo de variável nome é {}".format(type(nome)))) #str
print(("O tipo de variável saldo é {}".format(type(saldo)))) #float

'''
OPERADORES

OPERADORES ARITMÉTICOS
+ soma
- subtração
* multiplicação
/ divisão
// divisão (descarta o resto fracionário)
** potência

OPERADORES RELACIONAIS
> maior
>= maior igual
< menor
<= menor igual
== igual
!= diferente

OPERADORES LÓGICOS (OPERAÇÕES BOOLEANAS 0 OU 1)
& lógico E (and)
│ logico OU (or)
^ lógico OU exclusivo (xor)

FUNÇÕES print() e input ()
print: utilizada para exibir dados no console (saída), semelhante ao printf() no C e o System.out.print() no Java.
input: utilizada para "capturar" daos (entrada), semelhante ao scanf() no C e ao Scanner() no Java.
obs.: a função input() faz com que qualquer dado digitado pelo usuário seja tratado como um texto. Para manipular esse dado como número, é preciso fazer uma conversão.

Entrada = dados
Processamento = operação
Saída = informação

Lembrete: informações são sempre os dados trabalhados

'''
#EXEMPLO
print("CALCULADORA")

'''entrada = dados'''
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

'''processamento = operação'''
soma = valor1 + valor2
subtração = valor1 - valor2
multiplicação = valor1 * valor2
divisão = valor1 / valor2

'''saída = informação'''
print("Resultado da soma: {}".format(soma))
print("Resultado da subtração: {}".format(subtração))
print("Resultado da multiplicação: {}".format(multiplicação))
print("Resultado da divisão: {:.2f}".format(divisão)) # {:.2f} = determina a quantidade de casa decimais depois do processamento#

'''
FORMATAÇÃO
/t paragrafo
\n pular linha
{}.format - Para a função print não concatenar as variáveis é preciso utilizar o método .format para exibir um texto no local desejado.
Para isso, utiliza-se as chaves como um marcador e a função format para preencher esse marcador vom o valor a ser exibido.
'''

#EXEMPLO
print("\t\t\t\t\t\tCENTRALIZAR\n\n\n\n\n")
print("fim")

'''
DESVIOS CONDICIONAIS
Ao construir qualquer algoritmo é preciso considerar que alguns dados são temporários, mas importantes para tomada de decisão.
Ex.: uma página de internet indicada para maiores de 18 anos.


'''
