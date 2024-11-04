#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


def pedir_y_comprobar(contraseña):
    contraseña_puesta = input("Introduce la contraseña: ").strip()
    while contraseña != contraseña_puesta:
        contraseña_puesta = input("Contraseña incorrecta, prueba de nuevo: ")
    return True

def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    contraseña = "aceituna"
    if pedir_y_comprobar(contraseña) == True:
        print("Contraseña correcta")


if __name__=="__main__":
    main()