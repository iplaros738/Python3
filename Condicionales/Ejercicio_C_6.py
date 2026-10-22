Nombre = input("Digame su nombre : " ).lower()
Sexo = input("Digame su sexo (Ej: masculino/femenino) :  (" ).lower()

if Sexo == "femenino" and  Nombre <= "m" :
    print("Grupo A")
else :
    print("Grupo B")