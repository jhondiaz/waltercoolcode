class Nodo
{
	String contenido;
	int profundidad;
	Nodo derecho;
	Nodo izquierdo;
	
	public Nodo(String contenido, int peso)
	{
		this.contenido = contenido;
		profundidad = peso;
		derecho = null;
		izquierdo = null;
	}
	public String toString()
	{
		return profundidad + " # " + contenido;
	}
}