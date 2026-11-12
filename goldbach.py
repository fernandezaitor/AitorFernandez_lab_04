#1 - Goldbachs Conjecture // Read an even number greater than 2

# Comprobamos que un numero es primo
def primo(numero):
    if numero <2:
        return False
    for i in range (2, numero): 
        if numero % i == 0:
            return False
    return True

try:
    n = int(input("Introduce un numero par mayor que 2: "))
    if n<=2 or n%2 != 0 :
        print("El numero introducido no es valido")
    else: 
        print("El numero introducido es valido: ", n)
        for p in range(2, n//2+1):
            q=n-p
            if primo(p) and primo(q):
                print(p, "+", q, "=", n)

except ValueError:
    print("Error: Introduce un entero valido")

#print("Es el numero 7 primo??", primo(7))
#print("Es el numero 10 primo?", primo(10))
