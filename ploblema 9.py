#Programa que pida tres números y los muestre ordenados (de mayor a menor)

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

numeros = [num1, num2, num3]

numeros.sort(reverse=True)

print("Los números ordenados de mayor a menor son:", numeros)
