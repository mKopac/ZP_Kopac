package testing;

public class P1 {
	public static double calc(double x,double y,String op){
		 if(op.equals("+"))
		  return x+y;
		 else if(op.equals("-"))
		return x-y;
		 else if(op.equals("*")){
		  return x*y;
		}else if(op.equals("/"))
		  return x/y;
		 else return 0;
		}
		public static void main(String[] args){
		 java.util.Scanner sc=new java.util.Scanner(System.in);
		 System.out.print("Enter first number: ");
		 double a=sc.nextDouble();
		System.out.print("Enter second number: ");
		 double b=sc.nextDouble();
		System.out.print("Enter operator (+,-,*,/): ");
		 String op=sc.next();
		 double result=calc(a,b,op);
		 if(result==0)
		  System.out.println("Invalid operator");
		 else System.out.println("Result: "+result);
		 for(int i=0;i<3;i++){
		  System.out.println("Loop "+i);
		 }
		 for(int i=0;i<2;i++){
		  for(int j=0;j<2;j++){
		   System.out.println("Nested loop "+i+","+j);
		  }
		 }
		 sc.close();
		}
		}
