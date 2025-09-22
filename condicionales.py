#Caracter em le codigo ASCII
'''
X=int(input("Escribe el numero correspondiente a ASCII: "))
X1=(chr(X))
if X1 in "aeiou":
    print(f"El número {X} corresponde a la vocal minúscula '{X1}'.")
else:
    print(f"El número {X} NO corresponde a una vocal minúscula.")
#Numero real positivo negativo o neutro
X3=int(input("Ingresa un numero real: "))
if(X3>0):
    print(f"El número {X3} es positivo")
elif(X3<0):
    print(f"El número {X3} es negativo")
else:
    print(f"El número {X3} es neutro")
'''
#
def pertenece_circulo(h, k, r, x, y):
    distancia2 = (x - h)**2 + (y - k)**2
    
    if distancia2 < r**2:
        print(f"El punto ({x}, {y}) está dentro del círculo.")
    elif distancia2 == r**2:
        print(f"El punto ({x}, {y}) está en la circunferencia del círculo.")
    else:
        print(f"El punto ({x}, {y}) está fuera del círculo.")

h = float(input("Ingrese la coordenada x del centro: "))
k = float(input("Ingrese la coordenada y del centro: "))
r = float(input("Ingrese el radio del círculo: "))
x = float(input("Ingrese la coordenada x del punto: "))
y = float(input("Ingrese la coordenada y del punto: "))

pertenece_circulo(h, k, r, x, y)
