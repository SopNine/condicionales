#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error

mes = int(input("Ingresa un número de mes (1-12): "))

if mes == 1:   
    dias = 31
elif mes == 2: 
    dias = 28  
elif mes == 3: 
    dias = 31
elif mes == 4: 
    dias = 30
elif mes == 5:
    dias = 31
elif mes == 6: 
    dias = 30
elif mes == 7: 
    dias = 31
elif mes == 8:
    dias = 31
elif mes == 9: 
    dias = 30
elif mes == 10:
    dias = 31
elif mes == 11: 
    dias = 30
elif mes == 12: 
    dias = 31
else:
    dias = "ERROR: número incorrecto."

print(f"Número de días en el mes {mes}: {dias}")
