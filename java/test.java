public class test
{
	public static void main(String[] args) throws Exception
	{
		String inputfilecontents = "1111111111111111111111000000010101010101010101010101010101010101010101010101010101001100101010101010101010";
		for (int i = 0; i<inputfilecontents.length(); i++){
			char c = inputfilecontents.charAt(i);
			inputfilebinary += Integer.toBinaryString(c);
		}
    	
		System.out.println("File binary is : " + inputfilebinary);
	}
}
 
