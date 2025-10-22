iniciar = input("Quisiera iniciar? (si/no):").lower()
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
        
if iniciar == "si": 
    print("""
1. Pedir datos del usuario
2. Pedir objetivo
3. Establecer cantidad ideal de calorías
4. Registrar datos de comidas
5. Salir
""")
    opcion = int(input("Elige tu opcion:"))

    continuar_prog = "si"  
    
    
    P = A = E = 0
    objetivo = ""
    calorias_ideales = 0

    while continuar_prog == "si":
        
        if opcion == 1:
            P = float(input("Dame tu peso en kg:"))
            A = float(input("Dame tu altura en cm:"))
            E = float(input("Dame tu edad:"))
            print ("Calorias recomendables para subir de peso:",(calorias_necesarias("subir",P,A,E)))
            print ("Calorias recomendables para bajar de peso:",(calorias_necesarias("bajar",P,A,E)))
            print ("Calorias recomendables para mantener peso:",(calorias_necesarias("mantener",P,A,E)))
            while True:
                continuar_prog = input("¿Guardar progreso? (si/no): ").lower()
                if continuar_prog == "si":
                    break
                elif continuar_prog == "no":
                    exit()
                else:
                    print("Opción inválida. Escribe 'si' o 'no'.")
           

        elif opcion == 2:
            while True:
                objetivo = input("Dime cual es tu objetivo (subir, bajar, mantener):").lower()
                if objetivo == "subir" or objetivo == "bajar" or objetivo == "mantener":
                    print("Objetivo", objetivo, "guardado correctamente.")
                    while True:
                        continuar_prog = input("¿Guardar progreso? (si/no): ").lower()
                        if continuar_prog == "si":
                            break
                        elif continuar_prog == "no":
                            exit()
                        else:
                            print("Opción inválida. Escribe 'si' o 'no'.")
                    break
                else: 
                    print("No existe la opcion")
       
        elif opcion == 3:
            if P and A and E and objetivo:
                calorias_ideales = calorias_necesarias (objetivo, P, A, E)
                print ("tu cantidad ideal de calorias:", calorias_necesarias(objetivo, P, A, E))
                while True:
                    continuar_prog = input("¿Guardar progreso? (si/no): ").lower()
                    if continuar_prog == "si":
                        break
                    elif continuar_prog == "no":
                        exit()
                    else:
                        print("Opción inválida. Escribe 'si' o 'no'.")
            else:
                print ("Primero ingresa tus datos")
           
        
            
        elif opcion == 4:
            if P == 0 or A == 0 or E == 0 or objetivo == "":
                print ("Primero ingresa tus datos")

            else:
                dias = []	
                total = 0
                continuar_dia = "si"
                while continuar_dia == "si":
                    print("Nuevo dia")
                    comidas_dia = []
                    total_dia = 0
                    continuar_comida = "si"
                    
                    while continuar_comida == "si":
                        while True:
                            comida = input("Comida del día (desayuno, comida, cena, snack): ").lower()
                            if comida in ["desayuno", "comida", "cena", "snack"]:
                                break  
                            else:
                                print("Opción inválida. Elige: desayuno, comida, cena o snack.")
                                
                        
                        calorias = float(input("Ingresa las calorías de la comida: "))
                        comidas_dia.append([comida,calorias])
                        total_dia = total_dia + calorias
                    
                        while True:
                            continuar_comida = input("¿Quieres seguir registrando comidas (si/no)?: ").lower()
                            if continuar_comida in ["si", "no"]:
                                break
                            else:
                                print("Opción inválida. Escribe 'si' o 'no'.")

                    
                    
                    dias.append(comidas_dia)
                    total = total + total_dia
                
                    print("Total de este día:", total_dia)
                    
                    if calorias_ideales > 0:
                        if objetivo == "subir":
                            if total_dia >= calorias_ideales:
                                print ("Lograste tu objetivo")
                            else:
                                print("No lograste el objetivo")
                        
                        elif objetivo == "bajar":
                            if total_dia <= calorias_ideales:
                                print ("Lograste tu objetivo")
                            else:
                                print("No lograste el objetivo")
                        
                        elif objetivo == "mantener":
                            if (total_dia >= calorias_ideales - 200) and (total_dia <= calorias_ideales + 200):
                                print ("Lograste tu objetivo")
                            else:
                                print ("No lograste el objetivo")
                    else: 
                        print("Aun no se establece cantidad ideal")
                            
                    
                    while True:
                        continuar_dia = input("¿Registrar otro día? (si/no): ").lower()
                        if continuar_dia == "si":
                            break
                        elif continuar_dia == "no":
                            exit()
                        else:
                            print("Opción inválida. Escribe 'si' o 'no'.")
                    
                    
                    while True:
                        continuar_prog = input("¿Guardar progreso? (si/no): ").lower()
                        if continuar_prog == "si":
                            break
                        elif continuar_prog == "no":
                            exit()
                        else:
                            print("Opción inválida. Escribe 'si' o 'no'.")
                            
               
                print ("calorias del dia:", total)  
            
        elif opcion == 5:
            print ("Adios")
            break
        
        else:
            print("opcion invalida")
        
        opcion = int(input("Elige tu opcion:"))

        
        
else:
    print("Okay")



            
	



