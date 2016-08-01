__author__='Sergio Imeri 160727'
# Metodos

# .index() indice en una lista
lista = ['perro', 'gato', 'raton']

print('Lista de animales', lista)
print('raton tiene el indice', lista.index('raton'))

# .append() para agregar al final de una lista
print('Agrego mono al final de la lista')
lista.append('mono')
print('Lista de animales', lista)

# .insert(indice, valor) inserta un valor en la posicion del indice, y corre el resto
print('Inserto pollo en el indice #2, el resto lo corre')
lista.insert(2, 'pollo')
print('Lista de animales', lista)

# .remove() elimina el valor que hace match
print('Elimino pollo de la lista')
lista.remove('pollo')
print('Lista de animales', lista)

# .sort() ordena la lista
print('Ordenemos la lista ascendente')
lista.sort()
print('Lista de animales', lista)
print('Ordenemos la lista descendente')
lista.sort(reverse=True)
print('Lista de animales', lista)

# string[indice]
print('Imprimiendo coco=Cocodrilo con indices')
coco='Cocodrilo'
print ('Primera letra indice=0', coco[0])
print ('Quinta letra indice=4', coco[4])
print ('2da 3ra y 4ta posicion', coco[1:4])

for i in coco:
    print('Letras ', i)



      



