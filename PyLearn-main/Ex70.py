print("-=-" * 20)
print("LOJA DO SEU ZÉ")
print("-=-" * 20)

continua = "sim"
valorTotal = 0
acima1000 = 0
menorValor = 0
count = 1
nomeMaisBarato = ""

while True:
    nome = str(input("Nome do produto: "))
    preco = int(input("Preço: R$ "))
    continua = str(input("Deseja continuar? [S/N] ")).strip().lower()[0]    # Inputs do usuário
    

    valorTotal += preco # Calculo do valor total

    if count == 1 or preco < menorValor:
        menorValor = preco
        nomeMaisBarato = nome # Calculo do menor valor
    
    if preco >= 1000:
        acima1000 += 1  # Calculo do valor acima de 1000
    
    if continua in "Nn":    # FLAG
        break

    count += 1
    
print(f"O total da compra foi: R${valorTotal:.2f}")
print(f"Temos {acima1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {nomeMaisBarato} que custa R${menorValor:.2f}")
