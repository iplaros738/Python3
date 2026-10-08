precio = input("digame el precio de un producto en euros: ")
separador = precio.split(",")
print(f"el numero de euros son {separador[0]} y  {separador[1]} centimos")