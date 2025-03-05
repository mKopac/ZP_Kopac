package testing;

public class P2{
	public static int[] generateFib(int n){
		 int[] fib=new int[n];
		 if(n>0) fib[0]=0;
		 if(n>1) fib[1]=1;
		 for(int i=2;i<n;i++){
		  fib[i]=fib[i-1]+fib[i-2];
		 }
		 return fib;
		}
		public static void main(String[] args){
		 java.util.Scanner scanner=new java.util.Scanner(System.in);
		 System.out.print("Enter number of terms:");
		 int n=scanner.nextInt();
		 int[] result=generateFib(n);
		 for(int i=0;i<result.length;i++){
		  System.out.print(result[i]+" ");
		 }
		 System.out.println();
		 for(int i=0;i<3;i++){
		  System.out.println("Iteration "+i);
		 }
		 scanner.close();
		}
}

