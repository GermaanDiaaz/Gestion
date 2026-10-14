import numpy as np

aleatorio = np.random.randint(0, 11)
intentos = 0

while intentos < 3:
    num = int(input("Adivina el numero entre el 0 y el 10:\n"))
    intentos += 1
    if num == aleatorio:
        print("Acertaste")
        intentos = 3
    else:
        print("Fallaste, vuelve a intentarlo.\n")

print(f"El numero secreto es el: {aleatorio}")