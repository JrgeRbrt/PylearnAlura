from ex02contador import contar_palavras

frase = (input("Digite a sua frase: ")).strip()

if not frase:
    print("ERRO: Nenhuma frase foi digitada.")
else:
    resultado = contar_palavras(frase)
    if resultado:
        print("Contagem de Palavras: ")
        for palavra, quantidade in resultado.items():
            print(f"{palavra} : {quantidade}")
    else:
        print("Nenhuma palavra valida foi encontrada")

