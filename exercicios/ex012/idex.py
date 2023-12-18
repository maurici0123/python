person={
    'name': 'felipe',
    'age': 26,
    'city': 'gramado',
    'profession': 'piloto'
}

print(person)
print(person.values())
print(person.keys())
print(person.items())

person['sexo']='m'
print(person)

del(person['sexo'])
print(person)

concessionaria={
    'bmw': ['m3', 'x6', 'i4', 'serie3'],
    'mercedes': ['gle', 'gla', 'amg gt', 'classe c'],
    'chevrolet': ['camaro', 'onix', 'cruze', 'tracker'],
    'toyota': ['corolla', 'sw4', 'camry', 'yaris'],
    'ferrari': [
        {
            'modelo': 'ferrari roma',
            'ano': 2019
        },
        {
            'modelo': 'ferrrari 458 spider',
            'ano': 2011
        },
        {
            'modelo': 'ferrari portofino',
            'ano': 2017
        }
    ]
}

print()
print()
print()

for x in concessionaria.values():
    print(x)