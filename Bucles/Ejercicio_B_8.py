n = int(input("Introduce un número entero positivo: "))

# Recorre los números impares desde 1 hasta n (sumando 2 en cada vuelta)
for i in range(1, n + 1, 2):
    # Imprime desde el impar actual hasta 1 (restando 2)
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()  # Salto de línea al terminar la fila