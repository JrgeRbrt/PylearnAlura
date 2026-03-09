def calcula_gorjeta(valor, porcentagem):
    gorjeta = (valor * porcentagem / 100) 
    total = valor + gorjeta
    return gorjeta, total

valor = float(input("Digite o valor da conta: "))
porcentagem = int(input("Digite a porcentagem da gorjeta: "))

valor_gorjeta, valor_total = calcula_gorjeta(valor, porcentagem)

print(f"Valor da gorjeta: R${valor_gorjeta:.2f}")
print(f"Valor total da conta: R${valor_total:.2f}")
    