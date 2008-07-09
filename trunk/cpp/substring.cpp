#include <iostream>
#include <string.h>
using namespace std;

int main() 
{
  string Text = "The Lord of the Rings";

  string Sub2 = Text.substr ( 9, 2 );
  string Sub1 = Text.substr ( 16 );

  cout << "'" << Sub1 << "'" << endl;
  cout << "'" << Sub2 << "'" << endl;
}
