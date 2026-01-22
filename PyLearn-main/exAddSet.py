mySet = {1, 2, 3, 3, 'Banana', 'Cherry', False}

mySet.add('Orange')

print(mySet)
#com o método .add podemos adicionar item as sets, note que o "Orange" Não aparece numa ordem "correta"

otherset = {'Maçã', 'Quiabo'}
mySet.update(otherset)

print(mySet)
#Podemos adicionar qualquer Iterável a uma Set, ex: Listas, Dicionarios, Tuples.
myList = ['Machado', 7]
mySet.update(myList)
print(mySet)
