Contrasenia = ("hola")
ContraseniaUsu = input("digame su contraseña :  ")


ContraseniaUsuMayus = ContraseniaUsu.upper
if (Contrasenia.lower() == ContraseniaUsu.lower() ) :
    print("su contraseña es igual que una de nuesra base de datos")
else :
    print("muy buena contraseña")