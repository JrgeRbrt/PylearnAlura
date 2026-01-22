somaidade = 0
mediaidade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totmulher20 = 0
# Definição das variaveis que vão receber valores dentro do laço

for p in range(1, 5):
    print(f'========= {p}ª PESSOA =======')
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    #Requisição dos dados

    somaidade += idade  # Soma as idades das pessoas

    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    # Define qual o homem mais velho dentre as pessoas


    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    # Calcula o total de mulheres menores de 20 anos

mediaidade = somaidade / 4  # calcula a média das idades


print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O nome do homem mais velho é {nomeVelho} e sua idade é {maiorIdadeHomem}')
print(f'Temos {totmulher20} mulheres com menos de 20 anos')
