#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.


def comprobar_negativo(numero:str) -> str:
    if numero.startswith("-"):
        numero = numero[1:]
        return numero
    return numero

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
    numero = input("Dame un numero entero: ")
    while comprobar_numero(numero) == False:
        numero = input("Dame un numero valido: ")
    numero = comprobar_negativo(numero)
    numero = int(numero)
    while numero > 0:
        print(f"{numero}, ", end="")
        numero -= 1
    print(f"{numero}.", end="")

            


if __name__=="__main__":
    main()