
def comprobar_numero(valor):
    if valor == float:
        print("Dato incorrecto")
        valor == False
    elif valor == int:
        valor == True
    else:
        print("Dato incorrecto")
        valor == False


def calcular_media():
    pass



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