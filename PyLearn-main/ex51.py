p1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a Razão: '))
d = p1 + (10 - 1) * r
for i in range (p1, d + r, r):
    print(i)
