#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def limpiar_consola():
    import os
    os.system("cls")
    

def main():
    limpiar_consola()
    palabra = input("Dame una palabra: ")
    for i in range(10):
        print (palabra)

if __name__=="__main__":
    main()