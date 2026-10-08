fechaNac = input("Digame su fecha de nacimiento (Ej: dd/mm/aaaa): ")
separador = fechaNac.split("/")
print(f"el dia {separador[0]} del mes {separador[1]} de {separador[2]} es tu cumpleaños")