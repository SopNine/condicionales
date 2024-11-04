
# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario. 
2
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num2 != 0:
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
else:
    print("Error: No se puede dividir entre cero.")
