# Avance-7

**Se incluyeron listas para, además de sumar los datos de las comidas, se elija la comida del día donde se guardaran las calorías, así cada que se ingrese una comida del día le puedas asignar un valor de calorías, y en que comida del dia se esta comiendo (desayuno, comida,cena). Para el avance 7, se usa una lista anidada (dias), donde el elemento dentro es otra lista (comidas_dia). Así se guardan varios días, y en cada día varias comidas. Tambien te calcula el total diario y general cuando decides ya no registrar mas. **

Este es un proyecto que va a ayudar a gestionar las calorias en las comidas de una persona en su dia a dia. La idea es registrar cada alimento ingerido junto con su cantidad y valor energético. A partir de estos datos, el algoritmo suma las calorías totales del día, las compara con el objetivo calórico establecido, por ejemplo, para bajar o subir de peso, y genera un reporte que muestra si la persona está dentro, por debajo o por encima de su meta. Creo que es interesante porque así se puede tener un registro exacto de lo que una persona ingiere en el día, y así poder tener un mejor control y salud de su cuerpo. 
# Algortimo
Estado inicial

1. Pedir datos del usuario.

2. Pedir al usuario el objetivo (subir,bajar o mantener peso)
   
3. Establecer una cantidad de calorias al dia ideales para el objetivo
   
4. Registrar datos de sus comidas
   
5. Total de calorias
   
6. Salir 

Leer la opcion del usuario


Si opcion = 1

   Preguntar el peso (numero)
   
   Preguntar estatura (numero)
   
   Preguntar edad (numero)


Si opcion = 2
   Subir de peso (si/no)
   
   Bajar de peso (si/no)
   
   Mantener peso  (si/no)
   

Si opcion = 3

  Calcular calorias al dia con la formula si usuario selecciona Subir de peso
  66.47 + (13.75 x peso) + (5 x estatura) – (6.74 x edad) + 500

  Calcular calorias al dia con la formula si usuario selecciona Bajar de peso
  66.47 + (13.75 x peso) + (5 x estatura) – (6.74 x edad) - 500

  Calcular calorias al dia con la formula si usuario selecciona Mantener peso
  66.47 + (13.75 x peso) + (5 x estatura) – (6.74 x edad)

Mientras opcion = 4

  Inserte cantidad de calorias de su comida (numero)
  
  Guardar datos
  

Si opcion = 5

  Leer datos
  
  Sumar todos los datos y darle el resultado al usuario
  res = (Dato1 + Dato2 + Dato3 + Dato4 + Dato5 + Dato6)
  print(res)
     

Si opcion = 6 

Cerrar el programa

Estado final
  
