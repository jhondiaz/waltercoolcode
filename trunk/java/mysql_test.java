import java.sql.*;
import java.io.*;

public class mysql_test
{  

  String userName, password, reply, table, query, insert;
  public static void main (String[] args)
  {
    mysql_test kk = new mysql_test();
    try
    { 
      kk.sql();
    }
    catch (Exception e) { }
    
    
  }
  public void sql() throws IOException
  {
    InputStreamReader isr = new InputStreamReader(System.in);
    BufferedReader br = new BufferedReader (isr);
    Connection conn = null;
    System.out.print("Ingrese username: "); userName = br.readLine();
    System.out.print("Ingrese password: "); password = br.readLine();
    System.out.print("Ingrese tabla: "); table = br.readLine();
    try
    {
      String url = "jdbc:mysql://localhost:3306/" + table;
      String fix = "?useJvmCharsetConverters=true&useOldUTF8Behavior=true";
      String driver = "com.mysql.jdbc.Driver";
      Class.forName(driver).newInstance();
      conn = DriverManager.getConnection (url + fix, userName, password);
      System.out.println ("Database connection established");
    }
    catch (Exception e)
    {
      System.err.println ("Cannot connect to database server");
    }
    if (conn != null)
    {
      while(true)
      {
        System.out.print("What you want do? "); reply = br.readLine();
        if (reply.equals("q")) { break; }
        if (reply.equals("query"))
        {
          System.out.print("What query? "); query = br.readLine();
          try
          {
            Statement s = conn.createStatement();
            s.executeQuery(query);
            ResultSet rs = s.getResultSet();
            ResultSetMetaData rsmd = rs.getMetaData();
            int row = rsmd.getColumnCount();
            while(rs.next())
            {
              for(int x=1; x <= row; x++)
              {
                System.out.print(rsmd.getColumnName(x) + ": ");
                System.out.print(rs.getString(x) + " ");
              }
              System.out.println();
            }
            rs.close();
          }
          catch(Exception e)
          {
            System.out.println(e);
          }
        }
        if (reply.equals("mod"))
        {
          System.out.print("What sql command? "); insert = br.readLine();
          try
          {
            Statement s = conn.createStatement();
            s.executeUpdate(insert);
          }
          catch(Exception e)
          {
            System.out.println(e);
          }
        }
      }
      try
      {
        conn.close ();
        System.out.println ("Database connection terminated");
      }
    catch (Exception e) { /* ignore close errors */ }
    }
  }
}
