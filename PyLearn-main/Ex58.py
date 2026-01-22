from random import randint

print("Bem vindo ao jogo de adivinhação 2.0!!!")
chuteJogador = int(input("Digite um valor para tentar adivinhar: "))    #escolha do Jogador

escolhaDaMaquina = randint(0, 10)   #escolha da Máquina

palpites = 1
while chuteJogador != escolhaDaMaquina:     #loop para manter o Jogador jogando até que acerte
    palpites += 1
    if chuteJogador < escolhaDaMaquina:
        chuteJogador = int(input("Mais... Tente novamente: "))
    elif chuteJogador > escolhaDaMaquina:
        chuteJogador = int(input("Menos... Tente novamente: "))


print(f'Você escolheu {chuteJogador} e a Máquina escolheu {escolhaDaMaquina}. Parabéns! Você GANHOU!!!')
print(f'Você ganhou depois de {palpites} palpites')
