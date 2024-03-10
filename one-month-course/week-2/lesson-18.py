states = {'SC': 'Santa Catarina', 'PR': 'Paraná', 'SP': 'São Paulo'}
print(states['NY'])

print(states.get('RJ', 'Not found'))

print(states.keys())
print(states.values())

states['RJ'] = 'Rio de Janeiro'
print(states)


user = {'name': 'Emanoel', 'height': 70, 'shoe size': 10.5, 'hair': 'brown', 'eye': 'brown'}
print(user['name'])
