Algoritmo Control_Dieta
		Definir nombre Como Cadena
		Definir numComidas, i Como Entero
		Definir descripciones Como Cadena
		Definir cantidades Como Real
		
		Escribir "�Cu�l es tu nombre?"
		Leer nombre
		
		Escribir "Hola ", nombre, ", �cu�ntas comidas har�s hoy?"
		Leer numComidas
		
		Dimension descripciones[numComidas + 1]
		Dimension cantidades[numComidas + 1]
		
		Para i <- 1 Hasta numComidas Con Paso 1
			Escribir "Ingresa la descripci�n o tipo de la comida #", i, ":"
			Leer descripciones[i]  // aqu� ya es tipo Cadena
			
			Escribir "Ingresa la cantidad en gramos para la comida #", i, ":"
			Leer cantidades[i]     // aqu� ya es tipo Real
		Fin Para
		
		Escribir ""
		Escribir "Resumen de la dieta de ", nombre, ":"
		Para i <- 1 Hasta numComidas Con Paso 1
			Escribir "Comida #", i, ": ", descripciones[i], " - ", cantidades[i], " gramos"
		Fin Para
		
FinAlgoritmo



