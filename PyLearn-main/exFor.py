fruits = [1, 2, 3, 4, 5]
for i in fruits:
    print(i)
# As linhas 2 e 3 vão printar todos os itens da lista fruits
# O break pede uma pausa, considerando a condição
    if i == 3:
        break

# Podemos também usar o loop "for" em uma string
for x in 'Banana':
    print(x)
    # printa todos os caracteres da string
mLista = ['Banana', 'Sorvete', 'Cacau']
for z in mLista:
    if z == 'Sorvete':
        break
    print(z)

# O else pode ser usado com o for, a lógica é que assim que o loop acabe,
#  o else determina um bloco de código a ser executado
for y in range(10):
    print(y)
else:
    print('O loop acabou! ')
# Importante lembrar que o metodo range não considera o numero 10 ali!
# Importante lembrarque o else não é executado quando o loop para com um break!
