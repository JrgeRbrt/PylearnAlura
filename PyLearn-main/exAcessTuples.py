Tuple = ('Mamão', 'Maçã', 'Banana', 'Cereja', 'Pêra')
print(Tuple[1])
print(Tuple[-1])
#quando colocamos -1 no index, estamos referenciando o ultimo item. -2 = penultimo item e etc.
print(Tuple[1:3])
print(Tuple[:2])
print(Tuple[2:])
#Ranges, quando não aparece, puxa do inicio ou fim
print(Tuple[-4:-1])
if 'Banana' in Tuple:
    print('Sim, o item: "Banana", esta na Tuple')
else:
    print('Não, o item: "Banana", não esta na Tuple')
    