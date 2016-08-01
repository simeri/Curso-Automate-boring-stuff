__author__='sergio.imeri'
""" pagina 36 - Primer programa """

print('Cual es tu nombre ? ')
miNombre = input()              # Preguntar por el nombre
print('Mucho gusto ', miNombre)
largoNombre = len(miNombre)
print('El largo de tu nombre es de ', largoNombre, ' posiciones')
print()
print('Cual es tu edad ?')
miEdad = input()
print('Tendrás ' + str(int(miEdad) + 1) + ' en un año')
print('Tendras', int(miEdad)+1, 'en un año')

