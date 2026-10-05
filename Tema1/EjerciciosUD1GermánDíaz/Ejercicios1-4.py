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


"""-----------------------------Ejercicio P-P-T ----------------------------- """
print('¿Qué primera mano vas a jugar?')

print('Pulse 1 para jugar PIEDRA')
print('Pulse 2 para jugar PAPEL')
print('Pulse 3 para jugar TIJERA')
mano1 = input()

match mano1:
    case '1':
        print('¿Qué segunda mano vas a jugar?')

        print('Pulse 1 para jugar PIEDRA')
        print('Pulse 2 para jugar PAPEL')
        print('Pulse 3 para jugar TIJERA')
        mano2 = input()

        match mano2:
            case '1':
                print('Empate: La piedra rebota contra la otra piedra.')
            case '2':
                print('Gana el jugardor 2: La piedra es envuelta por el papel.')
            case '3':
                print('Gana el jugardor 1: La piedra rompe las tijeras.')
            case _:
                print('No hay más opciones esto no es Lagarto Spock.')
    case '2':
            print('¿Qué segunda mano vas a jugar?')
    
            print('Pulse 1 para jugar PIEDRA')
            print('Pulse 2 para jugar PAPEL')
            print('Pulse 3 para jugar TIJERA')
            mano2 = input()
    
            match mano2:
                case '1':
                    print('Gana el jugardor 1: La piedra es envuelta por el papel.')
                case '2':
                    print('Empate: El papel choca contra el papel')
                case '3':
                    print('Gana el jugardor 2: La tijera corta el papel.')
                case _:
                    print('No hay más opciones esto no es Lagarto Spock.')
    case '3':
                print('¿Qué segunda mano vas a jugar?')
        
                print('Pulse 1 para jugar PIEDRA')
                print('Pulse 2 para jugar PAPEL')
                print('Pulse 3 para jugar TIJERA')
                mano2 = input()
        
                match mano2:
                    case '1':
                        print('Gana el jugardor 2: La piedra rompe las tijeras.')
                    case '2':
                        print('Gana el jugardor 1: La tijera corta el papel.')
                    case '3':
                        print('Empate: Las tijeras no se pueden cortar entre sí.')
                    case _:
                        print('No hay más opciones esto no es Lagarto Spock.')
    case _:
        print('No hay más opciones esto no es Lagarto Spock.')
