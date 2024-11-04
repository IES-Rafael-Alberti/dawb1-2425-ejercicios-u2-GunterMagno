#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.


def veces_que_aparece(frase,letra):
    contador = 0
    for i in frase:
        if i == letra:
            contador += 1
    print (f"La letra -> {letra} <- aparece {contador} en la frase.")




def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    frase = input("Dame una frase: ")
    letra = input("Dame una letra: ")
    veces_que_aparece(frase,letra)


if __name__=="__main__":
    main()