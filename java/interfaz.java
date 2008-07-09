import java.awt.*;
import javax.swing.*;
class interfaz extends JFrame
{
	JTextField  dado = new JTextField();
	JTextField  cantidad = new JTextField();
	JTextField  dificultad = new JTextField();
	JButton boton = new JButton();
	JTextArea pepe = new JTextArea();
	BorderLayout holi = new BorderLayout();
	public static void main(String args[])
	{
		new interfaz();
	}
	
	public interfaz()
	{
		super.setTitle("Dados Avatar");
		holi.setHgap(10);
		holi.setVgap(10);
		boton.setText("Tirar");
		this.getContentPane().setLayout(holi);
		this.getContentPane().add(boton, BorderLayout.NORTH);
		this.getContentPane().add(dado, BorderLayout.WEST);
		this.getContentPane().add(cantidad, BorderLayout.CENTER);
		this.getContentPane().add(dificultad, BorderLayout.EAST);
		this.getContentPane().add(pepe, BorderLayout.SOUTH);
		super.pack();
		super.show();
	}

}