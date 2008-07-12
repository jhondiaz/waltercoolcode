/**
Bugs Conocidos:

1) Add() agrega de n a n+m, pero si añado n-1, vuelve a añadir n... n+m
2) Segmention Fault cuando M o N vale 0
3) Los procesos son ilimitados...
4) Detecta P, pero no la heurística de Px:axb
*/

#include <iostream>
#include <sstream>
using namespace std;
string **memoriaFisica;
string *recuerdaProc = new string[1000];
int *procsUsed = new int[1000];
int M, S, N, FIFOcounter, record[2], fault, **chance;
int salvaBugs = 0;
bool lock = false;
char method = 'f';

bool ordena(string p) //Method Handler
{
  cout << "He comenzado a liberar :D\n";
  fault++;
  int x,y,z = 0;
  while(true)
  {
    if ( (FIFOcounter == z) && (chance[x][y] = 0) ) //Lo Encontré!
    {
      memoriaFisica[x][y] = p; //Reemplazalo
      FIFOcounter++; //Fifo list, para saber a quien le toca.
      if (FIFOcounter = (M*S))
      {
	FIFOcounter = 0;
      } 
      return 1;
    }
    else if( (FIFOcounter == z) && (chance[x][y] = 1) ) //Second Oportunity regala una oportunidad
    {
      chance[x][y] = 0;
    }
    else //Siga buscando
    {
      y++;
      if (y = S)
      {
	y=0;
	x++;
      }
      if (x = M)
      {
	x = 0;
      }
    }
  }
  //Falta implementar
  return 0;
}

bool LRU(string p)
{
  //Falta implementar
  return 0;
}

bool add(string p)
{
  stringstream qwerty;
  int x,y;
  int d = p.find("x");
  string hex1 = p.substr(d+1,p.length());
  qwerty << hex1;
  qwerty >> y;
  qwerty.str("");
  cout << "Soy y: " << y << "\n";
  string hex0 = p.substr(0, d+1);
  for(x = 0; x < S; x++) //Existe un bug, añade existentes si uno anterior no se ha añadido
  {
    stringstream ytrewq;
    string temp;
    string q = hex0;
    ytrewq << y+x;
    ytrewq >> temp;
    ytrewq.str("");
    cout << "Soy temp y valgo " << temp <<"\n";
    q.append(temp);
    memoriaFisica[record[0]][x] = q;
    cout << "He añadido " << q << "\n";
  }
  fault++;
  return 1;
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
  cout << "Chequeando... \"" << p << "\"\n";
  //Falta implementar
  for(x = 0; x < M; x++)
  {
    for(y = 0; y < S; y++)
    {
      if (memoriaFisica[x][y] == p)
      {
	record[0] = x;
	record[1] = y;
	
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
  cout << "f)Cambia el reemplazo a FIFO\nl) Cambia el reemplazo a LRU\n";
  cout << "s)Cambia el reemplazo a Segunda Oportunidad\nq) Sale del programa\n\n";
  cout << "Debes ingresar \"Px:a×b\" donde x es el identificador del proceso\n";
  cout << "axb es la posición hexadecimal\n";
}

void ending()
{
  cout << "Conteo actual!\n\nTotal PageFaults: " << fault << "\n";
  //Por implementar
}

int main()
{
  int x,y;
  fault = 0;
  cout << "Ingrese M: ";
  cin >> M;
  cout << "Ingrese S: ";
  cin >> S;
  cout << "Ingrese N: ";
  cin >> N;
  chance = new int*[M];
  memoriaFisica = new string*[M];
  for( x = 0 ; x < M ; x++ )
  {
    chance[x] = new int[S];
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
	salvaBugs = 0;
	if(chequea(k) == false) //No existe en memoria
	{
	  if(chequea("") == true) //Existe espacio libre en memoria
	  {
	    cout << "Existe espacio libre en memoria, congrats\n";
	    add(k);
	  }
	  else //No existe espacio, osea, reemplazar
	  {
	    ordena(k);
	  }
	}
	else
	{
	  cout << "Esta palabra ya se encuentra :)\n";
	  if(method = 's')
	  {
	    chance[record[0]][record[1]] = 1;
	  }
	  //No hay interrupción
	}
      }
      else
      {
	cout << "Has tipeado algo mal, intenta nuevamente, recuerda, Px:axb\n";
	salvaBugs++;
	if(salvaBugs > 10)
	{
	  cout << "Lo siento, has tenido muchas fallas, o bug, exit!\n";
	  break;
	}
      }
    }
  }
  ending();
}
