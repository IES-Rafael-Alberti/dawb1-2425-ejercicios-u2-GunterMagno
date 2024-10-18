
def comprobar_numero(edad):
    try:
        int(edad)
    except ValueError:
        print("*Error*")
        return False
    return True




def main():

    edad = input("Dame tu edad: ")
    if comprobar_numero(edad) == True:
        edad = int(edad)
        if edad >= 18:
            print("Eres mayor de edad!!")
        else:
            print("Eres menor de edad")
            
if __name__=="__main__":
    main()