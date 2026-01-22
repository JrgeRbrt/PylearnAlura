b = 'Hello, World!'
print(b[2:5])
#takes the third and five character

b = "Hello, World!"
print(b[-5:-2])
#busca caracteres a partir do fim da string, ou seja, de tras para frente

a = "Hello, World!"
print(a.upper())
print(a.lower())
#converte a variavel para maiúsculo ou minúsculo

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!". Remove os espaços em branco do começo e do fim da string

a = "Hello, World!"
print(a.replace("H", "J"))
#substitui o H por J

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
