
def crear_linea(num: int):
    suma = 0
    cadena = ""
    for i in range(num+1):
        suma += i

        if cadena == "":
            cadena = str(i)
        else:
            cadena = cadena + " + " + str(i)
    if num != 0:
        linea = f"{num} => {cadena} = {suma}"
    else:
        linea = f"{num} => {cadena} = {suma}"


    return linea

def crear_piramide(num, order):
    piramide = ""
    if order == 1:
        for i in range(0, num+1):
            x = num-i
            if x != 0:
                piramide += crear_linea(x) + "\n"
            else:
                piramide += crear_linea(x)
    elif order == -1:
        for i in range(num):
            piramide += crear_linea(i+1) + "\n"
    
    return piramide
        

def validar_numero(num: str):
    try:
        num = int(num)

        if num < 0 or num > CONSTANTE:
            return False
        else:
            return num
    except ValueError:
        return False

def introducir_numero() -> int:
    num = False
    while num == False:
        num = input("Introducir número: ").strip()
        num = validar_numero(num)
        if num == False:
            print("[-] ERROR: Has introducido un número incorrecto")
    return num

def main():
    num = introducir_numero()
    piramide_1 = crear_piramide(num, 1)
    print(piramide_1)
    piramide_2 = crear_piramide(num, -1)
    print(piramide_2)
    

if __name__ == '__main__':
    CONSTANTE = 20
    main()