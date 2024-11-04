#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
#el dí­a correspondiente. 
# Si introducimos otro número nos da un error.

dia_numero = int(input("Ingresa el día de la semana (1-7): "))

if dia_numero == 1:
    dia = "Lunes"
elif dia_numero == 2:
    dia = "Martes"
elif dia_numero == 3:
    dia = "Miércoles"
elif dia_numero == 4:
    dia = "Jueves"
elif dia_numero == 5:
    dia = "Viernes"
elif dia_numero == 6:
    dia = "Sábado"
elif dia_numero == 7:
    dia = "Domingo"
else:
    dia = "ERROR: número incorrecto."

print(dia)
