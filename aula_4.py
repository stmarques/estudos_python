#FUNÇÃO LISTA E APPEND
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
jedi.append("Mace Windu")
jedi.insert(2,"Luminara")
jedi.insert(2, input("Digite o nome de um Jedi: "))

for nome in jedi:
    print(nome)

#REMOVER ITENS   
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]
jedi.remove("Yoda")
jedi.pop(2)
for nome in jedi:
    print(nome)

#OUTROS MÉTODOS
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]
print("A lista foi criada assim: {}".format(valores))

#count() - retorna a quantidade de vezes que um elemtno aparece na lista
contagem = valores.count(7)
print("Nessa lista o número 7 aparece {} vezes".format(contagem))

#reverse() - inverte a ordem dos elementos de uma lista
valores.reverse()
print("A lista agora está invertida: {}".format(valores))

#sort() - organiza a lista em ordem crescente/alfabética
valores.sort()
print("A lista agora está ordenada: {}".format(valores))

#len - retorna o tamanho de um objeto ou a quantidade de elementos na lista
tamanho = len(valores)
print("A lista possui {} elementos".format(tamanho))

#sum - retorna a soma dos elementos presentes
soma = sum(valores)
print("A soma dos elementos é igual a {}".format(soma))
