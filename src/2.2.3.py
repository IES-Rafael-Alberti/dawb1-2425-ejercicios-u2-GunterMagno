#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


def par(numero) -> bool:
    if numero % 2 == 0:
        return True
    elif numero % 2 == 1:
        return False
    

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
    if par(numero) == True:
        numero = numero - 1
        while numero >= 0:
                cadena = ####### ARREGLARRR #####
                numero -= 2
               
                print(f"{cadena}" ,end=" ")
    else:
        while numero >= 0:
                print(f"{numero}, ", end="")
                numero -= 2


if __name__=="__main__":
    main()