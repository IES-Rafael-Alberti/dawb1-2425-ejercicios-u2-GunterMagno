#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    palabra = input("")
    cadena = ""
    while palabra != "salir":
        cadena += palabra  + " "
        palabra = input("")
    print(cadena)
if __name__=="__main__":
    main()