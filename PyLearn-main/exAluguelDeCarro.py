dias = int(input('Por quantos dias o seu carro foi alugado? '))
km = float(input('Quantos Km foram rodados? '))
precoDias = dias * 60
precoKm = km * 0.15
print(f'O valor do aluguel fica: R${precoDias + precoKm:.2f}')
