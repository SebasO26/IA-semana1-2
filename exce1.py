numeros = []

numero = int(input("Ingrese el primer número: "))
numeros.append(numero)

numero = int(input("Ingrese el segundo número: "))
numeros.append(numero)

numero = int(input("Ingrese el tercer número: "))
numeros.append(numero)

for i in range(len(numeros)):
    for j in range(0, len(numeros) - i - 1):
        if numeros[j] > numeros[j+1]:
            aux = numeros[j]
            numeros[j] = numeros[j+1]
            numeros[j+1] = aux

for numero in numeros:
    print("\n", numero)