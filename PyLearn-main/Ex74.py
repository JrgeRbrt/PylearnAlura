from random import randint

menorValor = 0
maiorValor = 0

sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))


print('Os valores sorteados foram: ', end='')
for n in sorteio:
    print(n, end=' ')
    if n > maiorValor:
        maiorValor = n
    if n < menorValor:
        menorValor = n

print(f'\nO maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')
