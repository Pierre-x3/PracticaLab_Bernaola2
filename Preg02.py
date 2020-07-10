#AUTOR: BERNAOLA MORENO PIERRE

def comparar():
    
    variable = input("Ingrese correo de la untels: ")
    
    untels = "untels.edu.pe"
    
    if variable.split("@")[1] == untels:
        print("ES CORREO DE LA UNIVERSIDAD")
    else:
        print("NO ES CORREO DE LA UNIVERSIDAD")
        
comparar()