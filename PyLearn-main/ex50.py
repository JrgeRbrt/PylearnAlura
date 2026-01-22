soma = 0
count = 0

for c in range(1, 7):
    n = int(input('Digite um valor: '))# 6
    if n % 2 == 0:
        soma += n
        count += 1
print(f'Você informou {count} números e a soma foi {soma}')