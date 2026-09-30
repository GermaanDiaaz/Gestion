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

"""-----------------------------Ejercicio 4 ----------------------------- """
num = input('Diga un número para comprobar si está entre 0 y 10: ')
if int(num) >=0 and int(num) <=10:
    print('El ',num, 'está entre el 0 y el 10')
else:
    print('El ',num, 'NO está entre el 0 y el 10')
