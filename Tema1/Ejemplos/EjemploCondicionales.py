temperature = 40

if temperature > 35:
    print('Aviso alta temperatura')
elif temperature > 40:
    print('Temperaturas extremas')
else:
    print('Parametros normales')


#----------Esto ya no se hace----------
if temperature > 30:
    fire_risk = 'LOW'
else:
    fire_risk = 'HIGH'

#------Mejor esta forma, hacerlo a partir de ahora---------
fire_risk = 'LOW' if temperature < 30 else 'HIGH'


canFly = False
isHuman = True
hasMask = False

if canFly:
    if isHuman:
        if hasMask:
            print('Ironman')
        else:
            print('Captain Marvel')
    else:
        if hasMask:
            print('Ronan')
        else:
            print('Vision')
else:
    if isHuman:
        if hasMask:
            print('Spiderman')
        else:
            print('Hulk')
    else:
        if hasMask:
            print('Black Bolt')
        else:
            print('Thanos')