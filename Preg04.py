#AUTOR: BERNAOLA MORENO PIERRE OSCAR

def invertir():
    num=input("Ingrese el numero a invertir: ")

    invertido=reversed(num)
    [char for char in reversed(num)]

    resultado="".join(invertido)
    print("El numero ivnertido es: ") 
    print(resultado)

invertir()