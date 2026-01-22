brasileirao = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Mirassol', 'Botafogo', 'Bahia', 'São paulo', 'Fluminense', 'Bragantino', 'Grêmio', 'Ceará', 'Vasco', 'Corinthians', 
               'Atlético-MG', 'Internacional', 'Santos', 'Juventude', 'Vitória', 'Fortaleza', 'Sport')

print(f'Os 5 primeiros colocados são {brasileirao[0:5]}')
print("==" * 30)
print(f'Os ultimos 4 colocados são {brasileirao[-1:-5:-1]}')
print("==" * 30)
print(f'Os times em ordem alfabética são {sorted(brasileirao)}')
print("==" * 30)
print(f'O time Botafogo está na posição {brasileirao.index("Botafogo") + 1}')
print("==" * 30)