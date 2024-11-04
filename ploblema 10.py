#El director de una escuela está organizando un viaje de estudios, y requiere 
#determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
#viajes por el servicio. La forma de cobrar es la siguiente: 
#si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
#de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
#y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
#sin importar el número de alumnos. 
#Realice un programa que permita determinar el pago a la compañía de autobuses 
#y lo que debe pagar cada alumno por el viaje.

num_alumnos = int(input("Ingresa el número de alumnos: "))

costo_por_alumno = 0
pago_total = 0

if num_alumnos >= 100:
    costo_por_alumno = 65
elif 50 <= num_alumnos < 100:
    costo_por_alumno = 70
elif 30 <= num_alumnos < 50:
    costo_por_alumno = 95
else:
    costo_por_alumno = 4000
    num_alumnos = 1  

if num_alumnos < 30:
    pago_total = costo_por_alumno  
else:
    pago_total = costo_por_alumno * num_alumnos

print(f"Costo por alumno: {costo_por_alumno} euros")
print(f"Pago total a la compañía de autobuses: {pago_total} euros")
