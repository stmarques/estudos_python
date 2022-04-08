
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

#4. OPERADORES BÁSICOS

#EXEMPLO 1
variavel1=input("insira o valor 1: ")
variavel2=input("insira o valor 2: ")

variavel1=int(variavel1)
variavel2=int(variavel2)

print("Soma: ",variavel1+variavel2,type(variavel1+variavel2))
print("Subtração: ",variavel1-variavel2,type(variavel1-variavel2))
print("Multiplicação: ",variavel1*variavel2,type(variavel1*variavel2))
print("Divisão: ",variavel1/variavel2,type(variavel1*variavel2))
print("Divisão inteira: ",variavel1//variavel2,type(variavel1//variavel2))
print("Modulo: ",variavel1%variavel2,type(variavel1%variavel2))
print("Exponencial: ",variavel1**variavel2,type(variavel1**variavel2))

#EXEMPLO 2
variavel1=int(input("Insira o valor 1:"))
variavel2=int(input("Insira o valor 2"))

print("Soma: ",variavel1+variavel2,type(variavel1+variavel2))
print("Subtração: ",variavel1-variavel2,type(variavel1-variavel2))
print("Multiplicação: ",variavel1*variavel2,type(variavel1*variavel2))
print("Divisão: ",variavel1/variavel2,type(variavel1*variavel2))
print("Divisão inteira: ",variavel1//variavel2,type(variavel1//variavel2))
print("Modulo: ",variavel1%variavel2,type(variavel1%variavel2))
print("Exponencial: ",variavel1**variavel2,type(variavel1**variavel2))

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
