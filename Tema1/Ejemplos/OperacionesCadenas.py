reaccion = 'Wow'

#Podemos multiplicar un String para duplicarlo
print(reaccion * 4)

#Podemos obtener un caracter del String indicando con corchetes su posición, también funciona al reves con negativos
print(reaccion[0])
print(reaccion[-1])


hola = 'Hola soy el Ger'

#Imprime tal cual, haciendo una 'COPIA'
print(hola[:])

#Borra desde el inicio el numero de caracteres indicado
print(hola[1:])
print(hola[9:])

#Borra desde el final dejando el numero de caracteres indicado
print(hola[:4])

#Borra del inicio y del final lo que le hayas indicado
print(hola[5:-3])

#Para contar el número de caracteres
print(len(hola))

#Para comprobar si una cadena pertenece a un String
print('Ger' in hola)
print('German' in hola)

#Para comprobar si una cadena NO pertenece a un String
print('Ger' not in hola)
print('German' not in hola)

#Para dividir un String en cadenas
print(hola.split())

#Podemos indicar qué queremos de separador
excepcion = 'Hola,soy,el,Ger'
print(excepcion.split(','))

#Divide en 3 partes siendo una el separador indicado
text = '3 + 4'
print(text.partition('+'))

#Limpia la cadena de espacios en blanco
hola2 = '\n \t Hola soy el Ger \t  \n'
print(hola2.strip())