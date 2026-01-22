valorProduto = float(input('Qual o valor do produto?'))
desconto = float(input('Qual a desconto?'))
promocao = valorProduto - (valorProduto * desconto / 100)
print(f'O seu produto com {desconto:.0f}% de desconto fica R${promocao:.2f}')
