package testing;

import java.util.Scanner;
import java.util.Random;
public class P10{
	public static java.util.List<java.util.Map<String,Double>> generateWeatherData(int days){
		 java.util.List<java.util.Map<String,Double>> data=new java.util.ArrayList<>();
		 for(int d=0;d<days;d++){
		  java.util.Map<String,Double> record=new java.util.HashMap<>();
		  record.put("day",(double)(d+1));
		  record.put("temp",Math.random()*45-10);
		  record.put("humidity",Math.random()*80+20);
		  record.put("wind",Math.random()*20);
		  data.add(record);
		 }
		 return data;
		}
		public static double averageTemperature(java.util.List<java.util.Map<String,Double>> data){
		 double total=0;
		 for(java.util.Map<String,Double> record:data){
		  total+=record.get("temp");
		 }
		 return data.size()>0 ? total/data.size() : 0;
		}
		public static double maxWind(java.util.List<java.util.Map<String,Double>> data){
		 double max=0;
		 for(java.util.Map<String,Double> record:data){
		  if(record.get("wind")>max) max=record.get("wind");
		 }
		 return max;
		}
		public static java.util.List<java.util.Map<String,Double>> filterHotDays(java.util.List<java.util.Map<String,Double>> data,double threshold){
		 java.util.List<java.util.Map<String,Double>> hot=new java.util.ArrayList<>();
		 for(java.util.Map<String,Double> record:data){
		  if(record.get("temp")>threshold){
		   hot.add(record);
		  }
		 }
		 return hot;
		}
		public static void printWeatherData(java.util.List<java.util.Map<String,Double>> data){
		 for(java.util.Map<String,Double> record:data){
		  System.out.println("Day "+record.get("day")+", Temp: "+record.get("temp")+", Humidity: "+record.get("humidity")+", Wind: "+record.get("wind"));
		 }
		}
		public static void main(String[] args){
		 java.util.List<java.util.Map<String,Double>> weather=generateWeatherData(15);
		 System.out.println("Weather Data:");
		 printWeatherData(weather);
		 double avgTemp=averageTemperature(weather);
		 System.out.println("Average Temperature: "+avgTemp);
		 double maxWindSpeed=maxWind(weather);
		 System.out.println("Maximum Wind Speed: "+maxWindSpeed);
		 java.util.List<java.util.Map<String,Double>> hotDays=filterHotDays(weather,25);
		 System.out.println("Hot Days:");
		 printWeatherData(hotDays);
		 for(int i=0;i<3;i++){
		  for(int j=0;j<2;j++){
		   System.out.println("Nested loop "+i+","+j);
		  }
		 }
		 int totalRecords=weather.size();
		 System.out.println("Total records: "+totalRecords);
		 double sumTemp=0;
		 for(java.util.Map<String,Double> record:weather){
		  sumTemp+=record.get("temp");
		 }
		 double avgTemp2=totalRecords>0 ? sumTemp/totalRecords : 0;
		 System.out.println("Calculated Average Temperature: "+avgTemp2);
		 for(int a=0;a<2;a++){
		  System.out.println("Extra loop "+a);
		 }
		 for(int b=0;b<2;b++){
		  for(int c=0;c<2;c++){
		   System.out.println("Double nested "+b+","+c);
		  }
		 }
		 System.out.println("Additional analysis start");
		 java.util.List<Double> tempList=new java.util.ArrayList<>();
		 for(java.util.Map<String,Double> record:weather){
		  tempList.add(record.get("temp"));
		 }
		 System.out.println("Temperatures: "+tempList);
		 double maxTemp=tempList.get(0);
		 double minTemp=tempList.get(0);
		 for(double t:tempList){
		  if(t>maxTemp) maxTemp=t;
		  if(t<minTemp) minTemp=t;
		 }
		 System.out.println("Max Temp: "+maxTemp);
		 System.out.println("Min Temp: "+minTemp);
		 double diff=maxTemp-minTemp;
		 System.out.println("Temperature Difference: "+diff);
		 for(int p=0;p<2;p++){
		  System.out.println("Loop p "+p);
		 }
		 for(int q=0;q<2;q++){
		  System.out.println("Loop q "+q);
		 }
		 for(int r=0;r<2;r++){
		  for(int s=0;s<2;s++){
		   System.out.println("Nested r,s "+r+","+s);
		  }
		 }
		 System.out.println("Additional analysis complete");
		 java.util.Map<String,Double> finalSummary=new java.util.HashMap<>();
		 finalSummary.put("Summary",totalRecords*1.0);
		 System.out.println("Final summary: "+finalSummary);
		 System.out.println("Simulation ends now");
		 System.out.println("Goodbye");
		 for(int i=0;i<2;i++){
		  System.out.println("Final loop "+i);
		 }
		 System.out.println("End of Weather Data Analysis");
		}
		}