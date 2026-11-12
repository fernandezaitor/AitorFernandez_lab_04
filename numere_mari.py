#Task 2 - + And * of large numbers

def suma(num1, num2):
    resultado = ""
    llevada = 0
    i=len(num1) - 1
    j=len(num2) - 1

    while i >= 0 or j >= 0 or llevada:
        digito1 = int(num1[i]) if i >= 0 else 0
        digito2 = int(num2[j]) if j >= 0 else 0
        total = digito1 + digito2 + llevada
        resultado = str(total%10) + resultado
        llevada = total // 10

        i-=1
        j-=1
    return resultado.lstrip("0") or "0"

def multiplicacion(num1, num2):
    resultado = [0]*(len(num1)+len(num2))

    for i in range(len(num1) - 1, -1, -1):
        llevada = 0

        for j in range(len(num2) - 1, -1, -1):
            producto = int(num1[i]) * int(num2[j])
            total = producto + resultado[i+j+1] + llevada
            resultado[i+j+1] = total % 10
            llevada = total // 10
        resultado[i] += llevada
    numero_final = "".join(str(digito) for digito in resultado)
    return numero_final.lstrip("0") or "0"

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

        print("SUM:", suma(num1, num2))

        print("MUL:", multiplicacion(num1, num2))
except FileNotFoundError:
    print("Error: No hay documento txt")