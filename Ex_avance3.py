
def calorias_necesarias (objetivo,P,A,E):
	if objetivo == "subir":
		return  66.47 + (13.75 * P) + (5 * A) - (6.74 * E) + 500
	elif objetivo == "bajar":
		return 66.47 + (13.75 * P) + (5 * A) - (6.74 * E) - 500
	elif objetivo == "mantener":
		return 66.47 + (13.75 * P) + (5 * A) - (6.74 * E)
        
print (calorias_necesarias("subir",85,178,18))
print (calorias_necesarias("bajar",85,178,18))
print (calorias_necesarias("mantener",85,178,18))
	