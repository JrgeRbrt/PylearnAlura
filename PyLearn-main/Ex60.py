n = int(input("Digite um valor para descobrir o seu fatorial: "))

fatorial = 1
contador = n

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f'O fatorial de {n} é: {fatorial}')
