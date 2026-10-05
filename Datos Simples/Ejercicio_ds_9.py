Cantidad = float(input('Digame su Cantidad a invertir : '))
IntA = float(input('Digame su Interes Anual : '))
Años = float(input('Digame su Cantidad de años : '))
CapitalTotal = round(Cantidad * (1+(IntA/100))**Años, 2)

print(f'el capital obtenido en la inversion es {CapitalTotal}')
