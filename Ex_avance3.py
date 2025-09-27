opcion = input("Elige tu opcion:")
uno = "Pedir datos del usuario"
dos = "Pedir al usuario el objetivo"
tres = "Establecer cantidad ideal de calorias"
cuatro = "Registrar datos de sus comidas"
cinco = "Total calorias "


def calorias_necesarias (objetivo,P,A,E):
	if objetivo == "subir":
		return  66.47 + (13.75 * P) + (5 * A) - (6.74 * E) + 500
	elif objetivo == "bajar":
		return 66.47 + (13.75 * P) + (5 * A) - (6.74 * E) - 500
	elif objetivo == "mantener":
		return 66.47 + (13.75 * P) + (5 * A) - (6.74 * E)
	
total_calorias = 0
	
if opcion == "cuatro":
    continuar = "si"
    while continuar == "si":
        calorias = float(input("Ingresa las calorías de la comida:"))
        total_calorias = total_calorias + calorias
        print ("Tus calorias hasta ahora son:",total_calorias)
        continuar = input ("quieres seguir registrando comidas (si/no):")
      
           
print (calorias_necesarias("subir",85,178,18))
print (calorias_necesarias("bajar",85,178,18))
print (calorias_necesarias("mantener",85,178,18))
print ("calorias del dia:", total_calorias)

	
