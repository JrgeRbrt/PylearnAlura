lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tupla são IMUTÁVEIS

for comida in lanche:
    print(f'Eu vou comer {comida}')

for count in range(0, len(lanche)):
    print(lanche[count])

print(sorted(lanche))


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(c, d)
print(c.count(5))
print(c.index(8))
print(c.index(5, 1))    # O segundo elemento é o deslocamento
print(len(c))


pessoa = ('Jorge', 18, 'M', 68.90)
print(pessoa)
del(pessoa)
print(pessoa)