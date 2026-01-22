maior = 0
menor = 0

for i in range(1, 5):
    peso = int(input('Digite o peso em Kg: '))
    if i == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso é {maior}')
print(f'O menor peso é {menor}')
