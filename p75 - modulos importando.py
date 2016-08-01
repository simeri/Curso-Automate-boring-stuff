# Importando un modulo y usandolo
# randint es una funcion del modulo random
import random
for i in range(5):
    print(random.randint(1, 10))    # numero random entre los numeros 1 & 10

import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
print('You typed ' + response + '.')
