n = int(input("Digite quantos termos você precisa da sequência de Fibonnacci "))

count = 0
p1 = 0
p2 = 1
total = 0

while count <= n:
    total = p1 + p2
    p1 = p2
    p2 = total
    count += 1
    print(total)
