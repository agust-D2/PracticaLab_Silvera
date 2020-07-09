# Autor: Jose Orlando Ramos Machuca

def correoUntels(correo):
    correo = correo.lower()
    
    if "@untels.edu.pe" in correo:
        return "Si es correo de untels."
    else:
        return "No es correo de la untels."
    
correo = input("Ingrese un correo: ")
print(correoUntels(correo))