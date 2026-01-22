print('-=-' * 20)
print('Análise de Triângulo')
print('-=-' * 20)
l1 = int(input('Primeiro Lado: '))
l2 = int(input('Segundo Lado: '))
l3 = int(input('Terceiro Lado: '))

if l1 < l2 + l3:
    print('Não é possível formar um triângulo!')
elif l2 < l1 + l3:
    print('Não é possível formar um triângulo!')
elif l3 < l1 + l2:
    print('Não é possível formar um triângulo!')
else:
    print('É possível formar um triângulo!')
    if l1 != l2 != l3:
        print('Esse é um triângulo Escaleno')
    elif l1 == l2 == l3:
        print('Esse é um triângulo Equilátero')
    else:
        print('Esse é um triângulo Isósceles')
