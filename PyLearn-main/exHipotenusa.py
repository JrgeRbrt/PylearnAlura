from math import sqrt, hypot
c1 = int(input('Qual o valor cateto oposto?: '))
c2 = int(input('Qual o valor cateto adjacente?: '))
hipotenusa = hypot(c1, c2)
print(f'Considerando o cateto oposto {c1} e cateto adjacente {c2}, a hipotenusa é {hipotenusa:.2f}')
