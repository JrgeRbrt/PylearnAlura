print('-=-' * 20)
print('Você tem que se alistar?')
print('-=-' * 20)
idade = int(input('Qual a sua idade? '))
if idade < 18:
    print('Ainda não precisa se alistar!')
elif idade == 18:
    print('Você precisa se alistar!')
else:
    print('Já passou do prazo de alistamento!')

