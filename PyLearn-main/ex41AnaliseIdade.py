idade = int(input('Qual sua idade? '))
if idade < 9:
    print('Você é um atleta Mirim!')
elif idade < 14:
    print('Você é um atleta Infantil!')
elif idade < 19:
    print('Você é um atleta Junior!')
elif idade == 20:
    print('Você é um atleta Senior!')
else:
    print('Você é um atleta Master!')
