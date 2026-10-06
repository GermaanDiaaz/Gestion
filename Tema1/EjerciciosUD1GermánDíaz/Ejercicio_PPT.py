print('Bienvenido al juego de Piedra-Papel-Tijera. \n')

print('¿Qué primera mano vas a jugar?')

print('Pulse 1 para jugar PIEDRA')
print('Pulse 2 para jugar PAPEL')
print('Pulse 3 para jugar TIJERA')
mano1 = input()

match mano1:
    case '1':
        print('¿Qué segunda mano vas a jugar?')

        print('Pulse 1 para jugar PIEDRA')
        print('Pulse 2 para jugar PAPEL')
        print('Pulse 3 para jugar TIJERA')
        mano2 = input()

        match mano2:
            case '1':
                print('Empate: La piedra rebota contra la piedra.')
            case '2':
                print('Gana el jugardor 2: La piedra es envuelta por el papel.')
            case '3':
                print('Gana el jugardor 1: La piedra rompe las tijeras.')
            case _:
                print('No hay más opciones esto no es Lagarto Spock.')
    case '2':
            print('¿Qué segunda mano vas a jugar?')
    
            print('Pulse 1 para jugar PIEDRA')
            print('Pulse 2 para jugar PAPEL')
            print('Pulse 3 para jugar TIJERA')
            mano2 = input()
    
            match mano2:
                case '1':
                    print('Gana el jugardor 1: La piedra es envuelta por el papel.')
                case '2':
                    print('Empate: El papel choca contra el papel')
                case '3':
                    print('Gana el jugardor 2: La tijera corta el papel.')
                case _:
                    print('No hay más opciones esto no es Lagarto Spock.')
    case '3':
                print('¿Qué segunda mano vas a jugar?')
        
                print('Pulse 1 para jugar PIEDRA')
                print('Pulse 2 para jugar PAPEL')
                print('Pulse 3 para jugar TIJERA')
                mano2 = input()
        
                match mano2:
                    case '1':
                        print('Gana el jugardor 2: La piedra rompe las tijeras.')
                    case '2':
                        print('Gana el jugardor 1: La tijera corta el papel.')
                    case '3':
                        print('Empate: Las tijeras no se pueden cortar entre sí.')
                    case _:
                        print('No hay más opciones esto no es Lagarto Spock.')
    case _:
        print('No hay más opciones esto no es Lagarto Spock.')
