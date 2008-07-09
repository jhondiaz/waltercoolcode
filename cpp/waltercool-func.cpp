using namespace std;

int[] burbujaMalvada(int* array, int size, int dir)
{
  for(int x = 0; x < size; x++)
  {
    for(int y = 0; y < size; y++)
    {
      if ((array[x] > array[y]) && dir == 0)
      {
	int p = array[x];
	array[x] = array[y];
	array[y] = p;
      }
      if ((array[x] < array[y]) && dir == 1)
      {
	int p = array[x];
	array[x] = array[y];
	array[y] = p;
      }
    }
  }
  return array;
}

int[] array3d_2dfila(int* array, int largo, int columna)
{
  int[] array2d = new int[largo];
  for(int x = 0; x < largo; x++)
  {
    array2d[x] = array[columna][x];
  }
  return array2d;
}

int[] array3d_3dcolumna(int* array, int largo, int fila)
{
  int[] array2d = new int[largo];
  for(int x = 0; x < largo; x++)
  {
    array2d[x] = array[x][fila];
  }
  return array2d;
}
