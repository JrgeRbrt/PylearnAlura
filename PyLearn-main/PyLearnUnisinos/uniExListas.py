comidas = ['Maçã', 'Banana', 'Sorvete', 'Queijo', 'Salgadinho']
newList = []
for x in comidas:
    if 'S' in x:
        newList.append(x)

print(newList)

#esse código usa o método .append pra anexar items da lista 'comidas' para a 'newList'

#forma com compreensão de listas
comidas1 = ['Maçã', 'Banana', 'Sorvete', 'Queijo', 'Salgadinho']

newList1 = [x for x in comidas1 if 'Q' in x]
print(newList1)
