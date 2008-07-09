#include <iostream>
using namespace std;

string **memoriaFisica;
int M, S, N;
bool lock = false;
char method = 'f';

bool FIFO(string p)
{
  //Falta implementar
  return 0;
}

bool LRU(string p)
{
  //Falta implementar
  return 0;
}

bool SecondOportunity(string p)
{
  //Falta implementar
  return 0;
}

bool add(string p)
{
  //Falta implementar
  return 0;
}

bool libera(string p) //Ordeno a los liberadores de memoria
{
  bool x = 0;
  if(method == 'f')
  {
    x = FIFO(p);
  }
  else if(method == 'l')
  {
    x = LRU(p);
  }
  else if(method == 's')
  {
    x = SecondOportunity(p);
  }
  else
  {
    cout << "Dammm... un bug\n";
  }
  //Falta implementar
  return x;
}

bool compruebaComando(string p)
{
  if(p[0] == 'P')
  {
    //Falta mejor implementación
    cout << "He comprobado correctamente\n";
    return 1;
  }
  return 0;
}

bool chequea(string p)
{
  int x,y;
  //Falta implementar
  for(x = 0; x < M; x++)
  {
    for(y = 0; x < S; y++)
    {
      if (memoriaFisica[x][y] == p)
      {
	return 1;
      }
    }
  }
  return 0;
}

void introduccion()
{
  cout << "Bienvenido a GNU/poneletarea3, podrás simular paginación desde aquí\n";
  cout << "Tus comandos son los siguientes:\n";
  cout << "l)Cambia el reemplazo a FIFO\nl) Cambia el reemplazo a LRU\n";
  cout << "s)Cambia el reemplazo a Segunda Oportunidad\nq) Sale del programa\n\n";
  cout << "
}

int main()
{
  int x,y;
  cout << "Ingrese M: ";
  cin >> M;
  cout << "Ingrese S: ";
  cin >> S;
  cout << "Ingrese N: ";
  cin >> N;
  
  memoriaFisica = new string*[M];
  for( x = 0 ; x < M ; x++ )
  {
   memoriaFisica[x] = new string[S];
  }
  introduccion();
  while(true)
  {
    string k;
    cin >> k;
    if( (k == "s") || (k == "f") || (k == "l") && (lock == false) )
    {
      cout << "Metodo anterior: " << method << "\n";
      cout << "Metodo nuevo: " << k[0] << "\n";
      method = k[0];  
    }
    else if( (k == "q") || (k == "quit") )
    {
      cout << "Saliendo del programa, GoodBye!\n";
      delete memoriaFisica;
      break;
    }
    else
    {
      if(compruebaComando(k) == true) //Es k válido
      {
	if(chequea(k) == false) //No existe en memoria
	{
	  if(chequea("") == true) //Existe espacio libre en memoria
	  {
	    cout << "Existe espacio libre en memoria, congrats\n";
	    add(k);
	  }
	  else //No existe espacio, osea, reemplazar
	  {
	    libera(k);
	  }
	}
	else
	{
	  cout << "Esta palabra ya se encuentra :)\n";
	  //No hay interrupción
	}
      }
      else
      {
	cout << "Has tipeado algo mal, intenta nuevamente, recuerda, Px=axb\n";
      }
    }
  }
  
}
