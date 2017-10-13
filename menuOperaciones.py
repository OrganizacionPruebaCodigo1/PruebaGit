# Ingresar dos números enteros por pantalla.
# El usuario debe seleccionar la operación a realizar: suma, resta, multiplicación o división.
# Mostrar los resultados por pantalla.

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def getInt(message): # repite nuevamente que introduzcas el valor, si no es el adecuado o se escribió algo por error.
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("No es un entero! Intente de nuevo.")
       continue
    else:
       return userInput

num1=getInt( "Introduzca un valor entero para el operando 1:" )
num2=getInt( "Introduzca un valor entero para el operando 2:" )

print( "Opciones:\n1.- Suma\n2.- Resta\n3.- Multiplicación\n4.- Division" )

operaciones={ '1':suma, '2':resta, '3':multiplicacion, '4':division }

seleccion=input( 'Elija una opción:' )

try: # Pueden haber muchos try except
    resultado = operaciones[seleccion]( int(num1), int(num2) )
    print(resultado)
    cociente= num1/num2
except ZeroDivisionError:
   print("Error!: No se puede dividir por cero.")
except KeyError:
    print( "Error! No se encuentra o no se ha cargado la operación." )
