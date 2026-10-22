Puntos = float(input("Cual es su puntuacion en la Empresa: " ))
salarioF = 0

if Puntos == 0.0 :
    salarioF = 2400 * 0.0
    print(f"SU nivel  de rendimiento es inaceptable  y el salario que recibira sera : {salarioF}")
elif Puntos == 0.4 :
    salarioF = 2400 * 0.4
    print(f"SU nivel  de rendimiento es inaceptable  y el salario que recibira sera : {salarioF}")
elif Puntos >= 0.6 :
    salarioF = 2400 * 0.6
    print(f"SU nivel  de rendimiento es inaceptable  y el salario que recibira sera : {salarioF}")
