# Funções são blocos de códigos que só executam quando são chamados
# Para definirmos uma função, usamos o 'def'
def first_func():
    print('Batata')
    lista = [1, 2, 3, 4]
    print(lista[2])


first_func()

def  my_func(refnames): # Refnames é um parametro, que podemos chamar depois 
    print(refnames + ' Oliveira')


my_func('João')
my_func('Tobias')
my_func('Jorge')
my_func('Feresp')
# Aqui estamos determinando o que deve ser lido no parametro da função
# Isso se chama arqgumentos!



# Uma função deve ser chamada com o mesmo número de argumentos que os parâmetros #type: ignore
# Por exemplo:
def new_func(pNome, sNome):
    print(pNome + " " + sNome)


new_func('João', 'Oliveira') # Correto
# new_func('João') # Incorreto, falta um argumento

# Caso você não saiba quantos argumentos serão passados, use * antes do nome do parâmetro
def other_func(*criancas):
    print('A criança mais velha é ' + criancas[2])

other_func('João', 'Maria', 'Tobias', 'Ana')
