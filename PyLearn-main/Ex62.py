a1 = int(input("Digite o primeiro termo de uma PA: "))
r = int(input("Digite a razão da PA: "))

termo = a1
cont = 1
total = 0
adc = 10

while adc != 0:
    total += adc
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += r
        cont += 1

    print('PAUSA')
    adc = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {total} termos mostrados.")
