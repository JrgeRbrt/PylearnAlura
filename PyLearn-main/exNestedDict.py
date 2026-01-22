#podemos aninhar um dicionario
familia = {
    'Criança1' : {
        'Nome' : 'Joao',
        'Idade' : 12,
    },
    'Criança2' : {
        'Nome' : 'Isabella',
        'Idade' : 6,
    },
    'Criança3' : {
        'Nome' : 'Izadora',
        'Idade' : 2,
    }
}

#podemos também adicionar varios dicionarios a um só
crianca4 = {
    'Nome': 'Joao',
    'Idade': 12,
}
crianca5 = {
    'Nome': 'Isabella',
    'Idade': 6,
}
crianca6 = {
    'Nome': 'Izadora',
    'Idade': 2,
}
newFamilia = {
    'Criança4' : crianca4,
    'Criança5' : crianca5,
    'Criança6' : crianca6,
}

#para acessar um item em um dicionario aninhado, primeiro você deve chamar qual dicionario quer e a chave
print(newFamilia['Criança4']['Nome'])
