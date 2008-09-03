/**

	WalterCool Present: Compresor

	Programmed in Kwrite, the project begins: 12/06/2007
	
	Using Gentoo Linux,, Unstable Arch (~86), Kernel Version: 2.6.23-gentoo-r3
	
	KDE 3.5.8
	
	For verbose mode, please execute this app adding the v option
	
	For a more cool version, please visit www.slash.cl/huffman
	
	By Pablo Cholaky and Pedro Costas

*/
import java.io.*;
import java.util.ArrayList;
class Compresor
{
	int verbose;
	int largo;
	Compresor(String p)
	{
		verbose = 0;
		largo = 0;
		if (p.indexOf("v") != -1)
		{
			System.out.println("Verbose Mode");
			System.out.println("************");
			System.out.println();
			verbose = 1;
		}
	}
	
	public static void main(String[] holanda)
	{
		if ((holanda.length != 2))
		{
			System.out.println("Usage: java Compresor -C fichero - Compress");
			System.out.println("       java Compresor -D fichero - Decompress");
			System.exit(0);
		}
		
		Compresor c = new Compresor(holanda[0]);
		
		if ((holanda[0].indexOf("C") != -1) && (holanda[0].indexOf("D") == -1)) //Compress
		{
			String[] file = c.leerFichero(holanda[1]);
			String[][] estadisticas = c.creaEstadisticas(c.Letrerizame(file));
			String[] lista = c.mixUp(estadisticas);
			String[] horneado = c.reemplaZo(estadisticas, lista, file);
			String[] compressed = c.compress(horneado);
			c.escribirFichero(holanda[1] + ".walt",compressed, lista, estadisticas);
			
		}
		else if ((holanda[0].indexOf("C") == -1) && (holanda[0].indexOf("D") != -1)) //Decompress
		{
			String[] file = c.leerFichero(holanda[1]);
			String[][] lista = c.fixTabla(c.dimensionaTabla(c.obtenTabla(file)));
			String[] desc = c.decodificar(c.decompress(file), lista);
			c.escribirFichero(holanda[1], desc);
		}
		else
		{
			System.out.println("Usage: java Compresor -C fichero - Compress");
			System.out.println("       java Compresor -D fichero - Decompress");
			System.exit(0);
		}
	}
	
	String[] leerFichero(String fichero)
	{
		if(verbose == 1) System.out.println("Leyendo Archivo...");//verbose
		ArrayList<String> lista = new ArrayList<String>();
		try
		{
			FileReader file = new FileReader(fichero);
			BufferedReader buff = new BufferedReader(file);
			String linea = buff.readLine();
			while (linea != null)
			{
				if(verbose == 1) System.out.println(linea);
				lista.add(linea);
				linea = buff.readLine();
			}
			buff.close();
		}
		catch(Exception e)
		{
			System.out.println("Error leyendo archivo, existe?");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Lectura Ok");
		return Stringizame(lista);
		
	}
	
	String[] Stringizame(ArrayList<String> a)
	{
		if(verbose == 1) System.out.println("Stringizando...");
		String[] asd = new String[a.size()];
		try
		{
			int x = 0;
			for(String i: a)
			{
				if(verbose == 1) System.out.println(i);
				asd[x] = i;
				x++;
			}
		}
		catch(Exception e)
		{
			System.out.println("Error Grave Stringizando");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Stringizado Ok");
		return asd;
	}
	
	String[] Letrerizame(String[] app)
	{
		if(verbose == 1) System.out.println("Letrerizando...");
		ArrayList<String> qwerty = new ArrayList<String>(); //Que monotono esto...
		try
		{
			for(int x = 0; x < app.length; x++)
			{
				for(int y = 0; y < app[x].length(); y++)
				{
					qwerty.add(app[x].substring(y, y+1));
				}
			}
			
		}
		catch(Exception e)
		{
			System.out.println("Error Grave Letrerizando");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Letrerizado Ok");
		return Stringizame(qwerty);
	}
	
	String[][] creaEstadisticas(String[] nomOri) //Esto es complejo
	{
		if(verbose == 1) System.out.println("Creando Estadísticas...");
		String[][] letrasEst = new String[10000][2];
		try
		{
			for (int x = 0; x < nomOri.length; x++)
			{
				int i = 0;
				int sec = 0;
				while(letrasEst[i][0] != null)
				{
					if(letrasEst[i][0].equals(nomOri[x]))
					{
						sec = 1;
						letrasEst[i][1] = "" + (Integer.parseInt(letrasEst[i][1])+1);
						break;
					}
					i++;
				}
				if(sec == 0)
				{
					letrasEst[i][0] = nomOri[x];
					letrasEst[i][1] = "1";
					largo++;
				}
				if(verbose == 1) System.out.println("Letra: " + letrasEst[i][0] + ", vez: " + letrasEst[i][1]);
			}
		}
		catch(Exception e)
		{
			System.out.println("Error Grave Creando estadísticas");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Fin Estadísticas");
		return mergeSort(letrasEst, largo);
	}
	
	String[][] estAcorta(String[][] palpe, int largo)
	{
		if(verbose == 1) System.out.println("Acortando el String a uno finito...");
		String[][] a = new String[largo][2];
		try
		{
			for(int y = 0;y<largo; y++)
			{
				a[y][0] = palpe[y][0];
				a[y][1] = palpe[y][1];
				if(verbose == 1) System.out.println(a[y][0] + ": " + a[y][1]);
			}
		}
		catch(Exception e)
		{
			System.out.println("Error Grave Acortando el String");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Acortado, pasó de uno de largo 1000 a uno " + largo);
		return a;
	}
	
	String[][] mergeSort(String[][] nice, int largo)
	{
		
		if(verbose == 1) System.out.println("Creando mergeSort...");
		String p[][] = estAcorta(nice, largo);
		try
		{
			for(int x = 0; x < largo; x++)
			{
				for(int y = 0;y < largo; y++) //Por problemas es ineficiente a morir!
				{
					if(Integer.parseInt(p[x][1]) > Integer.parseInt(p[y][1]))
					{
						String t1 = p[x][1];
						p[x][1] = p[y][1];
						p[y][1] = t1;
						String t2 = p[x][0];
						p[x][0] = p[y][0];
						p[y][0] = t2;
					}
				}
			}
			if(verbose == 1)
			{
				System.out.println("Ordenado:");
				for(int y = 0; y < largo; y++)
				{
					System.out.println(p[y][0] + ": " + p[y][1]);
				}
			}
		}
		catch(Exception e)
		{
			System.out.println("Error Grave en mergeSort");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Fin Mergesort");
		return p;
	}
	
	String[] mixUp(String[][] das)
	{
		if(verbose == 1) System.out.println("Creando la tabla mágica...");
		String[] ayy = new String[largo];
		try
		{
			String cami = "0";
			String base = "01";
			if(largo != 0)
			{
				ayy[0] = base;
				for(int x = 1; x< largo; x++)
				{
					ayy[x] = cami + base;
					if(cami.indexOf("0") != -1)
					{
						if(verbose == 1) System.out.println("Cambio 0 -> 1");
						cami = cami.replaceFirst("0","1");
					}
					else
					{
						String camila = "";
						for(int y = 0; y<=cami.length(); y++)
						{
							camila = camila + "0";
						}
						if(verbose == 1) System.out.println("Añadiendo 0s");
						cami = camila;
					}
				}
			}
			if(verbose == 1)
			{
				for(int x = 0; x < ayy.length; x++)
				{
					System.out.println(das[x][0] + " -> " + ayy[x]);
				}
			}
		}
		catch(Exception e)
		{
			System.out.println("Error Grave creando la tabla mágica");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Fin de la tabla mágica");
		return ayy;
	}
	
	String[] reemplaZo(String[][] arra, String[] tabla, String[] Archivo)
	{
		if(verbose == 1) System.out.println("Reemplazando datos...");
		try
		{
			for(int x = 0; x < Archivo.length; x++)
			{
				for(int y = 0; y < tabla.length; y++)
				{
					Archivo[x] = Archivo[x].replace(arra[y][0],tabla[y]);
					
					if(verbose == 1) System.out.println(Archivo[x]);
				}
			}
		}
		catch(Exception e)
		{
			System.out.println("Error Grave Reemplazando datos");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Fin del reemplazo de datos");
		return Archivo;
	}
	
	String[] compress(String[] Wtf)
	{
		if(verbose == 1) System.out.println("Comprimiendo...");
		String[] record = new String[Wtf.length];
		try
		{
			for(int x = 0; x<Wtf.length; x++)
			{
				int to;
				record[x] = "";
				for(int i =0;i < Wtf[x].length(); i+=16 ) {
					if((i+16) > Wtf[x].length()) {  to = Wtf[x].length(); }
					else  to = (i+16);
					String tessst = Wtf[x].substring(i,to);
					Long characterObj = Long.valueOf(tessst, 2);
					long character = characterObj.longValue();
					Character c = new Character((char)character); 
					record[x] = record[x] + c;
				}
			}
			if(verbose == 1)
			{
				for(int x = 0; x<Wtf.length; x++)
				{
					System.out.println(record[x]);
				}
			}
		}
		catch(Exception e)
		{
			System.out.println("Error Grave Comprimiendo");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Fin de la compresión");
		return record;
	}
	
	String[] decompress(String[] Wtf)
	{
		if(verbose == 1) System.out.println("Descomprimiendo...");
		String[] record = new String[Math.abs(largo-Wtf.length)];
		try
		{
			for(int x = 0; x<record.length; x++)
			{
				record[x] = "";
				int to;
				for(int  y = 0; y < Wtf[x].length(); y++)
				{
					Character p = Wtf[x].charAt(y);
					record[x] = record[x] + (Integer.toBinaryString(p));
				}
			}
			if(verbose == 1)
			{
				for(int x = 0; x < record.length; x++)
				{
					System.out.println(record[x]);
				}
			}
		}
		catch(Exception e)
		{
			System.out.println("Error Grave Descomprimiendo");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Fin de la Descompresión");
		return record;
	}
	
	String[] obtenTabla(String[] file)
	{
		ArrayList<String> arra = new ArrayList<String>();
		if(verbose == 1) System.out.println("Obteniendo la tabla...");
		try
		{
			int existe = 0;
			for(int x = 0; x < file.length; x++)	//Obtengo valores.
			{
				if(file[x].indexOf("01") != -1)
				{
					if(verbose == 1) System.out.println("Dato Encontrado: " + file[x]);
					largo++;
					arra.add(file[x]);
					existe = 1;
				}
			}
			
			if (existe == 0)
			{
				System.out.println("No existe Tabla, Archivo compreso?");
				System.exit(0);
			}
		}
		catch(Exception e)
		{
			System.out.println("Error Grave Obteniendo Tabla");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Tabla Obtenida");
		return Stringizame(arra);
	}
	
	String[][] dimensionaTabla(String[] tabla)
	{
		String[][] tablaDoble = new String[largo][2];
		if(verbose == 1) System.out.println("Dimensionando Tabla...");
		try
		{
			for(int x = 0; x < largo; x++)
			{
				tablaDoble[x][0] = tabla[x].substring(0,tabla[x].indexOf("-"));
				tablaDoble[x][1] = tabla[x].substring(tabla[x].lastIndexOf("-")+1,tabla[x].length());
			}
			if(verbose == 1)
			{
				for(int x = 0; x<largo; x++)
				{
					System.out.println(tablaDoble[x][0] + " es = a " + tablaDoble[x][1]);
				}
			}
		}
		catch(Exception e)
		{
			System.out.println("Error Grave Dimensionando Tabla");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Tabla Dimensionada");
		return tablaDoble;
	}
	
	String[][] fixTabla(String[][] AOL)
	{
		if(verbose == 1) System.out.println("Arreglando la tabla maestra...");
		try
		{
			String p = AOL[0][0];
			for(int x = 0; x < largo; x++)
			{
				AOL[x][1] = AOL[x][1].replaceAll("01",p);
				if(verbose == 1) System.out.println(AOL[x][1]);
			}
		}
		catch(Exception e)
		{
			System.out.println("Error Grave arreglando la tabla maestra");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Tabla arreglada");
		return AOL;
	}
	
	String[] decodificar(String[] transcode, String[][] list)
	{
		if(verbose == 1) System.out.println("Decodificando el binario...");
		try
		{
			for(int x = 0; x < transcode.length; x++)
			{
				transcode[x] = transcode[x].replaceAll("01", list[0][0]);
				if(verbose == 1) System.out.println(transcode[x]);
				for(int y = largo-1; y >= 0; y--)
				{
					transcode[x] = transcode[x].replaceAll(list[y][1],list[y][0]);
				}
			}
			if(verbose == 1)
			{
				for(int x = 0; x < transcode.length; x++)
				{
					System.out.println(transcode[x]);
				}
			}
		}
		catch(Exception e)
		{
			System.out.println("Error grave decodificando el binario");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Decodificado Completo");
		return transcode;
	}
	
	void escribirFichero(String loc, String[] p)
	{
		if(verbose == 1) System.out.println("Escribiendo en fichero...");
		try
		{
			String q = loc.substring(0,loc.lastIndexOf(".walt"));
			BufferedWriter buff = new BufferedWriter(new FileWriter(q + ".temp"));
			PrintWriter out = new PrintWriter(buff);
			for(int x = 0; x<p.length; x++)
			{
				out.println(p[x]);
			}
			out.close();
			System.out.println("Al estar con error de char, se grabará como fichero.temp");
			System.out.println("Nota, no creo que este error sea humano, simplemente por falta de chars");
		}
		catch(IOException e)
		{
			System.out.println("Error!");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Escritura Ok");
	}
	
	void escribirFichero(String loc, String[] p, String[] est, String[][] list)
	{
		if(verbose == 1) System.out.println("Escribiendo en fichero...");
		try
		{
			BufferedWriter buff = new BufferedWriter(new FileWriter(loc));
			PrintWriter out = new PrintWriter(buff);
			for(int x = 0; x<p.length; x++)
			{
				out.println(p[x]);
			}
			for(int x= 0; x<est.length; x++)
			{
				out.println(list[x][0] + "-" + est[x]);
			}
			out.close();
		}
		catch(IOException e)
		{
			System.out.println("Error!");
			System.exit(0);
		}
		if(verbose == 1) System.out.println("Escritura Ok");
	}
}

/**
		Notas del Programador
		
		Para comprimir
		
		1, Paso todo a lineas - Listo
		2, Paso todo a letras - Listo
		3, Creo estadisticas de letras - Listo
		4, Asigno Valor a las letras + 10 - Listo
		5, Reemplazo las lineas a numeros valorizados - Listo
		6, Los transformo a otras letras char 16bit - Listo
		7, Escribo en fichero estadisticas + binarios - Listo
		
		Para descomprimir
		
		1, Paso todo a lineas - Listo
		2, Paso la tabla estadistica a un array, el resto a otro - Listo
		3, Desbinarizo el array - Listo :) Al fin
		4, Decodifico el array - Listo, pero se desborda, debe ser error de char, NO humano.
		5, Escribo a fichero. -
*/