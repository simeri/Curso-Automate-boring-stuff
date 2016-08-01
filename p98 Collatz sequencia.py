__author__='Sergio Imeri'
# Secuencia de Collatz  https://en.wikipedia.org/wiki/Collatz_conjecture
# No importa el nuero entero ingresado, la secuencia siempre dará 1

def collatz(numero):
    if numero % 2 == 0:     # %modulo entonces numero es par
        print(numero, 'par, /2')
        numero = int(numero / 2)
        return(numero)
    else:
        print(numero, 'impar, *3+1')
        numero = 3 * numero +1
        return(numero)
            
print('Ingresa un entero positivo')
intIngreso = int(input())
intResultado=collatz(intIngreso)
contador = 1

while intResultado != 1:
    intResultado=collatz(intResultado) # llamaremos otra vez a collatz
    contador = contador + 1

print(intResultado, ' en ', contador, ' veces')
print('Enter para salir')
while True:
    enter = input()
    break



