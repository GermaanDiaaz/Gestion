#aleatorio = random.randint(0, 10)
aleatorio =5
intentos = 0

while intentos < 3:
    num = int(input("Adivina el numero entre el 0 y el 10: "))
    intentos += 1
    if num == aleatorio:
        print("Acertaste")
        intentos = 3
    else:
        print("Fallaste, vuelve a intentarlo")

print("El numero secreto es el:", aleatorio)