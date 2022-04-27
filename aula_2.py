#ATRIBUIR VARIÁVEIS#
variavel = "Olá, mundo!"
print(variavel)

#ATRIBUIR VARIÁVEIS E SUBTRAIR#
nome = input ("Digite seu nome: ")
ano_nascimento = input ("Digite seu ano de nascimento: ")
ano_atual = input ("Digite o ano atual: ")
idade = int(ano_atual) - int(ano_nascimento)
print(idade)

#1. TIPOS DE VARIAVEIS

#str (string): texto
valorString = "nome"
print(("valorString é uma variável do tipo {}".format(type(valorString))))

#int: números inteiros
valorInt = 1
print(("valorInt é uma variável do tipo {}".format(type(valorInt))))

#float: números reais (ponto flutuante)
valorFloat = 1.576
print(("valorFloat é uma variável do tipo {}".format(type(valorFloat))))

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

#EXEMPLO DO PORQUE PYTHON É POSSUI UMA TIPAGEM DINÂMICA#
textoVariavel=numeroVariavel
print(textoVariavel,type(textoVariavel))

my_list = [6, 2, 4]
print(my_list, type(my_list))

#2. ATRIBUIR TIPOS AS VARIAVEIS

#EXEMPLO 1
textoVariavel=input("Insira um número: ")
print(textoVariavel, type(textoVariavel))
numeroVar=int(textoVariavel)
print(numeroVar, type(numeroVar))

#EXEMPLO2
textoVariavel=int(input("Insira um número: "))
print(textoVariavel, type(textoVariavel))

#BOOLEANS
textoVariavel=bool(input("Insira um boolean: "))
print(textoVariavel, type(textoVariavel))

#3. CONCATENAR: OPERAÇÃO QUE UNE O CONTEÚDO DE DUAS STRINGS#

variavel1=input("insira valor 1")
variavel2=input("insira valor 2")
print(variavel1+variavel2,type(variavel1+variavel2))

#4. OPERADORES

#4.1. OPERADORES ARITMÉTICOS

#EXEMPLO 1
variavel1=input("insira o valor 1: ")
variavel2=input("insira o valor 2: ")

variavel1=int(variavel1)
variavel2=int(variavel2)

