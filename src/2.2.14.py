#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.





def comprobar_numero(numero) -> bool:
    try:
        int(numero)
    except ValueError:
        print("*Error*, intenta de nuevo.")
        return False
    return True


def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    numero = int
    cadena = 0
    while numero != 0:
        numero = input("Dame un numero entero: ")
        while comprobar_numero(numero) == False:
            numero = input("Dame un numero valido: ")
        numero = int(numero)
        cadena += numero
    print(f"La sumatoria de todos los numeros introducidos es: {cadena}")

if __name__=="__main__":
    main()