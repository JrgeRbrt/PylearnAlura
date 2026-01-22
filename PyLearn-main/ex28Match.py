dia = 2
match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sabado')

#match é um operador de condição, ele divide casos, e se algum caso especifico condiz com a condição,
#aquele bloco de código é executado. Se nenhum caso der 'match', você pode tanto não executar nada, quanto
#pedir que um código especifico pra caso não tenha macth seja executado, usando o '_'.

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
#O '_' conta como um match sempre, então é importante deixar ele como ultimo caso
#Podemos também usar operadores com o match, por exemplo:

diaSemana = 7
match diaSemana:
    case 1 | 2 | 3 | 4 | 5:
        print('Hoje é um dia de semana!')
    case 6 | 7:
        print('Hoje é um fim de semana!')
