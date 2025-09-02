# Autor Daniel Gómez Micán

#
#print ("hola")

#definición a problemas

#solucion a problermas

#algoritmos 

#encuentre el valor de x en la siguiente ecuacion

# AX = B - Z
print("Vamos a solucionar la ecuacion AX = B - Z, por favor inserta los valores")
A= int(input("El valor de la variable A es:"))
B= int(input("El valor de la variable B es:"))
Z= int(input("El valor de la variable Z es:"))

#Despues de los valores dar el resultado de la ecuación
D= B - Z
print("Ax=",(D))
D1= D / A
print("x=", D1)
print("El valor de x es:", D1)

#Conversiones str,int y float
print("Vamos hacer converciones entre str, int, float")
C=str(input("Dar valor a la variable C:"))
print(type(C),C)
#De str a int
C1=int(C)
print(type(C1),C1)
#De int a float
C2=float(C1)
print(type(C2),C2)
#De float a int
C3=int(C2)
print(type(C3),C3)
#De int a str
C4=str(C3)
print(type(C4),C4)
#De str a float
C5=float(C4)
print(type(C5),C5)
#De float a str
C6=str(C5)
print(type(C6),C6)

#Esrtructura de control, operaciones logicas
E=int(input("Inserta el valor a la variable E:"))
#Booleano, 1,0
#E>X
if(E>5):
    print("este es el resultado de if verdadero")
    print("la variable E es mayor a 5")
else:
   print("la condicion no se ejecuto")
   print("la variable E no es mayor a 5")
E1=int(input("Inserta el valor a la variable E1:"))   
#E1<X
if(E1<9):
  print("este es el resultado de if verdadero")
  print("La variable E1 es menor a 9")
else:
   print("la condicion no se ejecuto")
   print("la variable E1 no es mayor a 9")
#E2<=X
E2=int(input("Inserta el valor a la variable E2:"))
if(E2<=6):
   print("Este es el resultado de if verdadero")
   print("la variable E2 es menor o igual a 6")
else:
   print("la condicion no se cumple")
   print("la variable E2 no es menor o igual a 6")
#E3>=x
E3=int(input("Inserta el valor a la variable E3:"))
if(E3>=3):
   print("este es el resultado de if verdadero")
   print("la variable E3 es mayor o igual a 3")
else:
   print("la condicion no se cumple")
   print("la variable E3 no es mayor o igual a 3")
#E4==X
E4=int(input("Inserta el valor a la variable E4:"))
if(E4==8):
   print("este es el resultado de if verdadero")
   print("la variable E4 es igual a 8")
else:
   print("la condicion no se cumple")
   print("la variable E4 no es igual a 8")
#E5=!X
E5=int(input("Inserta el valor a la variable E5:"))
if(E5!=4):
   print("este es el resultado de if verdadero")
   print("la variable E5 es diferente a 4")
else:
    print("la condicion no se cumple")
    print("la variable E5 no es diferente a 4")
