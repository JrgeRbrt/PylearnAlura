print("-=-" * 20)
print("CADASTRO DE PESSOAS")
print("-=-" * 20)

count = 1
maioridade = 0
menosDeVinte = 0
homens = 0



while True:
    idade = int(input("Digite a idade: "))
    sexo = 'null'
    continua = 'null'
    
    while sexo not in "mf":
        sexo = str(input("Digite o sexo? [M/F] ")).strip().lower()[0]

    if sexo in 'Ff' and idade < 20: # Verifica idade se mulher
            menosDeVinte += 1
    if idade > 18:  # Verifica Maioridade
        maioridade += 1
        
    if sexo in 'Mm':    # Verifica se Homem
        homens += 1

    while continua not in "sn":
        continua = str(input("Você deseja continuar? [S/N] ")).strip().lower()[0]  # Deseja continuar?
        if continua not in "NnSs":  # Invalid input
            print("Você digitou um valor invalido!")
    if continua in "Nn":    # Flag
            break

    count += 1
print(f"Você cadastrou {count} pessoas. {homens} são homens. {menosDeVinte} mulheres tem menos de vinte. E {maioridade} pessoas ja tem são de maior")
