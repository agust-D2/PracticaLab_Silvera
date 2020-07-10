#autor: NATHAN SILVERA IÑIGO

numero = input("Ingrese numero: ")

i = 1
longitud = len(numero)
numeroalreves=""

while i <= longitud:
	numeroalreves = numeroalreves + numero[-i]
	i += 1 
print("Numero al reves: " + numeroalreves)