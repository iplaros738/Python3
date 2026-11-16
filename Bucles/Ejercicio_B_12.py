frase = input("Digame una frase : ")
letra = input("Cual es la la letra que quieres buscar?: ")

contador = 0
for i in range(len(frase)-1,-1,-1):
    if frase[i] ==letra :
        contador += 1

print(f"aparece un total de {contador}")