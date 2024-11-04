#Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
#al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#(dato cadena) de la cara opuesta al resultado obtenido.
#* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
#1-6, 2-5 y 3-4.
#* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
#se mostrará el mensaje: "ERROR: número incorrecto.".

def numero_a_palabra(num):
    palabras = {
        1: "uno",
        2: "dos",
        3: "tres",
        4: "cuatro",
        5: "cinco",
        6: "seis"
    }
    return palabras.get(num)

resultado = int(input("Ingresa el resultado del dado (1-6): "))

if resultado < 1 or resultado > 6:
    print("ERROR: número incorrecto.")
else:
    if resultado == 1:
        opuesta = 6
    elif resultado == 2:
        opuesta = 5
    elif resultado == 3:
        opuesta = 4
    elif resultado == 4:
        opuesta = 3
    elif resultado == 5:
        opuesta = 2
    elif resultado == 6:
        opuesta = 1
    
    opuesta_palabra = numero_a_palabra(opuesta)
    print(f"La cara opuesta al {resultado} es {opuesta_palabra}.")
