thisIsaSet = {1, 2, 3, 4, 5, 6}
print(thisIsaSet)

#Sets não aceitam duplicatas, elas são ignoradas
#True e 1, são considerados valores iguais em Sets
otherSet = {True, 1, 2, 'Banana', 'Cherry'}
print(otherSet)
#o mesmo acontece com 'False' e 0
zeroSet = {0, False, 'Banana', 'Cherry'}
print(zeroSet)

#uma set também pode ser construída como um método
thisset = set((1, 2, 'Banana', 'Cherry'))
print(thisset)
