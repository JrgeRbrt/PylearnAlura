while True:
    valor = int(input("Quer ver a tabuada de qual numero? "))
    
    if valor < 0:
        break

    for i in range(1, 11):
        print(f'{valor} x {i} == {valor * i}')
print("Fim do programa.")
