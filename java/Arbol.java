import java.util.ArrayList;
class Arbol
{
	Nodo raiz;
	String[] cont;
	Nodo[] nod;
	Nodo papa;
	
	public Arbol(Nodo raiz)
	{
		this.raiz = raiz;
		nod=new Nodo[1000];
		cont=new String[1000];
	}
	
	public void insertar(Nodo puntero, String elemento)
	{
		if (puntero != null)
		{
			if (elemento.compareTo(puntero.contenido)<0)
				if(puntero.izquierdo != null) insertar(puntero.izquierdo, elemento);
				else puntero.izquierdo = new Nodo(elemento, puntero.profundidad + 1);
			else
				if(puntero.derecho != null) insertar(puntero.derecho, elemento);
				else puntero.derecho = new Nodo(elemento, puntero.profundidad + 1);
			
		}
	}
	public Nodo buscar(Nodo puntero, String elemento){
	
		if (puntero != null)
		{
			if (elemento.compareTo(puntero.contenido)>0)
				if(puntero.izquierdo != null) return buscar(puntero.izquierdo, elemento);
				else{ System.out.println("no existe elemento");
					return puntero;
				}
			else if(elemento.compareTo(puntero.contenido)==0){
				
				return puntero;
			}
			else
				if(puntero.derecho != null) return buscar(puntero.derecho, elemento);
				else{ System.out.println("no existe elemento");
					return puntero;	
				}
			
		}
		return raiz;
		
		
		}
	
	public void eliminar(String elemento)
	{
		Nodo ubicacion=buscar(raiz,elemento);
		if(elemento.compareTo(ubicacion.contenido)!=0){
			System.out.println("no se encontro elemento");
			}
		else podar(ubicacion); 
			 
	}
	public void podar(Nodo puntero){
		int i=0;
		papa=puntero;
		while(i>=0){
		
		while(puntero.izquierdo!=null){
			
			cont[i]=(puntero.izquierdo).contenido;
			nod[i]=puntero;			
			puntero=puntero.izquierdo;
			i++;
			}
		while(((nod[i]).derecho==null) || (i<0)){
			
			i--;
			
			}
			if(i<0) break;
			puntero=nod[i].derecho;
		cont[i]=(puntero.contenido);
	
		}
		
		papa=null;
		String contenido;
		
		for(int j=0;j<100;j++){
			contenido=cont[j];
			insertar(raiz,contenido);
		}
	}
	
	public void imprimir(Nodo puntero)
	{
		if(puntero != null)
		{
			imprimir(puntero.izquierdo);
			System.out.println(puntero);
			imprimir(puntero.derecho);
			
		}
	}
	
	public static void main(String[] args)
	{
		Arbol a = new Arbol(new Nodo("b",0));
//		a.imprimir(a.raiz);
		a.insertar(a.raiz,"c");
//		a.imprimir(a.raiz);
		a.insertar(a.raiz,"a");
		a.insertar(a.raiz, "aa");
		a.insertar(a.raiz, "bb");
		a.insertar(a.raiz, "cc");
		a.insertar(a.raiz, "z");
		a.insertar(a.raiz, "ccc");
		a.imprimir(a.raiz);
		//a.eliminar(a.raiz, "cc");
		a.imprimir(a.raiz);
	
	}	
}