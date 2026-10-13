print("Bienvenido a la calculadora más top del mercado. \n")

op = 1

while op != 0:
    num1 = float(input("Diga el primer número a operar: "))
    num2 = float(input("Diga el segundo número a operar: "))
    print('\nPulse 1 para SUMAR')
    print('Pulse 2 para RESTAR')
    print('Pulse 3 para MULTIPLICAR')
    print('Pulse 4 para DIVIDIR')
    print('Pulse 0 para SALIR')
    op = int(input("Selecciona una opción: "))

    match op:
        case 1:
            print(num1, "+", num2, "=", num1+num2)
        case 2:
            print(num1, "-", num2, "=", num1-num2)
        case 3:
            print(num1, "*", num2, "=", num1*num2)
        case 4:
            if num2 == 0:
                print("No se permitedividir entre 0.")
                break
            
            print(num1, "/", num2, "=", num1/num2)
        case 0:
            print("Gracias por usarel programa.")
        case _:
            print("El número introducido no es válido")    
        