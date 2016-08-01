# Probemos for loops
# la variable i se incrementa automaticamente
print('Probando for loops')
print('Mi nombre es')
for i in range(5):
    print('Sergio cinco veces (' + str(i) + ')')
print(' ')

print('Sumando 0 a 100 :')
intTotal = 0
for intContador in range(101):
    intTotal = intTotal + intContador
print(intTotal)
print(' ')

# for con parametros de start, stop, step
print('Contemos de uno en uno hasta 20')
for i in range(20):
    print(i+1)
print('Contemos desde diez de uno en uno hasta 20')
for i in range(10,21):
    print(i)
print('Contemos desde cinco de cinco en cinco hasta 50')
for i in range(5,51,5):
    print(i)
print('Contemos en disminucion desde cinco hasta cero')
for i in range(5,-1,-1):
    print(i)
