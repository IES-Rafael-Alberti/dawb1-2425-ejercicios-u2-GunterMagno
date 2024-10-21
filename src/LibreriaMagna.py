def comprobar_numero(numero):
    try:
        float(numero)
    except ValueError:
        print("*Error*")
        return False
    return True



def comprobar_negativo(numero:str):
    if numero.startswith("-"):
        print("El numero es negativo intenta de nuevo: ")
        return None