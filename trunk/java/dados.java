class dados
{
	public static void main(String args[])
	{
		int a, b;
		int x = 0;
		int p = 1;
		int q = 0;
		try
		{
			a = Integer.parseInt(args[0]);
		}
		catch(ArrayIndexOutOfBoundsException e)
		{
			a =1;
			System.out.println("Este programa funciona haciendo java \"nro max\" \"veces\"");
			System.exit(0);
		}
		try
		{
			p = Integer.parseInt(args[1]);
			q = Integer.parseInt(args[2]);
		}
		catch(ArrayIndexOutOfBoundsException e)
		{
			
		}
		if (q == 0)
		{
			for (int y = 0; y < p ; y++)
			{
				x = new Double(Math.random() * a + 1).intValue();
				System.out.println("Resultado " + (y+1) + ": " + x);
			}
		}
		else
		{ // q = dificultad, p = veces, x = probabilidad
			int h = 0;
			for (int y = 0; y < p ; y++)
			{
				x = new Double(Math.random() * a + 1).intValue();
				System.out.println("Resultado " + (y+1) + ": " + x);
				if (x == 1) {y+=1;}
//h-=1;
				if (x == 10){ y-=1;}
				if (q <= x)
				{
					h++;
				}
			}
			if(h == 1){ System.out.println(h + " exito");}
			else{System.out.println(h + " exitos");}
		}
	}
}
