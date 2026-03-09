import sys

def validar_cpf(cpf_inteiros):
    """
    Recebe uma lista de 11 inteiros e retorna True se o CPF for válido
    ou False se for inválido, baseando-se no cálculo matemático de verificação.
    """
    # Verificação de segurança: CPFs com todos os números iguais passam na 
    # conta matemática, mas são inválidos na vida real.
    if len(set(cpf_inteiros)) == 1:
        return False

    soma1 = 0
    soma2 = 0 
    sequencia_1_ver = 10
    sequencia_2_ver = 11

    # --- Apuração do primeiro digito verificador ---
    for num in cpf_inteiros:
        soma1 = soma1 + (num * sequencia_1_ver)
        sequencia_1_ver -= 1
        if sequencia_1_ver == 1:
            break
            
    resto1 = soma1 % 11
    primeiro_digito_calculado = 11 - resto1
    if primeiro_digito_calculado >= 10:
        primeiro_digito_calculado = 0

    # --- Apuração do segundo digito verificador ---
    for num in cpf_inteiros:
        soma2 = soma2 + (num * sequencia_2_ver)
        sequencia_2_ver -= 1
        if sequencia_2_ver == 1:
            break
            
    resto2 = soma2 % 11
    segundo_digito_calculado = 11 - resto2
    if segundo_digito_calculado >= 10:
        segundo_digito_calculado = 0

    # Retorna o resultado da comparação (já é um valor booleano)
    return primeiro_digito_calculado == cpf_inteiros[-2] and segundo_digito_calculado == cpf_inteiros[-1]


# ==========================================
# FLUXO PRINCIPAL DO PROGRAMA
# ==========================================
if __name__ == '__main__':
    # 1. Receber entrada do usuario
    entrada_usuario = list(input("Digite o seu CPF: "))

    # 2. Verificar se existe algum digito invalido (letras)
    try:
        lista_digitos = [int(digito) for digito in entrada_usuario]
    except ValueError:
        print("Você digitou um valor invalido, tente novamente.")
        sys.exit()

    # 3. Verificar quantidade de digitos
    if len(lista_digitos) != 11:
        print("CPF invalido. Quantidade de dígitos incorreta.")
        sys.exit()

    # 4. Fazer calculo de validaçao
    if validar_cpf(lista_digitos):
        print("O seu CPF é valido!")
    else:
        print("CPF invalido!")