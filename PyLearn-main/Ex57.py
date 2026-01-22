sexo = str(input('Informe o seu gênero! [M/F] ')).strip().lower()[0]

while sexo not in "mf":
    print('Dados invalidos! Preencha o campo novamente com uma das opções validas.')
    sexo = input('Informe o seu gênero! [M/F] ').strip().lower()[0]

print(f'Sexo {sexo} selecionado com sucesso')
