//Sqlite test example

#import <iostream>
#import <sqlite3.h>
using namespace std;

bool databaseCreation(sqlite3 *db)
{
  cout << "No existe la tabla H, creando...";
  sqlite3_exec(db, "create table H(ID int primary key, NAME varchar, DVD varchar, PC book, FULL bool)", NULL, 0, 0);
}

bool sqlAdd(sqlite3 *db, string name, string dvd, bool pc, bool full)
{
  sqlite_exec("insert into H",0,0,0)
}

int main()
{
  sqlite3 *db;
  char *zErrMsg = 0;
  int rc;
  rc = sqlite3_open("waltercool.db", &db);
  rc = sqlite3_exec(db, "select * from H where ID = 0", NULL, 0, &zErrMsg);
  //if(rc == 
  //rc = sqlite3_exec(db, "insert into table2 (bla)values('poep')", NULL, 0, &zErrMsg);
  if( rc != SQLITE_OK )
  {
    sqlite3_free(zErrMsg);
    databaseCreation(db);
  }
  sqlite3_close(db);
  cout << "\n";
}
