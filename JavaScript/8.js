function getRandomItem(){
  var items=["sword","shield","potion","armor","ring"];
  return items[Math.floor(Math.random()*items.length)];
}
function encounterMonster(){
  var monsters=["goblin","troll","dragon","orc"];
  return monsters[Math.floor(Math.random()*monsters.length)];
}
function playTurn(player, health){
  var action = prompt("Choose action (fight/run):");
  if(action==="fight"){
    var monster = encounterMonster();
    console.log("You encounter a "+monster);
    var damage = Math.floor(Math.random()*16)+5;
    health -= damage;
    console.log("You take "+damage+" damage");
  } else if(action==="run"){
    console.log("You run away");
  } else {
    console.log("Invalid action");
  }
  return health;
}
function gameLoop(){
  var player = prompt("Enter your name:");
  var health = 100;
  var inventory = [];
  var turns = 0;
  while(health>0 && turns<10){
    console.log("Turn "+(turns+1)+" Health: "+health);
    var choice = prompt("Choose (explore/rest):");
    if(choice==="explore"){
      var item = getRandomItem();
      console.log("You found a "+item);
      inventory.push(item);
      health = playTurn(player, health);
    } else if(choice==="rest"){
      console.log("You rest and recover 10 health");
      health += 10;
    } else {
      console.log("Invalid choice");
    }
    turns++;
    for(var i=0;i<2;i++){
      console.log("Extra event "+i);
    }
  }
  console.log("Game over");
  console.log("Final Health: "+health);
  console.log("Inventory: "+inventory);
  return health;
}
function bonusRound(){
  var score = 0;
  for(var i=0;i<5;i++){
    var num = Math.floor(Math.random()*10)+1;
    var guess = parseInt(prompt("Guess a number between 1 and 10:"));
    if(guess===num){
      console.log("Correct");
      score += 10;
    } else {
      console.log("Wrong, number was "+num);
    }
  }
  return score;
}
console.log("Welcome to Fantasy Adventure");
var finalHealth = gameLoop();
console.log("Bonus round begins");
var score = bonusRound();
console.log("Your final score is "+score);
for(var x=0;x<3;x++){
  for(var y=0;y<3;y++){
    console.log("Nested loop "+x+","+y);
  }
}
console.log("Thank you for playing");
for(var a=0;a<2;a++){
  console.log("Extra loop "+a);
}
for(var b=0;b<2;b++){
  for(var c=0;c<2;c++){
    console.log("Double nested "+b+","+c);
  }
}
console.log("Game simulation complete");
for(var p=0;p<3;p++){
  console.log("Loop "+p);
}
var totalScore = score + finalHealth;
console.log("Total score: "+totalScore);
for(var i=0;i<2;i++){
  console.log("Additional loop "+i);
}
console.log("Adventure over");
for(var j=0;j<2;j++){
  console.log("Final loop "+j);
}
console.log("Simulation ends now");
for(var k=0;k<2;k++){
  for(var l=0;l<2;l++){
    console.log("Nested final "+k+","+l);
  }
}
console.log("Thank you");
console.log("Goodbye");
