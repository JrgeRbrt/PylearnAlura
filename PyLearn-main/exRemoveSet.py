thisset = {'Banana', 1, False}

thisset.remove('Banana')

print(thisset)
#esse é um metodo de remover itens de um Set, podemos usar também o discard()

thisset.discard(False)
print(thisset)
#se o item que queremos remover com o discard() não existir, não vai haver erro, o programa roda normalmente.

newSet = {'Banana', True, 'Cherry', 7}

x = newSet.pop()
print(x)
print(newSet)
#o metodo pop() remove um item aleatório da Set, o output da var x é o item removido.

thisset.clear()
del newSet

print(thisset)
print(newSet)
#o metodo clear() remove todos items de uma set, enquanto o del, deleta a set por completo.