salarioAntigo = float(input('Qual o salário atual? R$'))
reajuste = int(input('Quanto de reajuste em porcentagem?'))
salarioNovo = salarioAntigo + (salarioAntigo * reajuste / 100)
print(f'O salario reajustado com {reajuste}% de acréscimo fica R${salarioNovo:.2f}')