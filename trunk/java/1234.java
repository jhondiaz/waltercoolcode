public qwerty2
{
  public preg2()
  {
    try
    {
      Connection con = DriverManager.getConnection(ventas,venta,vevnta)
      Statement stmt = con.createStatement();
      Resultset rs = stmt.executeQuery("SELECT * FROM Ventas WHERE fecha_venta<\"8 de Julio del 2008\"");
      Resultset rs0 = stmt.executeQuery("SELECT * FROM Vendedores");
      Resultset rs1 = stmt.executeQuery("SELECT * FROM Productos");
      Resultset rs2 = stmt.executeQuery("SELECT * FROM Vendedores WHERE edad>25 AND edad<35");
      
      if(rs2.first())
      {
	System.out.println(rs2.getString("nombre"));
	System.out.println(rs2.getString("Rut));
	while(rs2.next())
	{
	  System.out.println(rs2.getString("nombre"));
	  System.out.println(rs2.getString("Rut));
	}
      }
      stmt.close();
      con.close();
    }
  }
}