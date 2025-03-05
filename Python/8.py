import random
def get_random_item():
 items=["sword","shield","potion","armor","ring"]
 return random.choice(items)
def encounter_monster():
 monsters=["goblin","troll","dragon","orc"]
 return random.choice(monsters)
def play_turn(player,health):
 action=input("Choose action (fight/run):")
 if action=="fight":
  monster=encounter_monster()
  print("You encounter a",monster)
  damage=random.randint(5,20)
  health-=damage
  print("You take",damage,"damage")
 elif action=="run":
  print("You run away")
 else:
  print("Invalid action")
 return health
def game_loop():
 player=input("Enter your name:")
 health=100
 inventory=[]
 turns=0
 while health>0 and turns<10:
  print("Turn",turns+1,"Health:",health)
  choice=input("Choose (explore/rest):")
  if choice=="explore":
   item=get_random_item()
   print("You found a",item)
   inventory.append(item)
   health=play_turn(player,health)
  elif choice=="rest":
   print("You rest and recover 10 health")
   health+=10
  else:
   print("Invalid choice")
  turns+=1
  for i in range(2):
   print("Extra event",i)
 print("Game over")
 print("Final Health:",health)
 print("Inventory:",inventory)
 return health,inventory
def bonus_round():
 score=0
 for i in range(5):
  num=random.randint(1,10)
  guess=int(input("Guess a number between 1 and 10:"))
  if guess==num:
   print("Correct")
   score+=10
  else:
   print("Wrong, number was",num)
 return score
print("Welcome to Fantasy Adventure")
final_health,inventory=game_loop()
print("Bonus round begins")
score=bonus_round()
print("Your final score is",score)
for x in range(3):
 for y in range(3):
  print("Nested loop",x,y)
print("Thank you for playing")
for a in range(2):
 print("Extra loop",a)
for b in range(2):
 for c in range(2):
  print("Double nested",b,c)
print("Game simulation complete")
for d in range(3):
 print("Loop",d)
score_total=score+final_health
print("Total score:",score_total)
for e in range(2):
 for f in range(3):
  print("Another nested",e,f)
print("Goodbye, adventurer")
for g in range(3):
 print("Final loop",g)
for h in range(2):
 print("Extra final",h)
print("Simulation end")
for i in range(2):
 for j in range(2):
  print("Additional nested",i,j)
for k in range(3):
 print("Closing loop",k)
print("Final simulation complete")
print("Adventure over")
for m in range(2):
 print("Extra step",m)
for n in range(2):
 print("Step complete",n)
print("All done")
print("Ending simulation")
print("Thank you")
print("See you next time")
print("Goodbye")
