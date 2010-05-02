import java.net.*;
import java.io.*;

//Parámetros importantes, necesita como parametro 1 la ubicación del servidor, osea, localhost o la IP y el mensaje como segundo parámetro.

public class Client 
{
  public static void main(String args[]) throws Exception 
  {
    Socket socket = new Socket(args[0], 6500); //Me conecto al servidor X en el puerto 6500
    BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream())); //Objeto para recibir mensaje del server.
    PrintStream ps = new PrintStream(socket.getOutputStream()); //Objeto para enviar mensaje al server
    ps.println(args[1]); //Le envío la información Y al servidor
    System.out.println("Received: " + br.readLine()); //Imprimo lo que me envió el servidor
    socket.close(); //Cierro la conexión.
    }
}

