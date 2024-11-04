#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    print("")


def comprobar_numero(numero) -> bool:
    try:
        int(numero)
    except ValueError:
        print("*Error*, intenta de nuevo.")
        return False
    return True


def pedir_numero():
    numero = input("Dame un numero entero: ")
    while comprobar_numero(numero) == False:
        numero = input("Dame un numero valido: ")
    return int(numero)


def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    numero = pedir_numero()
    tabla_multiplicar(numero)


if __name__=="__main__":
    main()
