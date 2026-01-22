continua = "s"
soma = 0
count = 0
maior = 0
menor = 0

while True:
    n = int(input("Digite um valor: "))
    soma += n
    count += 1
    
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    continua = str(input("Você deseja continuar? [S/N] ")).strip().lower()
    if continua != "s":
        break
média = soma / count

print(f"A média dos valores digitados é {média}.")
print(f'O maior valor foi {maior} e o menor foi {menor}')
