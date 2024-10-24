def comprobar_numero(entrada: str) -> bool :
    if entrada.startswith("-"):
        entrada = entrada[-1]

    return entrada.isdigit()



def introducir_numero(msj: str):
    entrada = input(msj).strip().lower()

    if comprobar_numero(entrada):
        return True, int(entrada)
    else:
        if entrada == "fin":
            return True, None
        else:
            return False, None



def main():
    cont = 0 
    suma = 0
    media = 0

    encuentra_fin = False

    while not encuentra_fin:
        entrada_correcta, numero = introducir_numero("Introduzca un numero: ")
        if entrada_correcta and numero is not None:
            cont += 1
            suma += numero
        elif entrada_correcta and numero is None:
            encuentra_fin = True
        else:
            print("Entrada invalida")
    if cont > 0:
        media = suma/cont
    print("{}{}{}".format(suma,cont,media))


if __name__=="__main__":
    main()  