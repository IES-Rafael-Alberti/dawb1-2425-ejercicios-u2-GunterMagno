#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.


def comprobar_negativo(numero:str) -> str:
    if numero.startswith("-"):
        print("El numero es negativo intenta de nuevo: ")
        return False
    return True


def comprobar_numero(numero) -> bool:
    try:
        int(numero)
    except ValueError:
        print("*Error*, intenta de nuevo.")
        return False
    if comprobar_negativo(numero) == False:
        return False
    return True


def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    numero = int
    cadena = 0
    mayor = 0
    while numero != 0:
        numero = input("Dame un numero entero: ")
        while comprobar_numero(numero) == False:
            numero = input("Dame un numero valido: ")
        numero = int(numero)
        cadena += numero
        if numero > mayor:
            mayor = numero
    print(f"La sumatoria de todos los numeros introducidos es: {cadena} y el mayor numero introducido es {mayor}")


if __name__=="__main__":
    main()