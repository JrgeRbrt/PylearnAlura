#Tuples são inalteráveis, mas tem como burlar essa regra de algumas formas
x = ('Maçã', 'Banana', 'Cereja', 'Uva')
y = list(x)
y[1] = 'Kiwi'
x = tuple(y)
print(x)
#esse script convete a tuple em uma lista, altera o dado, e converte em tuple novamente
z = list(x)
z.append('Melância')
x = tuple(z)
print(x)
#o mesmo foi feito aqui, mas para adicionar um item
tupleAdd = ('Hamburguer', 'Xis', 'Batata')
x += tupleAdd
print(x)
#Podemos também adicionar uma Tuple a outra Tuple existente
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists