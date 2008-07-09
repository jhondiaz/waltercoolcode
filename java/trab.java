import java.io.* ;

/**
	Este trabajo fué hecho en java por problemas en c
	
	Optimizado para UTF-8, Gentoo Linux.
*/

class trab
{
	public static void main(String args[]) throws IOException
	{
		BufferedReader lee = new BufferedReader(new InputStreamReader( System.in));
		write("Ingrese el tiempo a simular: "); int tiempo = Integer.parseInt(lee.readLine());
		write("Ingrese la cantidad de procesos: "); int cantidad = Integer.parseInt(lee.readLine());
		String[] datos = new String[cantidad];
		for(int x = 0; x < cantidad; x++)
		{
			write("Ingrese el proceso " + (x+1) + ": ");
			datos[x] = lee.readLine();
		}
		int[][] valores = procesos(cantidad, datos);
		FIFO(valores, cantidad, tiempo);
		SJN(valores, cantidad, tiempo);
		SJNST(valores, cantidad, tiempo);
		PPSE(valores, cantidad, tiempo);
		RR(valores, cantidad, tiempo);
		/**int[] y = new int[100];
		for(int x = 0; x < 100; x++)
		{
			y[x] = new Double(Math.random() * 100 + 1).intValue();
		}
		burbujaMalvada(100, y);
		for(int x = 0; x< 100; x++ )
		{
			write("" + y[x]);
		}*/
		
 	}
	
	static void RR(int[][] valores, int cantidad, int tiempo)
	{
		
		write("Iniciando Round Robin");
		write("");
		write("Proceso/Tiempo Llegada");
		write("Usando como tiempo quantum 20 tiempos");
		int RR = 20;
		int[] total = new int[cantidad];
		for(int x = 0; x < cantidad; x++)
		{
			int suma = 0;
			for(int y = 2;y < 100; y++)
			{
				if(valores[x][y] > 0)
				{
					suma += valores[x][y];
				}
			}
			total[x] = suma;
		}
		while(tiempo > 0)
		{
			for(int x = 0; x < cantidad; x++)
			{
				if(total[x] != 0)
				{
					if(total[x] < 20)
					{
						tiempo -= total[x];
						total[x] = 0;
					}
					else
					{
						tiempo -= 20;
						total[x] -= 20;
					}
				}
				if(tiempo < 0)
				{
					total[x] -= tiempo;
					break;
				}
			}
		}
		for(int x = 0; x < cantidad; x++)
		{
			if(total[x] == 0) write("Proceso " + (x+1) + " Finalizado");
			if(total[x] > 0)
			{
				write("Proceso" +(x+1) + " aún sin finalizar");
				write("Hicieron falta " + total[x] + " tiempos en P" + (x+1));
			}
		}
	}
	
	static void PPSE(int[][] valores, int cantidad, int tiempo)
	{
		write("Iniciando Por Prioridad Sin Expropiación");
		write("");
		write("Proceso/Tiempo Llegada");
		int[] tiempoLlegada = new int[cantidad];
		for(int x = 0; x < cantidad; x++)
		{
			tiempoLlegada[x] = valores[x][1];
		}
		int[] p = burbujaMalvada(cantidad, tiempoLlegada);
		
		calculaTiempo(cantidad, valores, p, tiempo);
	}
	
	static void SJN(int[][] valores, int cantidad, int tiempo)
	{
		write("Iniciando SJN");
		write("");
		write("Proceso/Tiempo Llegada");
		int[] tiempoMenor = new int[cantidad];
		for(int x = 0; x < cantidad; x++) //calculo menor tiempo
		{
			for(int y = 2; y < 100; y++)
			{
				tiempoMenor[x] += valores[x][y];
				//if(y != 0) write("" + tiempoMenor[x]);
			}
		}
		int[] p = burbujaMalvada(cantidad, tiempoMenor);
		calculaTiempo(cantidad, valores, p, tiempo);
	}
	
	static void SJNST(int[][] valores, int cantidad, int tiempo)
	{
		write("Iniciando SJN Sin Trampa");
		write("");
		write("Proceso/Tiempo Llegada");
		int[] cantidadProcesos = new int[cantidad];
		for(int x = 0; x < cantidad; x++) //calculo menor tiempo
		{
			int noTransantiago = 0;
			for(int y = 2; y < 100; y++)
			{
				if(y > 0) noTransantiago++;
			}
			cantidadProcesos[x] = noTransantiago;
		}
		int[] p = burbujaMalvada(cantidad, cantidadProcesos);
		calculaTiempo(cantidad, valores, p, tiempo);
	}
	
	static int[] burbujaMalvada(int cantidad, int[] arreglo)
	{
		int[] p = new int[cantidad];
		for(int x = 0; x < cantidad; x++) //variable p para orden
		{
			p[x] = x;
		}
		for(int x = 0; x < cantidad; x++)
		{ //burbuja malvada
			for(int y = 0; y < cantidad; y++)
			{
				if (arreglo[x] < arreglo[y])
				{
					int t1 = arreglo[x];
					arreglo[x] = arreglo[y];
					arreglo[y] = t1;
					
					t1 = p[x];
					p[x] = p[y];
					p[y] = t1;
				}
			}
		} //Fin de la burbuja malvada
		//for(int x = 0; x < cantidad; x++) write("" + p[x]);
		return p;
	}
	
	static void calculaTiempo(int cantidad, int[][] valores, int[] p, int tiempo)
	{
		int[] suma = new int[cantidad];
		int sumaTotal = 0;
		int tiempoFinal = 0;
		for(int x = 0; x < cantidad; x++) //calcula tiempo total
		{
			int contador = 0;
			for(int y = 2; y < 100; y++)
			{
				if ((sumaTotal + suma[x] + valores[p[x]][y])> tiempo)
				{
					write("Tiempo acortado!, el proceso no pudo terminar!");
					write("Del proceso P" + (p[x]+1) + " se ejecutaron " + contador + " cargas");
					tiempoFinal = 1;
					break;
				}
				suma[x] = suma[x] + valores[p[x]][y];
				if (valores[p[x]][y] != 0) 
				{
					contador++;//write("" + contador);
				}
			}
			write("P" + (p[x]+1) + "/" + suma[x]);
			sumaTotal = sumaTotal + suma[x];
			if (tiempoFinal == 1) break;
		}
	}

	static void FIFO(int[][] valores, int cantidad, int tiempo)
	{
		write("Iniciando FI/FO");
		write("");
		write("Proceso/Tiempo Llegada");
		int[] tiempoLlegada = new int[cantidad];
		for(int x = 0; x < cantidad; x++)
		{
			tiempoLlegada[x] = valores[x][0];
		}
		int[] p = burbujaMalvada(cantidad, tiempoLlegada);
		
		calculaTiempo(cantidad, valores, p, tiempo);
	}
	
	static int[][] procesos(int cantidad, String[] datos)
	{
		int[][] values = new int[cantidad][100];
		for(int x = 0; x < cantidad; x++)
		{
			int z = datos[x].indexOf(":");
			datos[x] = datos[x].substring(z+1,datos[x].length());
			String[] k = datos[x].split(":");
			values[x][0] = Integer.parseInt(k[0]);
			values[x][1] = Integer.parseInt(k[1]);
			String[] q = k[2].split(",");
			for(int y = 2; y < q.length+2; y++)
			{
				values[x][y] = Integer.parseInt(q[y-2]);
				//System.out.println(values[x][y]);
			}
		}
		return values;
	}
	
	static void write(String p) //Me da paha escribir a cada rato lo mesmo.
	{
		System.out.println(p);
	}
}