//Sqlite test example

#import <iostream>
#import <sqlite3.h>
using namespace std;

bool databaseCreation()
{
  
}
int main()
{
  sqlite3 *db;
  char *zErrMsg = 0;
  string rc;
  rc = sqlite3_open("test.db", &db);
  cout << rc;
  rc = sqlite3_exec(db, "select * from data", NULL, 0, &zErrMsg);
  //if(rc == 
  //rc = sqlite3_exec(db, "insert into table2 (bla)values('poep')", NULL, 0, &zErrMsg);
  cout << rc;
  if( rc != SQLITE_OK )
  {
    sqlite3_free(zErrMsg);
    databaseCreation;
  }
  sqlite3_close(db);
  cin.get();
}
