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
 
 
 
 

DESVIOS CONDICIONAIS
Ao construir qualquer algoritmo é preciso considerar que alguns dados são temporários, mas importantes para tomada de decisão.
Ex.: uma página de internet indicada para maiores de 18 anos.

TIPOS DE VARIÁVEIS
int: números inteiros
float: números reais (ponto flutuante)
complex: número complexo
bool: valores lógicos
str (string): texto

Obs.: ao estudar uma nova linguagem de programação, consulte sempre a documentação para verificar quais são os tipos de variáveis disponíveis
'''

#EXEMPLO: TIPOS DE VARIAVEIS

ano = 1989
nome = "Luke Skywalker"
saldo = 50.30
print(("O tipo de variável ano é {}".format(type(ano)))) #int
print(("O tipo de variável nome é {}".format(type(nome)))) #str
print(("O tipo de variável saldo é {}".format(type(saldo)))) #float
