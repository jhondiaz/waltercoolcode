#include <iostream>
using namespace std;

int main () 
{
	int x;
	string p;
	cin >> p;
	for(x = 0; x < 5; x++)
	{
		getline(cin, p);
		cout << p;
	}
	return 0;
}
