/**
	 Declarado como GNU Licencia V2
	Creado por Pablo Cholaky Cabezas 
	     <waltercool@slash.cl>

Bugs Conocidos:

2) Segmention Fault cuando M o N vale 0 - YA NO
3) Los procesos son ilimitados... - YA NO
4) Detecta P, pero no la heurística de Px:axb ARREGLADO
*/

#include <iostream>
#include <sstream>
using namespace std;
string **memoriaFisica;
string *recuerdaProc = new string[1000];
int *procsUsed = new int[1000];
int M, S, N, FIFOcounter, record[2], fault, **chance;
int* faltasPorProc;
int salvaBugs = 0;
int totalProc = 0;
bool lock = false;
char method = 'f';

bool chequea(string p)
{
  int x,y;
  cout << "Chequeando... \"" << p << "\"\n";
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
  cout << "No encontrado :D\n";
  return 0;
}

string LRUHandler(int method, string p)
{
  cout << "Soy LRUHandler\n";
  int x = 0;
  if(method == 1) //1 = Busca p en recuerdaProc
  {
    cout << "Busco por " << p << " en recuerdaProx[x]\n";
    cout << "Method: " << method << " string: " << p;
    while(true)
    {
      if (recuerdaProc[x] == p)
      {
	//cout << "procsUsed: " << procsUsed[x] << " x: " << x;
	procsUsed[x]++;
	//cout << "Ajá, yo te recuerdo! ++\n";
	return "";
      }
      if (recuerdaProc[x] == "")
      {
	method = 2;
	break;
      }
      x++;
    }
  }
  if(method = 2) //Añade p en recuerdaProc
  {
    cout << "Nuevo proceso en recuerdaProc, agregado\n";
    recuerdaProc[totalProc] = p;
    totalProc++;
    return "";
  }
  if(method = 3) //Ordena
  {
    cout << "LRU, ordenando\n";
    int menor = -1;
    for(x = 0; x < totalProc; x++)
    {
      if( (menor > procsUsed[x]) || (menor == -1) ) //Busca el menos usado
      {
	if(chequea(recuerdaProc[x]) == true) //Si está en memoria, lo agrega
	{
	  menor = procsUsed[x];
	}
      }
    }
    return recuerdaProc[x];
  }
  return 0;
}

bool compruebaComando(string p)
{
  cout << "Comprobando comando\n";
  int x = p.find("x");
  int y = p.find(":");
  int z;
  stringstream qwe;
  //cout << y << "   " << p.length() << "\n";
  qwe << p.substr(1,p.length()-y);
  qwe >> z;
  if ( (p[0] == 'P') && (x > y) && (z < N) )
  {
    cout << "He comprobado correctamente\n";
    return 1;
  }
  return 0;
}

bool ordena(string p) //Method Handler
{
  cout << "He comenzado a liberar\n";
  int cfo;
  stringstream lero;
  lero << p.substr(1,p.length()-p.find(":"));
  lero >> cfo;
  faltasPorProc[cfo]++;
  fault++;
  int x = 0;
  int y = 0;
  int z = 0;
  while(true)
  {
    if (method == 'l')
    {
      cout << "Buscando LRU\n";
      string q = LRUHandler(3,p); //Busco al menos usado
      cout << "Chequeando en memoria\n";
      chequea(q); //Busco la posición en memoria
      cout << "Cambiando\n";
      memoriaFisica[record[0]][record[1]] = p; //Lo cambio
      cout << "Marcando\n";
      LRUHandler(1,p); //Lo marco como usado
      return 1;
    }
    else if ( (FIFOcounter == z) && (chance[x][y] == 0) ) //Lo Encontré!
    {
      cout << "Liberando: " << memoriaFisica[x][y] << "\n";
      memoriaFisica[x][y] = p; //Reemplazalo
      FIFOcounter++; //Fifo list, para saber a quien le toca.
      return 1;
    }
    else if( (FIFOcounter == z) && (chance[x][y] == 1) ) //Second Oportunity regala una oportunidad
    {
      cout << "Regalito de Second Oportunity\n";
      FIFOcounter++;
      chance[x][y] = 0;
    }
    else //Siga buscando
    {
      if (FIFOcounter > (M*S))
      {
	FIFOcounter = 0;
      }
      if( z > (M*S))
      {
	z = 0;
      }
      //cout << z << "Buscando" << x << "..." << y << "\n";
      y++;
      if (y == S)
      {
	y = 0;
	z++;
	x++;
      }
      if (x == M)
      {
	x = 0;
      }
    }
  }
  return 0;
}

bool add(string p)
{
  int remember = record[0];
  stringstream qwerty;
  int x,y,z = 0;
  int d = p.find("x");
  string hex1 = p.substr(d+1,p.length());
  qwerty << hex1;
  qwerty >> y;
  qwerty.str("");
  //cout << "Soy y: " << y << "\n";
  string hex0 = p.substr(0, d+1);
  for(x = 0; x < S; x++) //Existe un bug, añade existentes si uno anterior no se ha añadido. ARREGLADO
  {
    stringstream ytrewq;
    string temp;
    string q = hex0;
    ytrewq << y+z;
    ytrewq >> temp;
    ytrewq.str("");
    //cout << "Soy temp y valgo " << temp <<"\n"; DEPRECATED
    q.append(temp);
    bool Q = chequea(q);
    if(Q == true) //Existe el termino
    {
      x--;
      z++;
    }
    if(Q == false) //No existe en memoria
    {
      memoriaFisica[remember][x] = q;
      cout << "He añadido " << q << "\n";
      z++;
    }
    if(method == 'l') LRUHandler(1,q);
  }
  int cfo;
  stringstream lero;
  lero << p.substr(1,p.length()-p.find(":"));
  lero >> cfo;
  faltasPorProc[cfo]++;
  fault++;
  return 1;
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
  int x;
  cout << "Conteo actual!\n\nTotal PageFaults: " << fault << "\n";
  cout << "Conteo por procesos: \n";
  for (x = 0; x < N; x++)
  {
    cout << "Proceso " << x << " produjo " << faltasPorProc[x] << " falta(s)\n";
  }
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
  if ((M == 0) || (S == 0) )
  {
    cout << "Has provocado una falta grave! No puedes declarar 0 páginas, 0 palabras o 0 procesos! EXIT!\n";
    return 0;
  }
  chance = new int*[M];
  memoriaFisica = new string*[M];
  faltasPorProc = new int[N];
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
    if( (lock == false) && ( (k == "s") || (k == "f") || (k == "l") ) )
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
      if (compruebaComando(k) == true) //Es k válido
      {
	salvaBugs = 0;
	lock = 1;
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
	  if(method == 's')
	  {
	    cout << "Wow, Second Oportunity te dió un 1!\n";
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
