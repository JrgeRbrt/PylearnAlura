print('-=-' * 20)
print('Todos os números ímpares e multiplos de 3 entre 1 e 500')
print('-=-' * 20)
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        print(i)
