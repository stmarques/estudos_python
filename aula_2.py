
'''
Características do python
- Sintaxe mais enxuta
- Tipagem dinâmica
'''

#1. TIPOS DE VARIAVEIS

#TIPO STRING
textoVariavel="Olá, mundo!"
print(textoVariavel, type(textoVariavel))

#TIPO INTEIRO
numeroVariavel=2
print(numeroVariavel, type(numeroVariavel))

#TIPO BOOLEAN
boolVariavel=True
print(boolVariavel, type(boolVariavel))

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


#OPERADOR DE IDENTIDADE
cidade_1 = "São Paulo"
cidade_2 = "São Paulo"
cidade_3 = "Rio de Janeiro"

#IS
resultado1=cidade_1 == cidade_2
resultado2=cidade_2 == cidade_3
print("resultado == is:", resultado1, resultado2)

#OPERADOR DE ASSOCIAÇÃO
variavel1=input("insira o valor: ")
lista="Vidas Secas"

#IN
resultado=variavel1 not in lista
print("resultado not in: ", resultado)

#NOT IN
resultado=variavel1 in lista
print("resultado in: ", resultado)
