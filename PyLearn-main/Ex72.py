nExtenso = ('zero', 'um', 'dois', 'tres','quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
             'dez', 'onze', 'doze', 'treze','quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

continua = ''

while True:
    nUsuario = int(input('Digite um valor entre 0 e 20: '))
    while nUsuario not in range(0, 21):
        nUsuario = int(input('Você digitou um numero invalido, tente novamente:'))
    print(f"Você digitou o número {nExtenso[nUsuario]}")
    continua = str(input("Você deseja continuar? [S/N] ")).strip().lower()[0]
    if continua in "Nn":
        break
