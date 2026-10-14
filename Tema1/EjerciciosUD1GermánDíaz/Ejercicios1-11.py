"""-----------------------------Ejercicio 1 ----------------------------- """
print('Hola Mundo!!')


"""-----------------------------Ejercicio 2 ----------------------------- """
a = 4
b = 9

c = a + b

print('El resultado es: ', c)


"""-----------------------------Ejercicio 3 ----------------------------- """
producto = input('Diga el precio del producto: ')
cien = 100
iva = 21

precio_final = float(producto) + float(producto)*iva/cien

print('El precio fianl es: 'f'{precio_final:.2f}''€')


"""-----------------------------Ejercicio 4 ----------------------------- """
num1 = input('Diga el número a comparar: ')
num2 = input('Diga el otro número: ')

if num1 > num2:
    print('El ',num1, 'es mayor que el ', num2)
elif num2 > num1: 
    print('El ',num2, 'es mayor que el ', num1)
else:
    print('El ',num2, 'es igual que el ', num1)


"""-----------------------------Ejercicio 5 ----------------------------- """
num = input('Diga un número para comprobar si está entre 0 y 10: ')
if int(num) >=0 and int(num) <=10:
    print('El ',num, 'está entre el 0 y el 10')
else:
    print('El ',num, 'NO está entre el 0 y el 10')


"""-----------------------------Ejercicio 6 ----------------------------- """
num = input('Diga un número para comprobar si está entre 0-10, 11-20 o 21-30: ')
if int(num) >=0 and int(num) <=10:
    print('El ',num, 'está entre el 0 y el 10')
elif int(num) <= 20:
    print('El ',num, 'está entre el 11 y el 20')
elif int(num) <= 30 and int(num) > 20:
    print('El ',num, 'está entre el 21 y el 30')
else:
    print('El ',num, 'NO está en ningún segmento')


"""-----------------------------Ejercicio 7 ----------------------------- """
num = 1
while num <=100:
    print(num)
    num = num + 1


"""-----------------------------Ejercicio 8 ----------------------------- """
num = 1
lim = 100
for _ in range(num, lim+1):
    print(num)
    num = num + 1


"""-----------------------------Ejercicio 9 ----------------------------- """
cadena = input("Introduzca un texto paran separar sus palabras:\n")

print(cadena.split(' '))


"""-----------------------------Ejercicio 11 ----------------------------- """
tope = int(input("Introduzca un número tope:\n"))
resultado = 0
lista = ""

while resultado < tope:
    num = int(input("Introduzca un número para alcanzar el tope: "))
    resultado += num
    lista += " " + str(num)

    if resultado == tope:
        print("Felicidades, encontraste el tope.")
        print(lista)
    elif resultado > tope:
        print("Vaya... Te pasaste del tope.")
        print(lista)
    else:
        print("Vas por", resultado, "aún no alcanzas el tope.")


"""-----------------------------Ejercicio 13 ----------------------------- """
num = int(input("Introduce un número para calcular su factorial:\n"))
result = 1

for i in range(1, num+1):
    result *= i
print(f"El número {num}! = {result}")