carros = {
    'Marca' : 'Ford',
    'Modelo' : 'Mustang',
    'Ano' : 2018
}
for i in carros:
    print(i)
#O loop escrito dessa forma, mostra somente os nomes chaves.


for x in carros:
    print(carros[x])
#já escrito dessa forma, mostra os valores do dicionario
#para mostrar os valores, também pode ser usado o metodo values()
for y in carros.values():
    print(y)

#a mesma lógica pode ser usada com o metodo keys()
for z in carros.keys():
    print(z)

#para mostrar tanto os valores quanto as chaves, usamos o metodo items()
for a, b in carros.items():
    print(a, b)
