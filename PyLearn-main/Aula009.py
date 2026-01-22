frase = 'Curso em Video Python'
print(frase[9])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
#Fatiamento de string
print(len(frase))
#Mostra o tamanho da String
print(frase.count('o'))
#conta quantas vezes tem "o" na string
print(frase.count('o', 0, 13))
#quantas vezes existe "o" dentro do range de 0 ao 12
print(frase.find('deo'))
#procura "deo" dentro da string, tendo como output a posição em que começa o "deo", que nesse caso é 11
print(frase.find('Android'))
#quando não existe o valor procurado, retorna -1
print('Curso' in frase)
#existe curso em 'frase'?
print(frase.replace('Python', 'Android'))
#substitui 'Python' por 'Android'
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
#compreende a contagem de palavras considerando os espaços, e retorna com a primeira letra de cada palavra como maiusculo
print(frase.strip())
#revome os espaços desnecessarios da string
print(frase.split())
#divide a string
print('-'.join(frase))
#junta a string
