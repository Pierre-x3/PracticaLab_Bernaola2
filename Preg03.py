#Autor: Giampierre Huaman Berru

def contador():
    
    texto = input("Ingrese texto: ")
    espacio = " "
    print( len([letra for letra in texto if letra not in espacio]))


contador()