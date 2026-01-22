n1 = int(input('Qual a sua nota do primeiro semestre: '))
n2 = int(input('Qual a sua nota do segundo semestre: '))
media = (n1 + n2) / 2
print(media)
if media >= 7:
    print('Você foi aprovado!')
elif media >= 5 and media <= 6.9:
    print('Você está de recuperação!')
else:
    print('Você foi reprovado!')
