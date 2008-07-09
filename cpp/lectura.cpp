#include <stdio.h>

int main()
{
   FILE * pFile;
   char buffer [100];

   pFile = fopen ("Objeto.cpp" , "r");
   if (pFile == NULL) perror ("Error opening file");
   else
   {
     while ( ! feof (pFile) )
     {
       fgets (buffer , 100 , pFile);
       fputs (buffer , stdout);
     }
     fclose (pFile);
   }
   return 0;
}

