def add_student(students,name,age,grade):
 students.append({"name":name,"age":age,"grade":grade})
def remove_student(students,name):
 for i in range(len(students)):
  if students[i]["name"]==name:
   del students[i]
   break
def average_grade(students):
 total=0
 for s in students:
  total+=s["grade"]
 return total/len(students) if students else 0
students=[]
add_student(students,"Alice",20,85)
add_student(students,"Bob",21,90)
add_student(students,"Charlie",19,78)
add_student(students,"David",22,92)
add_student(students,"Eva",20,88)
print("Initial list:")
for s in students:
 print(s)
remove_student(students,"Charlie")
print("After removal:")
for s in students:
 print(s)
avg=average_grade(students)
print("Average grade:",avg)
students.sort(key=lambda s:s["grade"])
print("Sorted by grade:")
for s in students:
 print(s)
for i in range(3):
 for j in range(2):
  print("Loop",i,j)
print("Final student count:",len(students))
x=0
while x<3:
 print("While loop iteration",x)
 x+=1
for k in range(2):
 print("Extra loop",k)
print("Student database simulation complete")
for p in range(2):
 print("Additional loop",p)
for y in range(2):
 print("Another loop",y)
print("Simulation done")
print("All operations complete")
for z in range(1):
 print("Final loop",z)
