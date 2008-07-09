#include <iostream>
#include <pthread.h>
#include <semaphore.h>
using namespace std;




pthread_mutex_t lock;


void *metodo(void *numero)
{
 int n;
 n = ((int)numero);
 pthread_mutex_lock(&lock);
 for(int i = 0 ; i < n ; i ++)
 {
  
  cout<<i<<endl;
  
 }
  pthread_mutex_unlock(&lock); 

}


int main()
{

  
 pthread_t thread1;
 pthread_t thread2;
 pthread_t thread3;
 pthread_mutex_init(&lock,NULL);


 int ThreadId1;
 int ThreadId2;
 int ThreadId3;
 int numero;
 cin>>numero;
 
 ThreadId1 = pthread_create(&thread1,NULL,metodo,(void*)numero);
 ThreadId2 = pthread_create(&thread2,NULL,metodo,(void*)numero);
 ThreadId3 = pthread_create(&thread3,NULL,metodo,(void*)numero);

 pthread_join(thread1,NULL); 
 pthread_join(thread2,NULL); 
 pthread_join(thread3,NULL); //esto hace que el main no continue hasta que el thread thread deje de ejecutar, de otra forma
			    // al temrinar el main, se terminara el thread forzadamente, aunque este este en la mitad de un proceso
 
 



 

}

