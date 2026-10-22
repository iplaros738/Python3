RentaA = int(input("Cual es su renta anual: " ))

if RentaA < 10000 :
    print(f"el ripo impositivo cobrando {RentaA} es 5%")
elif RentaA < 20000:
    print(f"el ripo impositivo cobrando {RentaA} es 15%")
elif RentaA < 35000:
    print(f"el ripo impositivo cobrando {RentaA} es 20%")
elif RentaA < 60000:
    print(f"el ripo impositivo cobrando {RentaA} es 30%")
elif RentaA > 60000:
    print(f"el ripo impositivo cobrando {RentaA} es 45%")