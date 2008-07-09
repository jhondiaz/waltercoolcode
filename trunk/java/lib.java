import java.util.*;
public class lib
{
	lib()
	{
		
	}

	public void vb(String hace)
	{
		System.out.println("Comienzo de " + hace);
		System.out.println(hace + "ha fallado en la linea");
		System.out.println("Finalizando " + hace);
	}

	public String[] var(String[] arreglo, int length, String error)
	{
		String[] a = new String[length];
		try
		{
			for(int x = 0; x<length; x++)
			{
				a[x] = arreglo[x];
			}
		}
		catch(Exception e)
		{
			System.out.println("Error, por favor ejecute este programa con java " + error);
			System.exit(0);
		}
		return a;
	}
}
