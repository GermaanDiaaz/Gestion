print("Bienvenido a la aplicación de Germán de 'Calculadora de Sueño'\n")

descanso_hoy = 0.0
descanso_acumulado = 0.0
descanso_resultante = 0.0
siesta = 0.5
op = 0

while op != 3:
    print("Pulse 1 para Usar la calculadora de descanso semanal.")
    print("Pulse 2 para Ver el diagnóstico del desarrollador.")
    print("Pulse 3 para Salir del programa.")
    op = int(input("¿Qué desea hacer?\n"))

    match op:
        case 1:
            descanso_minimo = float(input("Introduzca el número de horas mínimas de sueño para una semana:\n"))

            while descanso_hoy >= 0:
                descanso_hoy = float(input("Introduzca el número de horas que ha dormido diariamente esta semana (valor negativo para salir): "))
                descanso_acumulado += descanso_hoy

            descanso_resultante = descanso_acumulado - descanso_minimo

            if descanso_resultante < 0:
                siestas = descanso_resultante / siesta
                print(f"Alerta de agotamiento, no cumples con el requisito mínimo de horas de sueño, puedes dormir {siestas} siestas de {siesta} horas para recuperar.")
            else:
                print("Estas cumpliendo con las horas mínimas de sueño requeridas.")

        case 2:
            num_bebidas = int(input("\n¿Cuántas bebidas con cafeina ha tomado hoy?\n"))

            if num_bebidas > 4:
                print("Escribiendo código a la velocidad de la luz/colapso inminente.")
            elif num_bebidas >= 2:
                print("Rendimiento óptimo.")
            else:
                print("Modo batería baja.")

            for _ in range(0, num_bebidas):
                print("¡Bugg!")

        case 3:
            print("\nGracias por usar el programa!!!")
        case _:
            print("\nEl número introducido no es válido.\n")

            









