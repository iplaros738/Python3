n = int(input("digame un numero : "))
divisores = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisores += 1

if divisores == 2:
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")