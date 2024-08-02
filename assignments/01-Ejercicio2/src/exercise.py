'''
Programa de triangulos
'''
def main():
    '''
        Programa principal
    '''
    #escribe tu código abajo de esta línea
    x = float(input("Dame el valor de X:"))
    y = float(input("Dame el valor de y:"))
    z = float(input("Dame el valor de z:"))

    if not ((x > 0) and (y > 0) and (z > 0))and(((x+y)>z) or ((x+z)>y) or ((y+z)>x)):
        print("Los lados no corresponden a un triangulo")
    else:
        if ((x==y) and (y==z) and (z==x)):
            print("El triangulo es equilatero")
        elif (x==y and z != x) or (x==z and y != x) or (y==z and x !=y):
            print("El triangulo es isosceles")
        else:
            print("El triangulo es escaleno")
            
if __name__=='__main__':
    main()
