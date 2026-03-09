# 1 step - receber entrada do usuario e verificar quantidade de digitos. 2 step - verificar se existe algum digito invalido. 3 step - fazer calculo de validaçao do CPF.
import sys

Cpf_usuario = list(input("Digite o seu CPF: "))

try:
    lista_digitos = [int(digito) for digito in Cpf_usuario]
except ValueError:
    print("Você digitou um valor invalido, tente novamente.")
    sys.exit()

if len(lista_digitos) != 11:
    print("CPF invalido. Quantidade de dígitos incorreta.")
    sys.exit()

def validar_cpf(cpf_inteiros):
    # Primeiro digito verificador
    cpf_valido = False
    soma1 = 0
    soma2 = 0 
    sequencia_1_ver = 10
    sequencia_2_ver = 11

    for num in cpf_inteiros:
        soma1 = soma1 + (num * sequencia_1_ver)
        sequencia_1_ver -= 1

        if sequencia_1_ver == 1:
            break
    resto1 = soma1 % 11
    primeiro_digito_calculado = 11 - resto1

    if primeiro_digito_calculado >= 10:
        primeiro_digito_calculado = 0
    # ------------------ Apuração do primeiro digito verificador

    for num in cpf_inteiros:
        soma2 = soma2 + (num * sequencia_2_ver)
        sequencia_2_ver -= 1

        if sequencia_2_ver == 1:
            break
    resto2 = soma2 % 11
    segundo_digito_calculado = 11 - resto2
    if segundo_digito_calculado >= 10:
        segundo_digito_calculado = 0

    if primeiro_digito_calculado == cpf_inteiros[-2] and segundo_digito_calculado == cpf_inteiros[-1]:
        cpf_valido = True
    
    return cpf_valido

if validar_cpf(lista_digitos) == True:
    print("O seu CPF é valido!")
else:
    print("CPF invalido!")