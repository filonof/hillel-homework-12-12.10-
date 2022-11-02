# 1

'''
Дан список словарей, необходимо записать их в файл с помощью модуля pickle.
В каждом из словарей одинаковый набор ключей, а все значения представлены в виде строк
'''

import pickle

product_name = [
    {
        'type': 'Motherboard',
        'name': 'MSI MPG X570',
    },
    {
        'type': 'Processor',
        'name1': 'AMD Ryzen 7 3700X'
    }
]

file = open('can.ua', 'wb')
file.write(pickle.dumps(product_name))
file.close()

# 2

'''
Дано два словаря

A = {'key': 1}
B = {'key1: 2}

Необходимо написать код который будет их объединять

C = {'key': 1, 'key1': 2}

Но нужно так-же учитывать коллизии, например ситуация когда у нас два одинаковых ключа и чтобы не потерять значения
нужно записать в один ключ список в котором будут находится значения

Например:

A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}
C = {'key': [1, 'Hello'], 'key2': True}
'''

import json

pc_for_games = {
    'purpose': 'gaming',
    'price with sale': '850$'
}
pc_for_work = {
    'purpose': 'work',
    'price without sale': '450$'
}
same_keys = {}
for key, i in pc_for_games.items():
    for key2, j in pc_for_work.items():
        if key == key2:
            same_keys[key2] = [i, j]
        else:
            break

diff_keys = pc_for_games | pc_for_work
result = diff_keys | same_keys

json_result = json.dumps(result)
with open('result.json', 'w') as file:
    file.write(json_result)
