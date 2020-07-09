#Autor: Gomez Flores Elias

nombre=input("ingrese nombre: ")
juntar = nombre.split(' ')

finnombre=""
for n in juntar:
    finnombre=finnombre+n


tamaño=len(finnombre)
print(tamaño)
