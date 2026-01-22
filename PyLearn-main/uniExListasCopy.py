equipamentos = ['Espada', 'Machado', 'Arco', 'Flecha']
kit = equipamentos.copy()
print(kit)
#essa é uma forma de copiar uma lista usando o método .copy

#também é possível copiar usando o método list()
armas = list(equipamentos)
print(armas)

#pode ser usado também o operador [:]
novasArmas = equipamentos[:]
print(novasArmas)
