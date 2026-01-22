count = 0
soma = 0

while True:
    n = int(input("Digite um valor: "))
    
    if n == 999:    # Flag = 999
        break

    soma += n
    count += 1
print(f'Você digitou {count} números e a soma deles resulta em: {soma}!!')
