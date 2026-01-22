a = 25
b = 23
if a > b:
    print('A é maior que B')

#o 'elif' seria como dizer: 'Se essa condição não for verdadeira, tente essa outra condição'
c = 22
d = 22
if c > d:
    print('C é maior que D')
elif c == d:
    print('C é igual que D')
else:
    print('Nada!')

#Temos também o operador 'AND'

x = 200
y = 400
z = 600
if x < y and y < z:
    print('batata')
else:
    print('arroz')
#esse operador diz que as duas condições tem que ser verdadeiras.
#também temos o operador 'OR', dizendo que uma dessas condições tem que ser verdadeiras.

if x < y or z < x:
    print('frita')
else:
    print('Feijão')

#temos o 'NOT' também.
if not x > y:
    print('Queijo')

#podemos aninhar if's também
if x < y:
    print('mussarela')
    if y < z:
        print('Ralado')

#um if não pode estar vazio, mas caso seja necessário, é usado o "pass"
if x < y :
    pass
