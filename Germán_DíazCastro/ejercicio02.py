print("Bienvenido al programa de analizarcadenas de texto\n")

op = 0

while op != 3:
    num_mayusculas = 0
    num_exclamaciones = 0
    print("Pulse 1 para Usar el detector de satisfacción.")
    print("Pulse 2 para Salir del programa.")
    op = int(input("¿Qué desea hacer?\n"))

    match op:
        case 1:
            frase = input("Introduzca la reseña:\n")

            for letter in frase:
                if letter.isupper():
                    num_mayusculas += 1
                elif letter == '!':
                    num_exclamaciones += 1

            porc_mayus = num_mayusculas * 100 /len(frase)
            print(f"El porcentaje de mayusculas es del {porc_mayus:.2f}%")

            if porc_mayus > 50 or num_exclamaciones > 3:
                print("ALERTA. El cliente está gritando o descontento\n")
            else:
                print("Cliente medianamente satisfecho\n")