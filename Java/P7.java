package testing;

import java.util.Random;
public class P7{
	public static int[][] multiply(int[][] A,int[][] B){
		 int m=A.length;
		 int n=A[0].length;
		 int p=B[0].length;
		 int[][] result=new int[m][p];
		 for(int i=0;i<m;i++){
		  for(int j=0;j<p;j++){
		   for(int k=0;k<n;k++){
		    result[i][j]+=A[i][k]*B[k][j];
		   }
		  }
		 }
		 return result;
		}
		public static void main(String[] args){
		 int[][] A={{1,2,3},{4,5,6}};
		 int[][] B={{7,8},{9,10},{11,12}};
		 int[][] res=multiply(A,B);
		 System.out.println("Matrix A:");
		 for(int i=0;i<A.length;i++){
		  for(int j=0;j<A[i].length;j++){
		   System.out.print(A[i][j]+" ");
		  }
		  System.out.println();
		 }
		 System.out.println("Matrix B:");
		 for(int i=0;i<B.length;i++){
		  for(int j=0;j<B[i].length;j++){
		   System.out.print(B[i][j]+" ");
		  }
		  System.out.println();
		 }
		 System.out.println("Result:");
		 for(int i=0;i<res.length;i++){
		  for(int j=0;j<res[i].length;j++){
		   System.out.print(res[i][j]+" ");
		  }
		  System.out.println();
		 }
		 for(int i=0;i<2;i++){
		  for(int j=0;j<2;j++){
		   System.out.println("Loop "+i+","+j);
		  }
		 }
		 int x=0;
		 while(x<3){
		  System.out.println("While loop "+x);
		  x++;
		 }
		 for(int i=0;i<2;i++){
		  System.out.println("Extra loop "+i);
		 }
		 System.out.println("Matrix multiplication complete");
		 for(int p=0;p<1;p++){
		  System.out.println("Final loop "+p);
		 }
		}
}
