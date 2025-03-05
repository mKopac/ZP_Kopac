package testing;

import java.io.*;
public class P8{
	public static String getRandomItem(){
		 String[] items={"sword","shield","potion","armor","ring"};
		 return items[(int)(Math.random()*items.length)];
		}
		public static String encounterMonster(){
		 String[] monsters={"goblin","troll","dragon","orc"};
		 return monsters[(int)(Math.random()*monsters.length)];
		}
		public static int playTurn(String player,int health){
		 java.util.Scanner sc=new java.util.Scanner(System.in);
		 System.out.print("Choose action (fight/run):");
		 String action=sc.next();
		 if(action.equals("fight")){
		  String monster=encounterMonster();
		  System.out.println("You encounter a "+monster);
		  int damage=(int)(Math.random()*16)+5;
		  health-=damage;
		  System.out.println("You take "+damage+" damage");
		 } else if(action.equals("run")){
		  System.out.println("You run away");
		 } else{
		  System.out.println("Invalid action");
		 }
		 return health;
		}
		public static int gameLoop(){
		 java.util.Scanner sc=new java.util.Scanner(System.in);
		 System.out.print("Enter your name:");
		 String player=sc.next();
		 int health=100;
		 java.util.List<String> inventory=new java.util.ArrayList<>();
		 int turns=0;
		 while(health>0 && turns<10){
		  System.out.println("Turn "+(turns+1)+" Health: "+health);
		  System.out.print("Choose (explore/rest):");
		  String choice=sc.next();
		  if(choice.equals("explore")){
		   String item=getRandomItem();
		   System.out.println("You found a "+item);
		   inventory.add(item);
		   health=playTurn(player,health);
		  } else if(choice.equals("rest")){
		   System.out.println("You rest and recover 10 health");
		   health+=10;
		  } else{
		   System.out.println("Invalid choice");
		  }
		  turns++;
		  for(int i=0;i<2;i++){
		   System.out.println("Extra event "+i);
		  }
		 }
		 System.out.println("Game over");
		 System.out.println("Final Health: "+health);
		 System.out.println("Inventory: "+inventory);
		 return health;
		}
		public static int bonusRound(){
		 java.util.Scanner sc=new java.util.Scanner(System.in);
		 int score=0;
		 for(int i=0;i<5;i++){
		  int num=(int)(Math.random()*10)+1;
		  System.out.print("Guess a number between 1 and 10:");
		  int guess=sc.nextInt();
		  if(guess==num){
		   System.out.println("Correct");
		   score+=10;
		  } else{
		   System.out.println("Wrong, number was "+num);
		  }
		 }
		 return score;
		}
		public static void main(String[] args){
		 System.out.println("Welcome to Fantasy Adventure");
		 int finalHealth=gameLoop();
		 System.out.println("Bonus round begins");
		 int score=bonusRound();
		 System.out.println("Your final score is "+score);
		 for(int x=0;x<3;x++){
		  for(int y=0;y<3;y++){
		   System.out.println("Nested loop "+x+","+y);
		  }
		 }
		 System.out.println("Thank you for playing");
		 for(int a=0;a<2;a++){
		  System.out.println("Extra loop "+a);
		 }
		 for(int b=0;b<2;b++){
		  for(int c=0;c<2;c++){
		   System.out.println("Double nested "+b+","+c);
		  }
		 }
		 System.out.println("Game simulation complete");
		 for(int p=0;p<3;p++){
		  System.out.println("Loop "+p);
		 }
		 int totalScore=score+finalHealth;
		 System.out.println("Total score: "+totalScore);
		 for(int i=0;i<2;i++){
		  System.out.println("Additional loop "+i);
		 }
		 System.out.println("Adventure over");
		 for(int j=0;j<2;j++){
		  System.out.println("Final loop "+j);
		 }
		 System.out.println("Simulation ends now");
		}
}
