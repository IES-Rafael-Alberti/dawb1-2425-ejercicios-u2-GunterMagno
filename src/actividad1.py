
def comprobar_numero(valor:str):
    if valor.startswith("-"):
        valor = valor[-1]
    return valor.isdigit()


def introducir_numero():

def main():
    valor = None
    cantidad_numeros = 0
    media_numeros = 0

    while valor != "fin":
        valor = input("Introduzca un numero: ")
        si = comprobar_numero(valor)
    if si == True:
        cantidad_numeros += 1
        num = valor 
    else:
        pass


if __name__=="__main__":
    main()  