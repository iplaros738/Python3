CantInvert= int(input("Que cantidad quieres invertir: "))
interesAnual = int(input("Digame su interes anual : "))
Años = int(input("y cuantos años: "))


for i in range(1, Años + 1):
    CantInvert += CantInvert * (interesAnual / 100)
    print(f"La cantidad invertida es : {round(CantInvert,2)} en el año {i}")

