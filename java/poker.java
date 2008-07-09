import java.util.*;
class poker
{
	Random r = new Random();
	int maxmano;
	public static void main(String args[])
	{
		new poker();
	}
	
	private poker()
	{
		
	}
	
	private String generaCartas()
	{
		String simbolo = "";
		String color = "";
		int numero = r.nextInt(12) + 1;
		int tipo = r.nextInt(4);
		int col = r.nextInt(2);
		if (tipo == 0) {simbolo = " pica";}
		if (tipo == 1) {simbolo = " corazon";}
		if (tipo == 2) {simbolo = " trebol";}
		if (tipo == 3) {simbolo = " hoja";}
		String f = numero + simbolo;	
		return f;
	}
	
	private String[] separaMe(String carta)
	{
		String[] separacion = new String[2];
		int espacio = carta.indexOf(" ");
		separacion[0] = carta.substring(0,espacio);
		separacion[1] = carta.substring(espacio+1,carta.length());
		return separacion;
	}
			
	private String reglas(String[] mano)
	{
		String estrategia = "";
		String[][] listamano = new String[maxmano][2];
		for(int x = 0; x < maxmano; x++)
		{
			String[] separado = separaMe(mano[x]);
			listamano[x][0] = separado[0];
			listamano[x][1] = separado[1];
		}
		
		return estrategia;
	}
}