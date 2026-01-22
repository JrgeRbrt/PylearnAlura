print('-=-' * 20)
print('Calcule ja o financiamento da sua casa!')
print('-=-' * 20)
vCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Quanto você recebe mensalmente? R$'))
vezes = int(input('Quantas parcelas? '))
vParcela = vCasa / vezes
if vParcela > (salario * 30 / 100):
    print('O seu financiamento infelizmente foi negado!')
else:
    print('Parabéns! O seu financiamento foi aprovado!')