print("Adição: ",variavel1+variavel2,type(variavel1+variavel2))
print("Subtração: ",variavel1-variavel2,type(variavel1-variavel2))
print("Multiplicação: ",variavel1*variavel2,type(variavel1*variavel2))
print("Divisão: ",variavel1/variavel2,type(variavel1*variavel2))
print("Divisão inteira: ",variavel1//variavel2,type(variavel1//variavel2))
print("Módulo: ",variavel1%variavel2,type(variavel1%variavel2)) #retorna o resto da divisão de ambos operandos
print("Exponenciação: ",variavel1**variavel2,type(variavel1**variavel2)) #retorna o resultado da elevação da potência pelo outro

#EXEMPLO 2
variavel1=int(input("Insira o valor 1:"))
variavel2=int(input("Insira o valor 2"))

print("Adição: ",variavel1+variavel2,type(variavel1+variavel2))
print("Subtração: ",variavel1-variavel2,type(variavel1-variavel2))
print("Multiplicação: ",variavel1*variavel2,type(variavel1*variavel2))
print("Divisão: ",variavel1/variavel2,type(variavel1*variavel2))
print("Divisão inteira: ",variavel1//variavel2,type(variavel1//variavel2))
print("Módulo: ",variavel1%variavel2,type(variavel1%variavel2)) #retorna o resto da divisão de ambos operandos
print("Exponenciação: ",variavel1**variavel2,type(variavel1**variavel2)) #retorna o resultado da elevação da potência pelo outro

#EXEMPLO 3
variavel1=bool(input("insira valor 1: "))
variavel2=bool(input("insira valor 2: "))
total=variavel1+variavel2
print(total,type(total))

#EXEMPLO 4
variavel1=int(input("Insira o valor 1:"))
variavel2=int(input("Insira o valor 2:"))
variavel1*=variavel2
print("Multiplicação =: ",variavel1,type(variavel1))

variavel3=int(input("Insira o valor 3:"))
variavel4=int(input("Insira o valor 4:"))
variavel3-=variavel4
print("Subtração =: ",variavel3,type(variavel3))

variavel5=int(input("Insira o valor 5:"))
variavel6=int(input("Insira o valor 6:"))
variavel5/=variavel6
print("Divisão =: ",variavel5,type(variavel5))

#4.1.2. PRECEDÊNCIA DE OPERADORES

#EXEMPLO 1
variavel1=input("insira o valor 1: ")
variavel2=input("insira o valor 2: ")
variavel3=input("insira o valor 3: ")

valor1=int(variavel1)
valor2=int(variavel2)
valor3=int(variavel3)

total2=valor1 * valor2 + valor3
total3=valor1 * (valor2 + valor3)

print("Totais:", total2, total3)

#EXEMPLO 2
valor1=int(input("Insira o valor 1: "))
valor2=int(input("Insira o valor 2: "))
valor3=int(input("Insira o valor 3: "))

total1=valor1 * valor2 + valor3
total2=valor1 * (valor2 + valor3)

print("Total 1: ", total1, type(total1), "Total 2:", total2, type(total2))

#4.2. OPERADORES RELACIONAIS OU DE COMPARAÇÃO

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

variavel1=input("Insira o valor 1: ")
variavel2=input("Insira o valor 2: ")

#IGUAL A ==
resultado = variavel1 == variavel2
print("resultado ==:", resultado, type(resultado))

#DIFERENTE DE !=
resultado = variavel1 != variavel2
print("Resultado !=:", resultado, type(resultado))

#MENOR QUE <
resultado = variavel1 < variavel2
print("Resultado <:", resultado, type(resultado))

#MAIOR QUE >
resultado = variavel1 > variavel2
print("Resultado >:", resultado, type(resultado))

#MAIOR OU IGUAL A >=
resultado = variavel1 >= variavel2
print("Resultado >=:", resultado, type(resultado))

#MENOR OU IGUAL A <=
resultado = variavel1 <= variavel2
print("Resultado <=:", resultado, type(resultado))

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

#4.3. OPERADORES LÓGICOS

variavel1=input("insira o valor: ")
variavel2=input("insira o valor: ")
variavel3=input("insira o valor: ")

#AND (EM OUTRAS LINGUAGENS É O EQUIVALENTE A & &&)
resultado = variavel1==variavel2 and variavel2==variavel3
print("resultado == and:", resultado, type(resultado))

#OR (EM OUTRAS LINGUAGENS É O EQUIVALENTE A │ ││)
resultado = variavel1==variavel2 or variavel2==variavel3
print("resultado == or:", resultado, type(resultado))

#OR NOT
resultado = variavel1==variavel2 or not variavel2==variavel3
print("resultado == or not:", resultado, type(resultado))


#4.4. OPERADOR DE IDENTIDADE
cidade_1 = "São Paulo"
cidade_2 = "São Paulo"
cidade_3 = "Rio de Janeiro"

#IS
resultado1=cidade_1 == cidade_2
resultado2=cidade_2 == cidade_3
print("resultado == is:", resultado1, resultado2)

#EXEMPLO
cidade_p1 = "São Paulo"
cidade_p2 = "São Paulo"
cidade_p3 = "Rio de Janeiro"

resultado1 = cidade_p1 == cidade_p2
resultado2 = cidade_p2 == cidade_p3
print(" ==", resultado1, resultado2)

print(id(cidade_p1))
print(id(cidade_p2))
print(id(cidade_p3))
print(cidade_p1 is cidade_p2)
print(cidade_p1 is not cidade_p3)
print(cidade_p1 is cidade_p3)

print("----------------------")

list1 = [1,2,3,4]
list2 = [1,2,3,4]
list3 = list1

resultado1 = list1==list2
resultado2 = list1==list3
resultado3 = list2==list3
print(" ==", resultado1, resultado2, resultado3)

print(id(list1))
print(id(list2))
print(id(list3))

print("is: ", list1 is list2, " ==", list1==list2)
print("is: ", list1 is list3, " ==", list1==list3)

#4.5. OPERADOR DE ASSOCIAÇÃO
variavel1=input("insira o valor: ")
lista="Vidas Secas"

#IN
resultado=variavel1 not in lista
print("resultado not in: ", resultado)

#NOT IN
resultado=variavel1 in lista
print("resultado in: ", resultado)

#5. FUNÇÕES

#5.1. bool
#5.2. chr
#5.3. float#5.3. int
#5.4. input
#5.6. list
#5.7. print
#5.8. type
#5.9. id
#5.10 str

#5.11 len
umastring = "Torto arado"
tamanho=len(umastring)
print("tamanho: ", tamanho)
print("char[0]", umastring[0:5])
print("char[0]", umastring[-3:])

#5.12. index
umastring = "Torto arado"
indexWhiteSpace=umastring.index(' ')
print("index:", indexWhiteSpace, "string:", umastring[:indexWhiteSpace])

#5.13. upper e lower
umastring = "Torto arado"
print("UPPER: ", umastring.upper(), "lower: ", umastring.lower())

#5.14. artswith e endswith
umastring = "Torto arado"
print("starts with:", umastring.startswith("Torto"))
print("ends with:", umastring.endswith("ado"))

#5.15. split
umastring = "Torto arado"
palavrasSeparadas = umastring.split(" ")
print("Palavra[0]:", palavrasSeparadas[0])
print("Palavra[1]:", palavrasSeparadas[1])

#5.16. replace
umastring = "Torto arado"
palavrasSeparadas = umastring.replace("arado", "elefante")
print(palavrasSeparadas)

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


