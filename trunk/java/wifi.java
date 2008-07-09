import java.io.*;
class wifi
{
	String dispositivo;
	public Runtime d;
	FileInputStream file;
	
	public static void main(String args[])
	{
		wifi d = new wifi();
		d.dispositivo();
	}
	wifi()
	{	
		d = new Runtime();
	}
	
	void dispositivo() //Reconoce dispositivos
	{
		d.exec("iwconfig >> p");
		file = new FileInputStream("temp");
		int z = 0;
		String lectura = "";
		for(int x = 0; x < z; x++)
		{
			try
			{
				String kaplum = file.readLine();
				int p = kaplum.indexOf("IEEE");
				if(p != -1)
				{
					lectura = kaplum.substring(0,p);
				}
			}
			catch(Exception e)
			{
				System.out.println("Error leyendo");
			}
		}
		System.out.println(lectura);
	}
	
	void lectura()
	{
		d.exec("iwlist " + dispositivo + "");
	}
}