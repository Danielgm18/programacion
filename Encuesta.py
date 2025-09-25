#Autor: Daniel Gomez Mican
print("Nombre                               Proyecto")
print("---------------------------------------------")

for i in range(10):  
    N = input("Nombre: ")
    E = input("Proyecto: ")
    print(N.ljust(40, "-"), E)

