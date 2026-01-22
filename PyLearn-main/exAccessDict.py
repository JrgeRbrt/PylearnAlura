newDict = {
    'Marca' : 'Ford',
    'Modelo' : 'Mustang',
    'Ano' : 2018
}
modelo = newDict['Modelo']
print(modelo)
x = newDict.get('Modelo')
print(x)

y = newDict.keys()
print(y)

newDict['Cor'] = 'Branco'
print(y)

z = newDict.values()
print(z)
newDict['Ano'] = '2020'
print(z)
