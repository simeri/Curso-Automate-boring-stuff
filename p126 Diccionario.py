#! python3
__author__='Sergio Imeri 160729'
# Usando diccionarios, nombres con colores de perros
# Agregando llaves con valores

# Inicializo el diccionario. Nombre : Color
perros = {'Twister': 'café', 'Brownie': 'rubio', 'Tommy': 'café y negro'}

while True:
    nombre = input('Nombre del perro: (Enter para salir)')

    if nombre == '':     # enter termina
        break

    if nombre in perros:    # busca el nombre en el diccionario
        print(nombre, ' es de color ', perros[nombre])   # imprime el color
    else:
        print('No existe el perro', nombre, 'lo agregaremos')
        color = input('Cual es su color ?')
        perros[nombre] = color      # adiciona el nombre del perro y su color

print('\nImprime items')
print(perros.items())
for i in perros.items():
    print(i)       # imprime las llaves y sus valores

print('\nImprime keys')
print(perros.keys())
for i in perros.keys():
    print(i)       # imprime las llaves

print('\nImprime values')
print(perros.values())
for i in perros.values():
    print(i)       # imprime los valores

print('\nImprimo todo')
for i, j in perros.items():
    print('Llave', i, 'Valor', j)


#=======
    

