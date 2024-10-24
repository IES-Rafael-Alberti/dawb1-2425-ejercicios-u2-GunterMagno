def comprobar_numero(numero) -> bool:
    try:
        float(numero)
    except ValueError:
        print("*Error*, intenta de nuevo.")
        return False
    return True



def comprobar_negativo(numero:str) -> str:
    if numero.startswith("-"):
        print("El numero es negativo intenta de nuevo: ")
        return None



def comprobar_negativo(numero:str) -> str:
    if numero.startswith("-"):
        numero = numero[:1]
        return numero
    



def main():
    numero = input("Dame un numero entero")
    while comprobar_numero(numero) == False:

if __name__=="__main__":
    main()

def par(numero) -> bool:
    if numero % 2 == 0:
        return True
    elif numero % 2 == 1:
        return False