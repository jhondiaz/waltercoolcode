import java.net.*;
import java.io.*;
public class Server 
{
  public static void main(String args[]) throws Exception 
  {
    ServerSocket server = new ServerSocket(6500); //Abro un socket con el puerto 65000
    Socket socket = null;
    while(true) //En espera de mensajes.
    {
      socket = server.accept(); //Acepto una conexión si lo encuentro.
      BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream())); //Objeto para recibir información del cliente.
      PrintStream ps = new PrintStream(socket.getOutputStream()); //Objeto para enviar mensaje al cliente.
      String mensaje = br.readLine();
      ps.println(mensaje); //Le envío de vuelta el mensaje al cliente.
      System.out.println(mensaje);
      socket.close(); //Cierro la conexión, sólo puedo tener una a la vez.
    }
  }
}

