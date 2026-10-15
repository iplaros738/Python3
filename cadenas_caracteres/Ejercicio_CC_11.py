producto = input("Introduce el nombre  de el producto, precio y unidades (todo seguido separa por , en la misma cadena EJ: pan,1.2€,2): ")

separador = producto.split(",")

precio = float(separador[1])
cantidad = int(separador[2])
coste = precio * cantidad

print (f"EL precio unitario de {separador[0]} es {precio:09.2f}  se llevara un total de {cantidad:03} el coste total sera : {coste:.2f} ")