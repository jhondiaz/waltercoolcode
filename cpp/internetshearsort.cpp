#include<stdio.h>
#include<stdlib.h>
#include<omp.h>
#include<math.h>
int n=3;
int v[][3] = {{3,6,10},{4,9,7},{8,2,9}};
int compare_c(const void *a, const void *b)
{
	return *((int*)a)-*((int*)b);
}

int compare_d(const void *a, const void *b)
{
	return *((int*)b)-*((int*)a);
}

void sortcol(int col)
{
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			if(v[i][col]>v[j][col])
			{
				v[i][col] = v[i][col]^v[j][col];
				v[j][col] = v[i][col]^v[j][col];
				v[i][col] = v[i][col]^v[j][col];
			}
}

void sortlin(int lin)
{
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			if(v[i][col]>v[j][col])
			{
				v[i][col] = v[i][col]^v[j][col];
				v[j][col] = v[i][col]^v[j][col];
				v[i][col] = v[i][col]^v[j][col];
			}
}


int main()
{
	

	int i;
	omp_set_num_threads(4);


	for(i=0;i<0.5*log((double)n);i++)
	{
		#pragma omp parallel for
		for(int j=0;j<n;j+=2)
			qsort(v[j], n, sizeof(int), compare_c);

//#pragma omp barrier

		#pragma omp parallel for
		for(int j=1;j<n;j+=2)
			qsort(v[j], n, sizeof(int), compare_d);
		
		

		#pragma omp parallel for
		for(int j=0;j<n;j++)
			sortcol(j);

	}

	for(i=0;i<n;i++)
	{
		printf("\n");
		for(int j=0;j<n;j++)
			printf("%d ",v[i]);
	}
	printf("\n");
	system("pause");
	return 0;
}