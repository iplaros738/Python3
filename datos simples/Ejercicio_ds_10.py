PAYASOS = 0.112
MUNECA = 0.075  

Cpayasos = float(input('Digame la cantidad de payasos vendidos en el pedido: '))
Cmunecas = float(input('Digame la cantidad de munecas vendidos en el mismo pedido: '))

PesoPed = round((Cpayasos * PAYASOS) + (Cmunecas * MUNECA), 2)

print(f'El peso total de el pedido es: {PesoPed} kg' )
