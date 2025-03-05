package testing;

public class P3{
	public static void sort(int[] arr){
		 int n=arr.length;
		 for(int i=0;i<n;i++){
		  for(int j=0;j<n-i-1;j++){
		   if(arr[j]>arr[j+1]){
		    int temp=arr[j];
		    arr[j]=arr[j+1];
		    arr[j+1]=temp;
		   }
		  }
		 }
		}
		public static void main(String[] args){
		 int[] array={64,34,25,12,22,11,90,88,76,55};
		 sort(array);
		 System.out.println("Sorted array:");
		 for(int i=0;i<array.length;i++){
		  System.out.print(array[i]+" ");
		 }
		 System.out.println();
		 for(int i=0;i<2;i++){
		  System.out.println("Loop "+i);
		 }
		 for(int i=0;i<2;i++){
		  for(int j=0;j<2;j++){
		   System.out.println("Nested loop "+i+","+j);
		  }
		 }
		 System.out.println("Bubble sort complete");
		 for(int x=0;x<2;x++){
		  System.out.println("Extra loop "+x);
		 }
		 for(int y=0;y<2;y++){
		  System.out.println("Another loop "+y);
		 }
		 System.out.println("End of program");
		 for(int z=0;z<1;z++){
		  System.out.println("Final loop "+z);
		 }
		}
}

