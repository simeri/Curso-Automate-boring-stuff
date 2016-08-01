# while loop
print('Probemos while')
print('Cuantas veces contaremos ?')
intConteo = int(input())
intContador = 1

while intContador <= intConteo:
    print('Hola #', intContador)
    intContador = intContador +1
print(' ')

# break sale del loop
print('Probemos break contando 10 veces')
A = 1
while True:
    print (A)
    A = A + 1
    if A == 11:
        break
print(' ')

# continue salta al inicio del loop
print('Probemos continue')
while True:
    print('Cual es tu primer nombre ?')
    strNombre = input()
    if strNombre != 'Sergio':
        continue
    else:
        while True:
            print('Hola Sergio, cual es el password ? (es un reptil)')
            strPassword = input()
            if strPassword != 'tortuga':
                print('Password incorrecto')
                continue
            else:
                break
    break
print('Acceso permitido')




