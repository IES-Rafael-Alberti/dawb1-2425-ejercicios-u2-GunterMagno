def comprobar_numero(edad):
    try:
        int(edad)
        edad = int(edad)
        test_edad(edad)
    except ValueError as e:
        if edad is None:
            print("*Error* , el numero introducido no es valido intentelo de nuevo")
            return False
        else:
            print(f"*Error*  {e}. Intentalo de nuevo")
            return False
    return True

def test_edad(edad):
    if edad == 0:
        raise ValueError("La edad no puede ser 0!!")
    if edad < 0:
        raise ValueError("La edad no puede ser negativa!!")
    if edad > 125:
        raise ValueError("La edad no puede ser superior a 125!!")

def escribir_años(edad):
    for i in range(1,edad+1):
        print(i)
        edad -= 1

def pedir_edad() -> int:
    edad = input("Dame tu edad: ")
    if comprobar_numero(edad) == True:
        escribir_años(edad)
    else:
        pedir_edad()
    return (edad)

def main():
    edad = None
    while edad is None:
        edad = pedir_edad()
        


if __name__=="__main__":
    main()