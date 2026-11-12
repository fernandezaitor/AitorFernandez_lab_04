#1 - Goldbachs Conjecture // Read an even number greater than 2

try:
    n = int(input("Introduce un numero par mayor que 2: "))
    if n<=2 or n%2 != 0 :
        print("El numero introducido no es valido")
    else: print("El numero introducido es valido: ", n)
except ValueError:
    print("Error: Introduce un entero valido")