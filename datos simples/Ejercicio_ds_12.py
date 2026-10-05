PRECIOPANDIA = 3.49
PRECIOPAN2 = round(PRECIOPANDIA *0.4 , 2)

TotalPANdia = float(input('Cuantas barras de pan que del dia has vendido: '))
TotalPAN2 = float(input('Cuantas barras de pan que no son del dia has vendido: '))
PrecioFinal = round((TotalPANdia * PRECIOPANDIA) + (TotalPAN2 * PRECIOPAN2), 2)

print(f'el precio de la barra de pan es de {PRECIOPANDIA}')
print(f'EL descuento por no ser de el dia es del 60% el coste por una barra que no es de el dia es de : {PRECIOPAN2}')
print(f'EL precio total es de : {PrecioFinal}')
