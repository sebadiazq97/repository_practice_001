Proceso curso_de_alumnos
	Definir alumnos, nota,i, opcion, suma, contador, aprobados, reprobados Como Entero;
	
	Repetir
		aprobados = 0;
		reprobados = 0;
		Escribir "Bienvenido a la super IA para rajar alumnos";
		Escribir "1.Revisar alumnos aprovados";
		escribir "2.Salir";
		Escribir "Opcion: ";
		Leer opcion;
		
		si opcion >= 3 o opcion <1 Entonces
			Escribir "";
			Escribir "Tienes 2 opciones y eliges la que no es wn,hazlo otra vez";
			Escribir "";
		FinSi
		
		si opcion = 1 Entonces
			Escribir "Escriba el numero de alumnos:";
			Leer alumnos; 
			
			Para i <- 1 Hasta alumnos Hacer
				
				Repetir
					Escribir "Ingrese nota:";
					Leer nota;
					
					si nota <1 o nota >7 Entonces
						Escribir "";
						Escribir "Ya pues, si sabes que son del 1 al 7, no molestes";
						Escribir "";
						
					FinSi
				Hasta Que nota >=1 Y nota <=7
				
				Si nota >=4 Entonces
					Escribir "Aprobado";
					aprobados = aprobados + 1;
				
					//sumar aprobados
				SiNo
					Escribir "Reprobado";
					reprobados = reprobados + 1;
					//sumar reprobados
				FinSi
				
				
				
			FinPara
			
			Escribir "===========";
			Escribir "Resultados";
			Escribir "===========";
			Escribir "";
			Escribir "aprobados ",aprobados;
			Escribir "reprobados ",reprobados;
			Escribir "";
			
			
			//mostrar resultados
			
		FinSi
		
	Hasta Que opcion = 2
	
FinProceso
