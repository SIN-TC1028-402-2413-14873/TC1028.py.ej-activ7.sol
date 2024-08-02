def main():
    #escribe tu código abajo de esta línea
    numero = int(input("Dame un número:"))

    if numero % 2 == 0:
        if numero > 0:
            print("El número es par positivo")
        else:
            print("El número es par negativo")
    else:
        if numero > 0:
            print("El número es impar positivo")
        else:
            print("El número es impar negativo")


if __name__=='__main__':
    main()
