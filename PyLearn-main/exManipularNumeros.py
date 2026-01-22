num = int(input('Digite um numero entre 1 e 9999: '))
num = str(num).zfill(4)
u = num[3]
d = num[2]
c = num[1]
m = num[0]
print(f'Unidade {u}\n Dezena {d}\n Centena {c}\n Milhar {m}')