nums = int(input("Digite valores para serem somados! [999 para parar o programa] "))

total = 0
while True:
    if nums == 999:
        break
    
    total += nums
    nums = int(input("Digite valores para serem somados! [999 para parar o programa] "))
print(f'A soma dos números digitados é: {total}')
