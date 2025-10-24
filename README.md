# Pensamiento computacional para Ingenieria

Este es un proyecto que va a ayudar a gestionar las calorias en las comidas de una persona en su dia a dia. La idea es registrar cada alimento ingerido junto con su cantidad y valor energético. A partir de estos datos, el algoritmo suma las calorías totales del día, las compara con el objetivo calórico establecido, por ejemplo, para bajar o subir de peso, y genera un reporte que muestra si la persona está dentro, por debajo o por encima de su meta. Creo que es interesante porque así se puede tener un registro exacto de lo que una persona ingiere en el día, y así poder tener un mejor control y salud de su cuerpo. 

# App gestor de calorias

Hoy en día mucha gente quiere cuidar su salud y su peso, pero no siempre es fácil saber cuántas calorías necesita o cuántas consume al día. Por eso este proyecto busca ayudar a llevar un control básico de las calorías de una persona usando un programa hecho en Python.

El programa permite que el usuario registre lo que come, calcule cuántas calorías debería consumir según su edad, peso y actividad, y compare si está cumpliendo su meta, ya sea subir, bajar o mantener su peso. También guarda los datos en un archivo para poder revisarlos después.

Además de servir como práctica para aprender a programar, este proyecto muestra cómo se pueden aplicar cosas como funciones, condiciones, ciclos, manejo de archivos y buenas prácticas de código (PEP 8). 

# Algortimo
Estado inicial

1. Pedir datos del usuario. (Peso, altura, edad y objetivo(subir,bajar o mantener peso))
   
2. Establecer una cantidad de calorias al dia ideales para el objetivo
   
3. Registrar datos de sus comidas
   
4. Salir 

Leer la opcion del usuario


Si opcion = 1

   Preguntar el peso (numero)
   
   Preguntar estatura (numero)
   
   Preguntar edad (numero)

   Preguntar objetivo (subir,bajar o mantener peso)


Si opcion = 2

  Establecer calorias ideales de acuerdo al objetivo con las siguientes formulas.
  
     Calcular calorias al dia con la formula si usuario selecciona Subir de peso
     66.47 + (13.75 x peso) + (5 x estatura) – (6.74 x edad) + 500
   
     Calcular calorias al dia con la formula si usuario selecciona Bajar de peso
     66.47 + (13.75 x peso) + (5 x estatura) – (6.74 x edad) - 500
   
     Calcular calorias al dia con la formula si usuario selecciona Mantener peso
     66.47 + (13.75 x peso) + (5 x estatura) – (6.74 x edad)

Si opcion = 3

  Inserte cantidad de calorias de su comida (numero)
  
  Guardar datos y sumarlos. 

  Determinar si se logro el objetivo. 
  

Si opcion = 4

Cerrar el programa

Estado final

#Referencias API 
"datetime" (https://docs.python.org/3/library/datetime.html): se usa para obtener la fecha actual.
