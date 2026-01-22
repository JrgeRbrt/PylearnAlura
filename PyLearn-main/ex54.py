from datetime import date
atual = date.today().year
tmaior = 0
tmenor = 0

for c in range(1, 8):
    nasc = int(input('Qual o ano de nascimento? '))
    idade = atual - nasc
    if idade < 18:
        tmenor += 1
    else:
        tmaior += 1
print(f'Temos {tmaior} pessoas maiores de idade')
print(f'Temos {tmenor} pessoas menores de idade')