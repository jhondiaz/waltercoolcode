#include <iostream>
using namespace std;

int add(int length, string *data)
{
  int x;
  for(x = 0; x < length; x++)
  {
      if (x == 0) getline(cin, data[x]); //Bug?
      getline(cin, data[x]);
      //cout << "PEPE: " << data[x];
  }
  return 0;
}

int main()
{
  int x = 0, y = 0, z, times, cases, min = -1;
  cin >> cases;
  for(z = 0; z < cases; z++) //Big For
  {
    int namesLength, valuesLength;
    cin >> namesLength;
    string *names = new string[namesLength];
    add(namesLength, names); //Add Names
    cin >> valuesLength;
    string *values = new string[valuesLength];
    add(valuesLength, values); //Add Values
    for(x = 0; x < namesLength; x++) //Check... bubblesort method
    {
      times = 0;
      for(y = 0; y < valuesLength; y++)
      {
	if(values[y] == names[x])
	{
	  times++;
	}
      }
      if ( (min == -1) || (min > times) )//If min isnt setted, set it!
      {
	min = times;
      }
    }
    cout << min << "\n";
  }
}
