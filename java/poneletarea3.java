import java.io.*;
class poneletarea3{
public static void main(String argv[]) throws IOException
{
  int M,S,N;
  InputStreamReader isr = new InputStreamReader(System.in);
  BufferedReader br = new BufferedReader (isr);
  System.out.print("Ingrese un número M: ");
  M = Integer.parseInt(br.readLine()); //Marcos
  System.out.print("Ingrese un número S: ");
  S = Integer.parseInt(br.readLine()); //Palabras
  System.out.print("Ingrese un número N: ");
  N = Integer.parseInt(br.readLine()); //N Procesos
  int[][] memoriaFisica = new int[M][S];
  System.out.println("Ahora puede ingresar procesos, comenzará con FIFO por defecto\n");
  System.out.println("Si desea cambiar de modo, acá va una lista con atajos");
  System.out.println("\n\nf) Cambia a FIFO por defecto\nl) Cambia a LRU por defecto");
  System.out.println("s) Cambia a Segunda Oportunidad por defecto\nq) Termina y muestra el sumario\n\n");
  char a = 'f';
  while(true)
  {
    String k = br.readLine();
    if (k.equals("f"))
    {
      System.out.println("Algorítmo usado ahora es FIFO");
      a = 'f';
    }
    else if (k.equals("l"))
    {
      System.out.println("Algorítmo usado ahora es LRU");
      a = 'l';
    }
    else if (k.equals("s"))
    {
      System.out.println("Algorítmo usado ahora es Segunda Oportunidad");
      a = 's';
    }
    else if (k.equals("q"))
    {
      System.out.println("Saliendo");
      break;
    }
    else
    {
      
    }
  }
}

int FIFO()
{
  return 0;
}

int LRU()
{
  return 0;
}

int SecondOportunity()
{
  return 0;
}
}