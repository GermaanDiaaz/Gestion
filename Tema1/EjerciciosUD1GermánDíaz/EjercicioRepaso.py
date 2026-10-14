print("Bienvenido al cajero automático del Ger")

saldo = float(input("Introduzca un saldo inicial:\n "))
op = 1
precio_entrada = 12.50

while op != 0:
    print(
        "\n¿Qué desea hacer?\n\n"
        "Pulse 1 para Ver saldo\n"
        "Pulse 2 para Retirar dinero\n"
        "Pulse 3 para Comprar entradas\n"
        "Pulse 4 para Ingresar dinero\n"
        "Pulse 0 para Salir"
    )
    op = int(input(""))

    match op:
        case 1:
            print(f"Su saldo actual es de: {saldo:.2f} €")

        case 2:
            retirar = float(input("¿Cúanto dinero desea retirar? "))
            if retirar > saldo:
                print("Saldo insuficiente en su cuenta corriente.")
            else:
                saldo -= retirar
                print("Operación realizadacon éxito.") 
        case 3:
            print(f"\nEl precio de la entrada es de: {precio_entrada:.2f}€")
            num_entradas = int(input("¿Cuántas desea comprar?"))
            precio_final = num_entradas * precio_entrada
            if precio_final > saldo:
                print("Saldo insuficiente en su cuenta corriente.")
            else:
                saldo -= precio_final
                print("Operación realizada con éxito.") 
        case 4:
            ingresar = float(input("¿Cúanto dinero desea ingresar?"))
            saldo += ingresar
            print("Operación realizadacon éxito.")
        case 0:
            print("Gracias por usar nuestro cajero.")
        case _:
            print("Operación inválida.")