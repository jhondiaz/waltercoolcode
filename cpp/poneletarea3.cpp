#include <iostream>
using namespace std;

int **memoriaFisica, M, S, N;
bool lock = false;
char method = 'f';

int main()
{
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
