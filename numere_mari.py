#Task 2 - + And * of large numbers

#Read numbers from txt file
try: 
    with open("numere.txt", "r") as file:
        numeros = file.read().splitlines()
    if len(numeros) != 2:
        print("En el documento debe haber solo 2 numeros. ERROR")
    elif not all(numero.isdigit() and len(numero) <= 200 and len(numero) > 0 for numero in numeros):
        print("ERROR: Los numeros deben tener entre 1 y 200 digitos.")
    else:
        num1 = numeros[0]
        num2 = numeros[1]

        print("First number:", num1)
        print("Second number", num2)
except FileNotFoundError:
    print("Error: No hay documento txt")