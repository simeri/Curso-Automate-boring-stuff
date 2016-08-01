# probemos if else elif
print('Nombre ?')
strNombre = input()

if strNombre == 'Sergio' or strNombre == 'sergio':
    print('Edad ?')
    intEdad = int(input())
    if intEdad == 50:
        print('Hola Sergio')
    elif intEdad > 150:
        print('Eres un muerto viviente vampiro !!')
    elif intEdad > 50:
        print('No eres Sergio, abuelo')
    else:
        print('No eres Sergio, niño')
else:
    print('No eres Sergio')






