num = int(input('Diga un número para pintar su triángulo de asteriscos: '))

for i in range(1, num+1):
    print("*" * i)
    
for i in range(num-1, 0, -1):
    print("*" * i)



"""asteriscos = 0

repes = int(num) * 2 

if int(num) >= 0:

    while repes != 0:
        if repes <= int(num):
            asteriscos = asteriscos - 1
            print('*' * asteriscos)
            repes = repes - 1

        else:
            asteriscos = asteriscos + 1
            print('*' * asteriscos)
            repes = repes - 1
"""