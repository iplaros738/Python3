numero = input("digame su numero con el prefijo (+34) y su extension (Ej:+34-667789803) :  ")
bloques = numero.split("-")

print(f"el numero de telefono es : {bloques[1]}")