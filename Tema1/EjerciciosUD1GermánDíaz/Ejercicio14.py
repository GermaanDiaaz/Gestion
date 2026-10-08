num = input('Diga un número para pintar su triángulo de asteriscos: ')
asteriscos = 0

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
   