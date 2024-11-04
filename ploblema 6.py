#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cadena = input("Ingresa una cadena: ")

if len(cadena) == 1 and cadena.isupper():
    print("Es una letra mayúscula.")
else:
    print("No es una letra mayúscula.")
