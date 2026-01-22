carros = {
    'Marca' : 'Ford',
    'Modelo' : 'Mustang',
    'Ano' : 2018
}
carros.pop('Marca')
#Usando o metodo pop() removemos a palavra chave nos referenciando a ela
print(carros)

carros.popitem()
#esse metodo popitem() remove o ultimo item do dicionario
print(carros)
carros['Marca'] = 'Ford'
carros['Ano'] = 2020
print(carros)

#O ultimo metodo é o 'del', ele pode tanto remover o dicionario por completo, como remover um item
#especificado pelo seu nome chave
del carros['Modelo']
print(carros)

del carros
print(carros)
#vai dar erro já que o dicionario não existe mais

carro.clear()#Esse metodo esvazia totalmente o dicionario
