import random

nombre = input('Koke: ¡Hola colchonero! ¿Cómo te llamas?\nTú: ')
equipos = ['FC Barcelona', 'Real Madrid', 'Rayo Vallecano']
equipo_aleatorio = random.choice(equipos)

print('Koke: Bienvenido al Civitas Metropolitano,', nombre,', estamos encantados de que un atlético como tú haya decidido acudir a nuestro estadio. \nHoy jugamos contra el',equipo_aleatorio,', así que esperamos presenciar un partidazo. Vamos a acercarnos a la puerta de entrada.')

input()

d1 = input('Frente Atlético: Todos los momentos que viví, todas las canchas donde te seguí...\nKoke: Como puedes ver, tenemos un ambientazo en los alrededores del estadio. Yo tengo que entrar a calentar. ¿Vienes o te quedas?\nTú: ')

if d1 == 'voy' or d1 == 'Voy':
    print('.\n.\n.\n.\n\nLlegas a tu asiento, empieza el partido y hay un seguidor del', equipo_aleatorio, 'que no para de criticar al Atleti.')
    d2 = input('¿Le dices algo o le ignoras?\n')
    if d2 == 'Le digo algo' or d2 == 'le digo algo':
        print('Asustas al aficionado rival y termina cambiándose de sitio.')
        input()
        d3 = float(input('El partido está muy aburrido, intentas sobornar a un aficionado para que salte al campo.\n¿Cuántos euros ofreces?\n'))
        precio = random.random()*100
        if d3 >= precio:
            print('Aficionado atlético: Hecho.')
            input()
            print('.\n.\n.\n.\n.\n')
            jugadores = ['Joao', 'Grizzi', 'Hermoso', 'Oblak', 'Carrasco', 'Reinildo', 'Cunha']
            jugador_aleatorio = random.choice(jugadores)
            print('El aficionado atlético salta al campo y se saca una foto con', jugador_aleatorio, '.\nA continuación, le detiene la policía, te delata y acabais los dos en el calabozo mientras te enseña la foto que se ha hecho.')
        else:
            print('Aficionado atlético: ¿De que vas?\nEl aficionado atlético llama a sus amigos y te dan una paliza.\n.\n.\n.\n\nDespiertas en el hospital.')
    else:
        print('El aficionado termina callándose y veis la primera parte del partido tranquilamente.')
        input()
        d3 = float(input('La segunda parte está muy aburrida, intentas sobornar a un aficionado para que salte al campo.\n¿Cuántos euros ofreces?\n'))
        precio = random.random()*100
        if d3 >= precio:
            print('Aficionado atlético: Hecho.')
            input()
            print('.\n.\n.\n.\n.\n')
            jugadores = ['Joao', 'Grizzi', 'Hermoso', 'Oblak', 'Carrasco', 'Reinildo', 'Cunha']
            jugador_aleatorio = random.choice(jugadores)
            print('El aficionado atlético salta al campo y se saca una foto con', jugador_aleatorio, '.\nA continuación, le detiene la policía, te delata y acabais los dos en el calabozo mientras te enseña la foto que se ha hecho.')
        else:
            print('Aficionado atlético: ¿De que vas?\nEl aficionado atlético llama a sus amigos y te dan una paliza.\n.\n.\n.\n\nDespiertas en el hospital.')
else:
    d2 = input('Te unes a un grupo de aficionados atléticos y comienzas a cantar con ellos. Se te acerca un policía.\nPolicía: ¿De qué equipo eres?\nTú: ')
    if d2 == 'Del atleti' or d2 == 'del atleti' or d2 == 'Del atlético de madrid' or d2 == 'Del Atlético de Madrid' or d2 == 'del atletico' or d2 == 'del atlético':
        print('Policía: Así me gusta. Aupa Atleti.\nContinúas cantando y terminas entrando al estadio.')
        input()
        print('.\n.\n.\n.\n.\nLlegas a tu asiento, empieza el partido y hay un seguidor del', equipo_aleatorio, 'que no para de criticar al Atleti.')
        d3 = input('¿Le dices algo o le ignoras?\n')
        if d3 == 'Le digo algo' or d3 == 'le digo algo':
            print('Asustas al aficionado rival y termina cambiándose de sitio.')
            input()
            d4 = float(input('El partido está muy aburrido, intentas sobornar a un aficionado para que salte al campo.\n¿Cuánto ofreces?\n'))
            precio = random.random()*100
            if d4 >= precio:
                print('Aficionado atlético: Hecho.')
                input()
                print('.\n.\n.\n.\n.\n')
                jugadores = ['Joao', 'Grizzi', 'Hermoso', 'Oblak', 'Carrasco', 'Reinildo', 'Cunha']
                jugador_aleatorio = random.choice(jugadores)
                print('El aficionado atlético salta al campo y se saca una foto con', jugador_aleatorio, '\nA continuación, le detiene la policía, te delata y acabais los dos en el calabozo mientras te enseña la foto que se ha hecho.')
            else:
                print('Aficionado atlético: ¿De que vas?\nEl aficionado atlético llama a sus amigos y te dan una paliza.\n.\n.\n.\n\nDespiertas en el hospital.')
        else:
            print('El aficionado termina callándose y veis la primera parte del partido tranquilamente.')
            input()
            d4 = float(input('La segunda parte está muy aburrida, intentas sobornar a un aficionado para que salte al campo.\n¿Cuánto ofreces?\n'))
            precio = random.random()*100
            if d4 >= precio:
                print('Aficionado atlético: Hecho.')
                input()
                print('.\n.\n.\n.\n.\n')
                jugadores = ['Joao', 'Grizzi', 'Hermoso', 'Oblak', 'Carrasco', 'Reinildo', 'Cunha']
                jugador_aleatorio = random.choice(jugadores)
                print('El aficionado atlético salta al campo y se saca una foto con', jugador_aleatorio, '\nA continuación, le detiene la policía, te delata y acabais los dos en el calabozo mientras te enseña la foto que se ha hecho.')
            else:
                print('Aficionado atlético: ¿De que vas?\nEl aficionado atlético llama a sus amigos y te dan una paliza.\n.\n.\n.\n\nDespiertas en el hospital.')
    else:
        print('Policía: Pues quedas arrestado por idiota.\nTe llevan al calabozo por no ser del atleti.')

goles_atleti = int(round(random.random()*10,0))
goles_visitante = int(round(random.random()*10,0))

input()

print('A los dos días, ya completamente recuperado, miras el resultado del partido.')

input()

if goles_atleti > goles_visitante:
    print('Ha ganado el atleti', goles_atleti, 'a', goles_visitante, '\nMereció la pena el sufrimiento. \nAUPA ATLETI')
elif goles_visitante > goles_atleti:
    print('Ha perdido el atleti', goles_atleti, 'a', goles_visitante, '\nNo fue un buen día ni para tí ni para el atleti.')
else:
    print('Empataron a', goles_atleti, '\nQué te esperabas, es el atleti.')

input('Escribe FIN para finalizar.\n')
