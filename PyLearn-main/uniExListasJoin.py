lista = ['a', 'b', 'c']
num = [ 1 , 2 , 3 ]

concatenar = lista + num
print(concatenar)

#isso vai concatenar as duas listas

#uma outra forma de juntar listar pode ser com o método append()
for x in lista:
    num.append(x)

print(num)

#outra forma seria adicionando items de uma lista para outra com o método extend()
lista.extend(num)
print(lista)
