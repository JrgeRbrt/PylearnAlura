nums = (int(input("Digite um valor: ")), int(input("Digite mais um valor: ")), int(input("Digite outro valor: ")), int(input("Digite o último valor: ")))

pares = 0
print("Você digitou os valores: ")
for n in nums:
    print(n, end=' ')

print('\n Os numeros pares são: ', end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=', ')

if 9 in nums:
    print(f'\n O número 9 apareceu {nums.count(9)} vezes')
else:
    print('O número 9 não foi digitado')

if 3 in nums:
    print(f'O número 3 apareceu na posição {nums.index(3) + 1}')
else:
    print('O número 3 não foi digitado')

