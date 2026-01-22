#Podemos extrair items de uma Tuple para torna-las variaveis
#o nome disso é Unpacking ou Desempacotar/Extrair
frutas = ('Maçã', 'Banana', 'Pecego')
(vermelho, amarelo, vermelho1) = frutas
print(vermelho)
print(amarelo)
print(vermelho1)

muitasFrutas = ('Maçã', 'Banana', 'Pecego', 'Uva', 'Mamão')
(vermelho, amarelo, *resto) = muitasFrutas
print(vermelho)
print(amarelo)
print(resto)
#usar o * faz com que o resto dos items seja puxado para variavel

#If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)