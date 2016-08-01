__author__='Sergio Imeri'
# Funcion sencillisima
def hola():
    print('Hola')

hola()

def HolaNombre(Nombre):
    print('Hola ' + Nombre)

HolaNombre('Sergio')

print('Nombre a saludar?')
strNombre = input()
HolaNombre(strNombre)
print(' ')

# return regresa un valor a la llamada de la funcion
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'Uno'
    elif answerNumber == 2:
        return 'Dos'
    elif answerNumber == 3:
        return 'Tres'
    elif answerNumber == 4:
        return 'Cuatro'
    elif answerNumber == 5:
        return 'Cinco'

r = random.randint(1, 5)
print(r)
fortune = getAnswer(r)
print(fortune)
# Tambien podemos acortarlo asi:
print(getAnswer(r))


def hola(nombre):
    print('Hola', nombre)
    return 'Alberto'

hola('Sergio')
print(hola('Sergio'))





