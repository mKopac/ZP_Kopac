package testing;

public class P5{
	public static void addStudent(java.util.List<java.util.Map<String,Object>> students,String name,int age,double grade){
		 java.util.Map<String,Object> student=new java.util.HashMap<>();
		 student.put("name",name);
		 student.put("age",age);
		 student.put("grade",grade);
		 students.add(student);
		}
		public static void removeStudent(java.util.List<java.util.Map<String,Object>> students,String name){
		 for(int i=0;i<students.size();i++){
		  if(students.get(i).get("name").equals(name)){
		   students.remove(i);
		   break;
		  }
		 }
		}
		public static double averageGrade(java.util.List<java.util.Map<String,Object>> students){
		 double total=0;
		 for(java.util.Map<String,Object> s:students){
		  total+= (double)s.get("grade");
		 }
		 return students.size()>0 ? total/students.size() : 0;
		}
		public static void main(String[] args){
		 java.util.List<java.util.Map<String,Object>> students=new java.util.ArrayList<>();
		 addStudent(students,"Alice",20,85.5);
		 addStudent(students,"Bob",21,90.0);
		 addStudent(students,"Charlie",19,78.0);
		 addStudent(students,"David",22,92.0);
		 addStudent(students,"Eva",20,88.5);
		 System.out.println("Initial list:");
		 for(java.util.Map<String,Object> s:students){
		  System.out.println(s);
		 }
		 removeStudent(students,"Charlie");
		 System.out.println("After removal:");
		 for(java.util.Map<String,Object> s:students){
		  System.out.println(s);
		 }
		 double avg=averageGrade(students);
		 System.out.println("Average grade: "+avg);
		 students.sort((s1,s2)->Double.compare((double)s1.get("grade"),(double)s2.get("grade")));
		 System.out.println("Sorted by grade:");
		 for(java.util.Map<String,Object> s:students){
		  System.out.println(s);
		 }
		 for(int i=0;i<3;i++){
		  for(int j=0;j<2;j++){
		   System.out.println("Loop "+i+","+j);
		  }
		 }
		 int x=0;
		 while(x<3){
		  System.out.println("While loop iteration "+x);
		  x++;
		 }
		 for(int k=0;k<2;k++){
		  System.out.println("Extra loop "+k);
		 }
		 System.out.println("Student database simulation complete");
		 for(int p=0;p<2;p++){
		  System.out.println("Additional loop "+p);
		 }
		 System.out.println("All operations complete");
		}
}
