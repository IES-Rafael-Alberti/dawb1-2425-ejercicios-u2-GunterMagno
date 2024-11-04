#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def girar_palabra(palabra :str):
    cadena = ""
    palabra = palabra.strip()
    for i in palabra:
        cadena += i + " "
    print(cadena[::-1])

def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    palabra = input("Dame una palabra: ")
    girar_palabra(palabra)


if __name__=="__main__":
    main()
