package testing;

public class P6{
	public static String fetchContent(String url){
		 return "Content of " + url;
		}
		public static int parseContent(String content){
		 String[] words=content.split(" ");
		 return words.length;
		}
		public static void main(String[] args){
		 String[] urls={"http://site1.com","http://site2.com","http://site3.com","http://site4.com"};
		 java.util.List<String> results=new java.util.ArrayList<>();
		 for(int i=0;i<urls.length;i++){
		  String content=fetchContent(urls[i]);
		  int wordCount=parseContent(content);
		  results.add(urls[i]+" -> "+wordCount);
		 }
		 System.out.println("Scraping results:");
		 for(String r:results){
		  System.out.println(r);
		 }
		 int sum=0;
		 for(String r:results){
		  String[] parts=r.split("->");
		  sum+=Integer.parseInt(parts[1].trim());
		 }
		 double avg=(double)sum/results.size();
		 System.out.println("Average word count: "+avg);
		 for(int i=0;i<3;i++){
		  for(int j=0;j<3;j++){
		   System.out.println("Loop "+i+","+j);
		  }
		 }
		 int x=(int)(Math.random()*10);
		 int y=(int)(Math.random()*10);
		 System.out.println("Random numbers: "+x+", "+y);
		 if(x>y)
		  System.out.println("x is greater");
		 else if(x<y)
		  System.out.println("y is greater");
		 else
		  System.out.println("x equals y");
		 for(int k=0;k<2;k++){
		  System.out.println("Extra loop "+k);
		 }
		 System.out.println("Web scraping simulation complete");
		 for(int p=0;p<2;p++){
		  System.out.println("Final loop "+p);
		 }
		 System.out.println("Program finished");
		}
}
