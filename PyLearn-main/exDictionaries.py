myDict = {
    'Marca' : 'Ford',
    'Modelo' : 'Mustang',
    'Ano' : 1964
}
print(myDict)
#Dicionarios são usados em pares, são ordenados, mutáveis e não aceitam duplicatas.
print(myDict['Marca'])
print(len(myDict))

otherDict = {
    'Marca' : 'Ford',
    'Elétrico' : False,
    'Ano' : 1964,
    'Cores' : ['Vermelho', 'Branco', 'Azul']
}
#Dicionarios aceitam qualquer tipo de dado.
#podem ser usado como métodos também.
metodoDict = dict(nome = 'Jorge', Idade = 18, brasileiro = True)
print(metodoDict)
