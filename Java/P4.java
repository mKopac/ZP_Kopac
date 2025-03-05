package testing;

public class P4{
	public static int countWords(String text){
		 String[] words=text.split(" ");
		 return words.length;
		}
		public static int countCharacters(String text){
		 return text.length();
		}
		public static int countLines(String text){
		 return text.split("\n").length;
		}
		public static void main(String[] args){
		 java.util.Scanner sc=new java.util.Scanner(System.in);
		 System.out.print("Enter text:");
		 String input=sc.nextLine();
		 int words=countWords(input);
		 int chars=countCharacters(input);
		 int lines=countLines(input);
		 System.out.println("Words: "+words);
		 System.out.println("Characters: "+chars);
		 System.out.println("Lines: "+lines);
		 for(int i=0;i<2;i++){
		  System.out.println("Iteration "+i);
		 }
		 for(int j=0;j<2;j++){
		  for(int k=0;k<2;k++){
		   System.out.println("Nested "+j+","+k);
		  }
		 }
		 sc.close();
		}
}
