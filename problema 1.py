
# Programa que pida dos números e indique Cuál es el mayor
# Si los dos son iguales que muestre el mensaje "Son iguales"

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num1 > num2:
    print("El primer número es mayor:", num1)
elif num2 > num1:
    print("El segundo número es mayor:", num2)
else:
    print("Son iguales")
