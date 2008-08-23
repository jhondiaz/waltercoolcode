public qwerty
{
  public uno()
  {
    
  }
  
  int tiempo(String X, String Y, Tren Z)
  {
    String p;
    int tiempo1 = Z.kilometro(X);
    int tiempo2 = Z.kilometro(Y);
    int tiempoTotal = 0;
    if(tiempo1 < tiempo2)
    {
      p = tiempo1;
    }
    else p = tiempo2;
    while(true)
    {
      P = Z.siguiente(P);
      tiempoTotal+2;
      if(P == Y)
      {
	break;
      }
    }
    return (tiempoTotal + p);
  }
  
}

{
  
  void insertar(String X, int Y)
  {
    estacion[N] = X;
    km[N] = Y;
    N++;
  }
  int kilometro(String X)
  {
    for(int x = 0; x < N; x++)
    {
      if(estacion[x] == X)
      {
	return km[N];
      }
    }
    return -1;
  }
  
  String estacion(int X)
  {
    for(int x = 0; x < N; x++)
    {
      if(km[x] == X)
      {
	return estacion[N];
      }
    }
    return -1;
  }
  
  String siguiente(String X)
  {
    for(int x = 0; x < N; x++)
    {
      if(estacion[x] == X)
      {
	return estacion[N+1];
      }
    }
    return -1;
  }
  
  String anterior(String X)
  {
    for(int x = 0; x < N; x++)
    {
      if(estacion[x] == X)
      {
	return estacion[N-1];
      }
    }
    return -1;
  }
}