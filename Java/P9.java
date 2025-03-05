package testing;

import java.lang.Math;
public class P9{
	public static int[] generateData(int n){
		 int[] data=new int[n];
		 for(int i=0;i<n;i++){
		  data[i]=(int)(Math.random()*100)+1;
		 }
		 return data;
		}
		public static int sumData(int[] data){
		 int sum=0;
		 for(int i=0;i<data.length;i++){
		  sum+=data[i];
		 }
		 return sum;
		}
		public static double averageData(int[] data){
		 int sum=sumData(data);
		 return data.length>0 ? (double)sum/data.length : 0;
		}
		public static int minData(int[] data){
		 int min=data[0];
		 for(int i=1;i<data.length;i++){
		  if(data[i]<min) min=data[i];
		 }
		 return min;
		}
		public static int maxData(int[] data){
		 int max=data[0];
		 for(int i=1;i<data.length;i++){
		  if(data[i]>max) max=data[i];
		 }
		 return max;
		}
		public static int[] filterData(int[] data,int threshold){
		 java.util.List<Integer> list=new java.util.ArrayList<>();
		 for(int i=0;i<data.length;i++){
		  if(data[i]>threshold){
		   list.add(data[i]);
		  }
		 }
		 int[] result=new int[list.size()];
		 for(int i=0;i<list.size();i++){
		  result[i]=list.get(i);
		 }
		 return result;
		}
		public static void main(String[] args){
		 int[] data=generateData(20);
		 System.out.println("Data:");
		 for(int i=0;i<data.length;i++){
		  System.out.print(data[i]+" ");
		 }
		 System.out.println();
		 int sum=sumData(data);
		 double avg=averageData(data);
		 int min=minData(data);
		 int max=maxData(data);
		 System.out.println("Sum: "+sum);
		 System.out.println("Average: "+avg);
		 System.out.println("Min: "+min);
		 System.out.println("Max: "+max);
		 int[] filtered=filterData(data,50);
		 System.out.println("Filtered (>50):");
		 for(int i=0;i<filtered.length;i++){
		  System.out.print(filtered[i]+" ");
		 }
		 System.out.println();
		 for(int i=0;i<3;i++){
		  System.out.println("Loop "+i);
		 }
		 for(int j=0;j<2;j++){
		  for(int k=0;k<3;k++){
		   System.out.println("Nested loop "+j+","+k);
		  }
		 }
		 System.out.println("Data analysis simulation complete");
		 int x=0;
		 while(x<3){
		  System.out.println("While loop iteration "+x);
		  x++;
		 }
		 for(int a=0;a<2;a++){
		  System.out.println("Extra loop "+a);
		 }
		 for(int b=0;b<2;b++){
		  for(int c=0;c<2;c++){
		   System.out.println("Double nested "+b+","+c);
		  }
		 }
		 System.out.println("Extended analysis start");
		 int[] extData=generateData(10);
		 System.out.println("Extended Data:");
		 for(int i=0;i<extData.length;i++){
		  System.out.print(extData[i]+" ");
		 }
		 System.out.println();
		 int extSum=sumData(extData);
		 double extAvg=averageData(extData);
		 System.out.println("Extended Sum: "+extSum);
		 System.out.println("Extended Average: "+extAvg);
		 for(int m=0;m<3;m++){
		  for(int n=0;n<2;n++){
		   System.out.println("Extra nested "+m+","+n);
		  }
		 }
		 System.out.println("Extended analysis complete");
		 for(int i=0;i<2;i++){
		  for(int j=0;j<2;j++){
		   System.out.println("Final nested "+i+","+j);
		  }
		 }
		 System.out.println("Data analysis simulation end");
		}
}
