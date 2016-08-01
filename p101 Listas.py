__author__='Sergio Imeri'

lista = ['perro', 'gato', 'raton']  # lista con valores delimitados por comas
lista[0]   # imprime 'perro'
print('Hola ' + lista[0])   # imprime Hola perro
lista[-1]   # imprime el ultimo valor de la lista, -2 el penultimo y asi
	
# Listas dentro de listas
lista = [['perro', 'gato', 'raton'], [0,1,2]]
lista

lista[0]    # imprime la primera lista
lista[1]    # imprime la segunda lista

lista[0][0] # imprime perro
lista[1][1] # imprime 1
lista[0][2] , lista[1][2]   # imprime raton 2
	
# Slices (porciones de listas)
# spam[2] is a list with an index (one integer).
# spam[1:4] is a list with a slice (two integers).
	
lista[1:3]  # imprime ['gato', 'raton']

# Cantidad de items en una lista
len(lista)  # imprime 3

# Cambiando valores dentro de la lista
lista = ['perro', 'gato', 'raton', 'pajaro']
lista[1]='oso'
lista[3]=1234
lista   # imprime ['perro', 'oso', 'raton', 1234]

# Concatenacion de listas
lista = ['perro', 'gato', 'raton', 'pajaro']
lista=lista+[0,1,2,3]
lista   # imprime ['perro', 'gato', 'raton', 'pajaro', 0, 1, 2, 3]

# Replicacion de listas
lista*2  # imprime ['perro', 'gato', 'raton', 'pajaro', 0, 1, 2, 3, 'perro', 'gato', 'raton', 'pajaro', 0, 1, 2, 3]

# Eliminacion de valores dentro de la lista
lista = ['perro', 'gato', 'raton', 'pajaro']
del lista[1]    # borra gato de la lista
lista   # imprime ['perro', 'raton', 'pajaro']
