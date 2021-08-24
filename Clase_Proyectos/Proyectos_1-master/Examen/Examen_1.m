menu = "      Menú      \n1)Peso\n2)Diferencia cuadrados\n3)Num primos\n4)Fibonacci\n5)conos\n6)Exit\n--> "
repetir = true;
archivo = fopen("registro0.txt","a");
while(repetir == true)
	try
		disp("-------------------------------------------------------------------------------");
		disp(menu);
		salida = input ("Selecciones operacion a realizar: ");
		if (salida == 6)           
			disp("\nGRACIAS POR USAR NUESTRA CALCULADORA");
			fclose("registro0.txt");
			repetir = false;
        elseif (salida == 1)  
            try
                hombres = input("Ingrese numero de hombres: "); 
                mujeres = input("Ingrese numero de mujeres: ")
                lista_ph = [1:hombres];
                lista_pm = [1:mujeres];
                lista_ah = [1:hombres];
                lista_am = [1:mujeres];
                for un = 1:hombres
                    disp(fprintf("Ingrese peso del hombre %d: ",un))
                    peso = input("--> ");
                    lista_ph(un) = peso;
                    disp(fprintf("Ingrese altura del hombre %d: ",un))       
                    altura = input("--> ");
                    lista_ah(un) = altura;
                endfor
                for dos = 1:mujeres
                    disp(fprintf("Ingrese peso de la mujer %d: ",dos))
                    peso = input("-->");
                    lista_pm(dos) = peso; 
                    disp(fprintf("Ingrese altura de la mujer %d: ",dos))      
                    altura = input("--> ");
                    lista_am(dos) = altura;
                endfor
                pah = sum(lista_ah)/hombres;
                disp(fprintf("promedio altura hombres: %d",pah))
                pam = sum(lista_am)/mujeres;
                disp(fprintf("promedio altura mujeres: %d",pam))
                pph = sum(lista_ph)/hombres;
                disp(fprintf("promedio peso hombres: %d",pph))
                ppm = sum(lista_pm)/mujeres;
                disp(fprintf("promedio peso mujeres: %d",ppm))
                salida = 15;
            catch
                fprintf(archivo,"Ocurrio un error");  
                disp("\nError en el ingres");
            end_try_catch    
        elseif (salida == 2)  
            try
                disp("la diferencia requerida es: ")
                suma_cuadrados = 0;
                suma_naturales = 0;
                for a = 1:100
                    suma_cuadrados = suma_cuadrados + a*a;
                    suma_naturales = suma_naturales + a;
                endfor
                fin_nat = suma_naturales*suma_naturales;
                resultado = fin_nat-suma_cuadrados;
                disp(resultado)
            catch
                fprintf(archivo,"Ocurrio un error");  
                disp("\nErdatos")
            end_try_catch    
        elseif (salida == 3)  
            try
                entrada = input("Ingrese número: ");
                disp("Su número primo maximo es:")
                m = [];
                conteo = 0;
                for cua = 1:entrada
                    if mod(entrada,cua)==0
                        conteo = conteo+1;
                        m(conteo) = cua;
                    endif
                endfor
                disp(m)
            catch
                fprintf(archivo,"Ocurrio un error");  
                disp("\nError e datos")
            end_try_catch    
        elseif (salida == 4)  
            try
                ingre = input("Ingrese numero: ")
                disp("La serie de fibonacci es: ")    
                a=0;
                b=1;
                x(:,1)=[1];
                for i=2:n
                    c=a+b;
                    x(:,i)=[c];
                    a=b;
                    b=c;
                endfor
                disp(x)
            catch
                fprintf(archivo,"Ocurrio un error");  
                disp("\nError en tos")
            end_try_catch    
        elseif (salida == 5)  
            try
                generatriz = input("Ingrese generatriz: ")
                radio = input("Ingrese radio: ")
                altura = input("Ingrese altura: ")
                area_bas = pi*radio*radio;
                area_lat = pi*radio*generatriz;
                area_tot = area_bas+area_lat;
                volumen  = (area_bas*altura)/3;
                disp(fprintf("Área base: %d",area_bas))
                disp(fprintf("Área lateral: %d",area_lat))
                disp(fprintf("Área total: %d",area_tot))
                disp(fprintf("Volumen: %d",volumen))
            catch
                fprintf(archivo,"Ocurrio un error");  
                disp("\nError  de datos")
            end_try_catch                 
		else	
			disp("Opcion no encontrada")
		endif
	catch
		disp("\nUsted a ingresado un valor no valido en PRIMER NÚMERO o SEGUNDO NÚMERO");
		fprintf(archivo,"%d;%d\n",5,0);
	end_try_catch		
endwhile