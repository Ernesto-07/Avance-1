opcion = int(input("Elige tu opcion:"))
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

dias = []	
total = 0
	
if opcion == 4:
    continuar_dia = "si"
    while continuar_dia == "si":
        print("Nuevo dia")
        comidas_dia = []
        total_dia = 0
        continuar_comida = "si"
        
        while continuar_comida == "si":
            comida = input ("Comida del dia (desayuno,comida,cena,snack): ")
            calorias = float(input("Ingresa las calorías de la comida: "))
            comidas_dia.append([comida,calorias])
            total_dia = total_dia + calorias
        
            continuar_comida = input ("quieres seguir registrando comidas (si/no):")
      
        dias.append(comidas_dia)
        total = total + total_dia
    
        print("Total de este día:", total_dia)
        continuar_dia = input("¿Registrar otro día? (si/no): ")
           
print (calorias_necesarias("subir",85,178,18))
print (calorias_necesarias("bajar",85,178,18))
print (calorias_necesarias("mantener",85,178,18))
print ("calorias del dia:", total)

	
	
	


