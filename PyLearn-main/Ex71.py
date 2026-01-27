print("=" * 50)
print(f'{"BANCO CEV":^40}')
print("=" * 50)

valor = int(input("Qual valor você deseja sacar? R$"))

valorTotal = valor
ced = 100
totalced = 0

while True:
    if valorTotal >= ced:
        valorTotal -= ced
        totalced += 1
    else:
        print(f"Você recebera {totalced} cédulas de {ced}")

        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totalced = 0
        if valorTotal == 0:
            break
print("FIM DO PROGRAMA!")
