Interes = 0.04

DineroTotal = float(input('Cual es su dinero total actualemente : '))

ano1 = DineroTotal * (Interes + 1 )
ano2 = ano1 * (Interes + 1 )
ano3 = ano2 * (Interes + 1 )

print(f'Los ahorros desde el primer año han sido de : {round(ano1, 2)}')
print(f'Los ahorros desde el segundo año han sido de : {round(ano2, 2)}')
print(f'Los ahorros desde el tercer año han sido de : {round(ano3, 2)}')