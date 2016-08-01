__author__='Sergio Imeri  160727'
""" Trabajando con listas
En vez de usar muchas variables para almacenar, es mejor usar listas

Ejemplo ineficiente para guardar nombres:

    print('Enter the name of cat 1:')
    catName1 = input()
    print('Enter the name of cat 2:')
    catName2 = input()
    print('Enter the name of cat 3:')
    catName3 = input()
    print('Enter the name of cat 4:')
    catName4 = input()
    print('Enter the name of cat 5:')
    catName5 = input()
    print('Enter the name of cat 6:')
    catName6 = input()
    print('The cat names are:')
    print(catName1 + ' ' + catName2

"""

# Ejemplo eficiente usando listas para guardar los nombres

listaPerros = []    # crea la lista en blanco

while True:
    print('Ingresa el nombre del perro #', len(listaPerros)+1, '(ó enter para parar)')
    nombrePerro = input()   # ingresa el nombre del perro
    if nombrePerro == '':   # si es enter o blanco se sale y termina
        break
    listaPerros = listaPerros + [nombrePerro]   # contatena la lista con el nombre ingresado

print('Ingresaste ', len(listaPerros), 'perros')
print('Los nombres de los perros son:')
for i in listaPerros:
    print(' ', i)

# Usando for con indices de la lista
for i in range(len(listaPerros)):   # range debe ir para especificar un rango
    print('Indice', i, '=', listaPerros[i])    # el indice de la lista
    
# Verficar si algun valor esta o no esta dentro de la lista
# in  y  not in
print('Ingresa el nombre del perro a buscar')
nombre = input()

if nombre in listaPerros:
    print('Encontré a', nombre)
else:
    print('Ese perro no existe')








    
    
    
