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

CONTROLE DE FLUXO
- Comandos utilizados para testar diferentes situaçõe e executar instruções definidas pelo programador.
- Os comandos mais utilizados são: IF, ELIF e ELSE

- IF: verifca o valor a ser testado e caso seja verdadeiro executa a instrução, caso seja falso não faz absolutamente nada.
- ELSE: verifica o valor a ser testado e caso seja verdadeiro executa a instrução, caso seja falso executa a outra instrução.
- ELIF: esta forma permite vários testes diferentes, ou seja, verifica o valor a ser testado e caso seja verdadeiro executa a instrução.
Caso seja falso testa a próxima condição, sendo a última á cláusula else.
'''

#EXEMPLO USANDO SOMENTE IF
valorInt = 5
valorFloat = 1.5

if valorInt == valorFloat:
    print("Os valores são correspondentes")

if valorInt != valorFloat:
    print("Os valores não são correspondentes")
  
#EXEMPLO USANDO IF, ELIF E ELSE
valorInt = 5
valorFloat = 5.7

if valorInt == valorFloat:
    print("Os valores são correspondentes")

elif valorInt > valorFloat:
    print("o valor 5 é maior que o valor 1.5")
    
else:
    print("O valor 1.5 é menor que o valor 5")
  
  '''
  Utilizar o IF - ELSE é mais performático do que múltiplos IF; quando a condição é verdadeira executa o tracho de código e ignora todos os demais. 
  Entretanto, em algumas situações pode ser interessante utilizar múltiplos IF, pois a condição IF - ELSE é mutuamente excludente.
  '''


