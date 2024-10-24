#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def pedir_edad() -> int:
    edad = input("Dame tu edad: ")
    if comprobar_numero(edad) == False:
        edad = pedir_edad()
    return (edad)


def comprobar_numero(edad) -> bool:
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
    if edad < 16:
        print("La edad no puede ser inferior a 16!!, como eres menor de 16 no puedes tributar.")
        raise SystemExit
    if edad > 100:
        raise ValueError("La edad no puede ser superior a 100!!")
   

def pedir_ingresos() -> int:
    ingresos = input("Dame tus ingresos mensuales: ")
    if comprobar_ingresos(ingresos) == False:
        ingresos = pedir_ingresos()
    return (ingresos)    


def comprobar_ingresos(ingresos) -> bool:
    try:
        int(ingresos)
        ingresos = int(ingresos)
        test_ingresos(ingresos)
    except ValueError as e:
        if ingresos is None:
            print("*Error* , el numero introducido no es valido intentelo de nuevo")
            return False
        else:
            print(f"*Error*  {e}. Intentalo de nuevo")
            return False
    return True


def test_ingresos(ingresos):
    if ingresos < 0:
        raise ValueError("Los ingresos no pueden ser negativos!!")
    if ingresos < 1000:
        print("Los ingresos no pueden ser menor que 1000!!, no puedes tributar.")
        raise SystemExit



def main():
    edad = None
    ingresos = None
    while edad is None:
        edad = pedir_edad()
    while ingresos is None:
        ingresos = pedir_ingresos()
    print(f"Como tienes {edad} años y {ingresos} € mensuales de ingresos puedes tributar ")
    

if __name__=="__main__":
    main()