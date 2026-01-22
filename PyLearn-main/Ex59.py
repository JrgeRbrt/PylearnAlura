valor1 = int(input("Digite o primeiro valor da Operação: "))
valor2 = int(input("Digite o segundo valor da Operação: "))     # Escolhas do usuário
print("Agora escolha a operação")

def menu():     # Menu de escolha
    return int(input("""
        [1] Soma
        [2] Multiplicação
        [3] Qual é o Maior
        [4] Novos Números
        [5] Sair        
    """))

resultado = 0
while True:
    opr = menu()

    if opr == 1:
        resultado = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é: {resultado}')
    elif opr == 2:
        resultado = valor1 * valor2
        print(f'A multiplicação entre {valor1} e {valor2} é: {resultado}')
    elif opr == 3:
        resultado = max(valor1, valor2)
        print(f'O maior entre {valor1} e {valor2} é: {resultado}')
    elif opr == 4:
        print('Informe os valores novamente:')
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
    elif opr == 5:
        print("Fim do programa. Obrigado por usar!")
        break
    else: 
        opr = int(input("""Opção invalida, tente novamente!
        [1] Soma
        [2] Multiplicação
        [3] Qual é o Maior
        [4] Novos Números
        [5] Sair        
    """))
    print("=-=" * 15)
    