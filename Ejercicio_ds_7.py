peso = float(input("¿Cual es su peso?"))
altura = float(input("Digame su altura(en metros)"))
imc = peso/(altura ** 2)
print(f"su IMC es : {round(imc, 2)}")