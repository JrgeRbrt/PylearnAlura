from random import randint

print("-=-" * 20)
print("Jogo do PAR ou IMPAR")
print("-=-" * 20)

count = 0

while True:
    c = randint(1, 10)
    j = int(input("Digite o seu numero escolhido: "))
    parOuImpar = str(input("Par ou ímpar? ")).lower().strip()[0]

    if parOuImpar == "p":    # PAR CASE 
        if (j + c) % 2 == 0:
            print(f"VOCÊ GANHOU!!! O computador jogou {c} e você jogou {j}.")
        else:
            print(f"VOCÊ PERDEU!!! O computador jogou {c} e você jogou {j}.")
            break   

    if parOuImpar == "i":   # IMPAR CASE
        if (j + c) % 2 != 0:
            print(f"VOCÊ GANHOU!!! O computador jogou {c} e você jogou {j}.")
        else:
            print(f"VOCÊ PERDEU!!! O computador jogou {c} e você jogou {j}.")
            break    

    count += 1
print(f"Fim de jogo! Você ganhou {count} vezes!")