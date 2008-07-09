#include <stdio.h>
#include <string.h>

int write(char fileName[], int times, char text[]);
int FIFO();
int SJNT();
int SJN();
int PPCE();
int PPSE();
int RR();
int ToIntArray(char P[], int status);
int llenaDatos(char name[], int proces);
main()
{
	int totalProcesos;
	int tiempo;
	printf("Ingrese el tiempo a simular: ");
	scanf("%d",&tiempo);
	tiempo;
	printf("Ingrese la cantidad de procesos a ingresar: ");
	scanf("%d",&totalProcesos);
	int max = write("trick.text", totalProcesos, "Ingrese el proceso ");
	int datos[totalProcesos][max] = llenaDatos("trick.text", totalProcesos, max);
	//printf("%d",FIFO()); //FIFO
	//printf("%d",SJNT()); //SJN Trampa
	//printf("%d",SJN()); //SJN
	//printf("%d",PPCE()); //PP con Exp.
	//printf("%d",PPSE()); //PP sin Exp.
	//printf("%d",RR()); //RR
	printf("\n%d\n",max);
}

int[][] llenaDatos(char name[], int proces, int maximo)
{
	FILE * pFile;
	char P [100];
	int counter = 0;
	int valores[proces][maximo];
	pFile = fopen (name , "r");
	for(forX = 0; forX < times; forX++)
	{
		if (pFile == NULL) perror ("No se detectó %s!", name);
		else {
			fgets (P , 100 , pFile);
			valores[counter] = toIntArray(P, 1);
			fclose (pFile);
		}
		fputs(P, pFile);
		fputs("\n", pFile);
		int tempore = toIntArray(P, 0);
		if (max < tempore) max = tempore;
	}
}

int write(char fileName[], int times, char text[])
{
	FILE * pFile;
	pFile = fopen ( fileName , "wb" );
	char P [100];
	int forX;
	int max = 0;
	for(forX = 0; forX < times; forX++)
	{
		printf("%s %d : ",text, forX+1);
		scanf("%s",P);
		fputs(P, pFile);
		fputs("\n", pFile);
		int tempore = toIntArray(P, 0);
		if (max < tempore) max = tempore;
	}
	fclose (pFile); //Guardado
	return  max;
}

int toIntArray(char P[], int status)
{
	int x = 0;
	//printf("\nFunciono");
	if (status == 1)
	{
		char * buff;
		int dat[];
		buff = strtok(P,":,");
		buff = strtok(NULL,":,");
		while (buff != NULL)
		{
			buff = strtok(NULL,":,");
			int dat[x] = (int)buff;
			++x;
		}
		return dat;
	}
	else
	{
		char * buff;
		buff = strtok(P,":,");
		buff = strtok(P,":,");
		while (buff != NULL)
		{
			buff = strtok(NULL,":,");
			++x;
		}
		//printf("\n%d\n",x);
		return x;
	}
}

int FIFO()
{
	printf("\nInicio de FIFO\n\n");
	return 0;
}
int SJNT()
{
	printf("\nInicio de SJN con Trampa\n\n");
	return 0;
}
int SJN()
{
	printf("\nInicio de SJN sin Trampa\n\n");
	return 0;
}
int PPSE()
{
	printf("\nInicio de Por Prioridad sin expropiación\n\n");
	return 0;
}
int PPCE()
{
	printf("\nInicio de Por Prioridad con expropiación\n\n");
	return 0;
}
int RR()
{
	printf("\nInicio de Round Robin\n\n");
	return 0;
}
