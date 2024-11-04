#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.


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
    numero = input("Dame un numero entero positivo: ")
    while comprobar_numero(numero) == False:
        numero = input("Dame un numero valido: ")
    suma_digitos = 0
    for digito in numero:
        suma_digitos += int(digito)
    print(f"{suma_digitos}")

########### MI NO ENTENDER ENUNCIADO ####################

if __name__=="__main__":
    main()