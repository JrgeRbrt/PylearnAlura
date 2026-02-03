print('-=-' * 40)
print('Todos os números ímpares e multiplos de 3 entre 1 e 400')
print('-=-' * 40)
for i in range(1, 401):
    if i % 2 != 0 and i % 3 == 0:
        print(i)
