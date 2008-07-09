#include <iostream>
#include <pthread.h>
#include <semaphore.h>
using namespace std;

int x,y,cantidad,threads,active,method;
int **array;
int modifico;
pthread_mutex_t lock;

int revision()
{
  //Yo reviso si está ordenado.
  for(int kk = 0; kk < cantidad; kk++)
  {
    int ans = array[kk][0];
    for(int pp = 0; pp < cantidad; pp++)
    {
      if( ((kk%2 == 0) && (ans > array[kk][pp])) || ((kk%2 == 1) && (ans < array[kk][pp])) )
      {
	cout << "Oops, ha fallado";
	return 1;
      }
      ans = array[kk][pp];
    }
  }
  return 0;
}

void *leftrightleft(void *num) //Ordeno!
{
  int numeroAsignado = ((int)num);
  pthread_mutex_lock(&lock);
  for(x = 0; x < cantidad; x++)
  {
    for(y = 0; y < cantidad; y++)
    {
      if ( (numeroAsignado%2 == 0) && (array[numeroAsignado][x] > array[numeroAsignado][y]) )//par
      {
	cout << "\nEstoy ordenando de izquierda a derecha ";
	//Yo ordeno de izquierda a derecha
	cout << array[numeroAsignado][x] << "es mayor que " << array[numeroAsignado][y];
	int p = array[numeroAsignado][x];
	array[numeroAsignado][x] = array[numeroAsignado][y];
	array[numeroAsignado][y] = p;
	modifico++;
      }
      else if ( (numeroAsignado%2 == 1) && (array[numeroAsignado][x] < array[numeroAsignado][y] ) )//impar
      {
	cout << "\nEstoy ordenando de derecha a izquierda ";
	//Yo ordeno de derecha a izquierda
	cout << array[numeroAsignado][x] << "es menor que " << array[numeroAsignado][y];
	int p = array[numeroAsignado][x];
	array[numeroAsignado][x] = array[numeroAsignado][y];
	array[numeroAsignado][y] = p;
	modifico++;
      } 
    }
  }
  pthread_mutex_unlock(&lock); 
}

void *updown(void *num) //Todo numero ordeno!
{
  int numeroAsignado = ((int)num);
  pthread_mutex_lock(&lock);
  cout << "\nEstoy ordenando de arriba hacia abajo"; //Yo ordeno de arriba hacia abajo
  for(x = 0; x < cantidad; x++)
  {
    for(y = 0; y < cantidad; y++)
    {
      if ( array[x][numeroAsignado] > array[y][numeroAsignado] ) //par
      {
	cout <<"\n" << array[x][numeroAsignado] << "es mayor que " << array[y][numeroAsignado];
	int p = array[x][numeroAsignado];
	array[x][numeroAsignado] = array[y][numeroAsignado];
	array[y][numeroAsignado] = p;
	modifico++;
      }
    }
  }
  pthread_mutex_unlock(&lock); 
}

int taskManager() //Administro los threads, y administro el paso.
{
  pthread_t tasks[cantidad];
  pthread_mutex_init(&lock,NULL);
  int threadValue[cantidad]; //Nada, no sirve, es referencia
  int threadsInUse = 0; //Threads usados actualmente
  int tasksInUse = 0; //Tareas Completadas
  while(true)
  {
    modifico,tasksInUse= 0;
    while(tasksInUse < cantidad) //Comienza leftrightleft
    {
      while( (threadsInUse < threads) || (tasksInUse != cantidad) ) 
      {
	threadValue[tasksInUse] = pthread_create(&tasks[tasksInUse],NULL,leftrightleft,(void*)tasksInUse);
	threadsInUse++;
	tasksInUse++;
      }
      for(int temp = 0;temp < cantidad; temp++)
      {
	pthread_join(tasks[temp],NULL); //FreeDOM
	threadsInUse--;
      }
    }
    tasksInUse = 0;
    while(tasksInUse < cantidad) //Comienza Up/Down
    {
      while( (threadsInUse < threads)  || (tasksInUse != cantidad) ) 
      {
	threadValue[tasksInUse] = pthread_create(&tasks[tasksInUse],NULL,updown,(void*)tasksInUse);
	threadsInUse++;
	tasksInUse++;
      }
      for(int temp = 0; temp < cantidad; temp++)
      {
	pthread_join(tasks[temp],NULL); //FREEEDOOOOOM
	threadsInUse--;
      }
    }
    cout << "\n" <<modifico;
    if(modifico == 0)
    {
      return 0;
    }	
  }
}

int orden() //Acá yo doy las ordenes!
{
  int p = taskManager();
  cout << "\nShearsort Finalizado";
  cout << "\nResultados:\n\n";
  for(x = 0; x < cantidad; x++)
  {
    for(y = 0; y < cantidad; y++)
    {
      cout << array[x][y] << "    ";
    }
    cout << "\n";
  }
  return 0;
}

int main() //Yo soy main
{
  active,method = 0;
  cout << "Ingrese el valor de la matriz cuadrada: ";
  cin >> cantidad;
  cout << "\nGracias";
  array = new int*[cantidad];
  for( x = 0 ; x < cantidad ; x++ )
  {
   array[x] = new int[cantidad];
  }
  
  for(x = 0;  x < cantidad; x++)
  {
    cout << "\nIngrese los valores de la fila "<< x+1 << ": ";
    for(y = 0; y < cantidad; y++)
    {
      cin >> array[x][y];
    }
  }
  
  cout << "\nGuardados sin problemas :D\nIngrese la cantidad de threads: ";
  cin >> threads;
  cout << "\nGracias\n\nDando inicio al ordenamiento shearsort!!";
  orden(); 
  cout << "\nRevisando si realmente está ordenado";
  int resultado = revision();
  if (resultado == 0)
  {
    cout << "\nEstoy ordenado :D";
  }
  else
  {
    cout << "\nOooops, fallé :'(";
  }
  cout << "\n";
}
