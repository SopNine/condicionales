# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.

usuario = input("Ingresa el nombre de usuario: ")
contraseña = input("Ingresa la contraseña: ")

if usuario == "pepe" and contraseña == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error: Usuario o contraseña incorrectos.")
