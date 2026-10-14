print("Bienvenido al cajero automático del Ger")

saldo = float(input("Introduzca un saldo inicial:\n "))
op = 1
precio_entrada = 12.50

while op != 0:
    print("\n¿Qué desea hacer?\n")

    print("Pulse 1 para Ver saldo")
    print("Pulse 2 para Retirar dinero")
    print("Pulse 3 para Comprar entradas")
    print("Pulse 4 para Ingresar dinero")
    print("Pulse 0 para Salir")
    op = int(input(""))

    match op:
        case 1:
            print("Su saldo actual es de:", f"{saldo:.2f}", "€")

        case 2:
            retirar = float(input("¿Cúanto dinero desea retirar? "))
            if retirar > saldo:
                print("Saldo insuficiente en su cuenta corriente.")
            else:
                saldo -= retirar
                print("Operación realizadacon éxito.") 
        case 3:
            print("\nEl precio de la entrada es de: ", f"{precio_entrada:.2f}", "€")
            num_entradas = int(input("¿Cuántas desea comprar?"))
            precio_final = num_entradas * precio_entrada
            if precio_entrada > saldo:
                print("Saldo insuficiente en su cuenta corriente.")
            else:
                saldo -= precio_final
                print("Operación realizadacon éxito.") 
        case 4:
            ingresar = float(input("¿Cúanto dinero desea ingresar?"))
            saldo += ingresar
            print("Operación realizadacon éxito.")
        case 0:
            print("Gracias por usar nuestro cajero.")
        case _:
            print("Operación inválida.")