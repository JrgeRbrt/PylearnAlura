i = 1
while i < 8:
    print(i)
    i += 1
a = 1
#while é um loop, que é autoexplicativo: enquanto a condição for verdadeira, executa o código abaixo.
while a < 10:
    print(a)
    if a == 5:
        break #break serve para parar o loop
    a += 1

z = 0
while z < 6:
  z += 1
  if z == 3:
    continue
  print(z)

#else pode ser usado no loop while

x = 1
while x < 6:
    print(x)
    x += 1
else:
    print('x Não é menor que 6 mais!')
