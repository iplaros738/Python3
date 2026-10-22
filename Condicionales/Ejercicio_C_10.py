Pizza = input("Quiere pizza normal o vegetariana : ").lower()

if Pizza == "vegetariana" :
    ingrediente = input(f"de que quiere su pizza {Pizza} (Pimiento o tofu) seleccione solo uno : ")
    print (f"su pizza {Pizza} con tomate , mozarrella y {ingrediente} ")
else :
    ingrediente = input(f"de que quiere su pizza {Pizza} (Peperoni,Jamon o Salmon) seleccione solo uno :") 
    print (f"su pizza {Pizza} es con tomate , mozarrella y {ingrediente} ")