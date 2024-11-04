# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta

def determinar_ganador(opcion1, opcion2):
    if opcion1 == opcion2:
        return "Empate"
    elif (opcion1 == "piedra" and opcion2 == "tijera") or \
         (opcion1 == "tijera" and opcion2 == "papel") or \
         (opcion1 == "papel" and opcion2 == "piedra"):
        return "Gana jugador 1"
    else:
        return "Gana jugador 2"

jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()

jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

opciones_validas = {"piedra", "papel", "tijera"}

if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
    print("Opción incorrecta. Debes elegir piedra, papel o tijera.")
else:
    resultado = determinar_ganador(jugador1, jugador2)
    print(resultado)
