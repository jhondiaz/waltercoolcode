#include <iostream>
using namespace std;

int **memoriaFisica, M, S, N;
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

bool libera(string p)
{
  //Falta implementar
  return 0;
}

bool compruebaComando(string p)
{
  //Falta implementar
  return 0;
}

bool chequea(string p)
{
  //Falta implementar
  return 0;
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
  
  memoriaFisica = new int*[M];
  for( x = 0 ; x < M ; x++ )
  {
   memoriaFisica[x] = new int[S];
  }
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
    cout << "Saliendo del programa, GoodBye!";
    delete memoriaFisica;
  }
  else
  {
    if(compruebaComando(k) == true) //Es k válido
    {
      if(chequea(k) == false) //No existe en memoria
      {
	if(chequea("") == true) //Existe espacio libre en memoria
	{
	  add(k);
	}
	else //No existe espacio, osea, reemplazar
	{
	  libera(k);
	}
      }
    }
    else
    {
      cout << "Has tipeado algo mal, intenta nuevamente, recuerda, Px=axb";
    }
  }
}
