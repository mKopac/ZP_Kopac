function addStudent(students, name, age, grade){
  students.push({name: name, age: age, grade: grade});
}
function removeStudent(students, name){
  for(var i=0;i<students.length;i++){
    if(students[i].name === name){
      students.splice(i,1);
      break;
    }
  }
}
function averageGrade(students){
  var total = 0;
  for(var i=0;i<students.length;i++){
    total += students[i].grade;
  }
  return students.length > 0 ? total/students.length : 0;
}
var students = [];
addStudent(students,"Alice",20,85);
addStudent(students,"Bob",21,90);
addStudent(students,"Charlie",19,78);
addStudent(students,"David",22,92);
addStudent(students,"Eva",20,88);
console.log("Initial Students:");
for(var i=0;i<students.length;i++){
  console.log(students[i]);
}
removeStudent(students,"Charlie");
console.log("After Removal:");
for(var i=0;i<students.length;i++){
  console.log(students[i]);
}
var avg = averageGrade(students);
console.log("Average Grade: "+avg);
students.sort(function(a,b){ return a.grade - b.grade; });
console.log("Sorted by Grade:");
students.forEach(function(s){ console.log(s); });
for(var i=0;i<3;i++){
  for(var j=0;j<2;j++){
    console.log("Loop "+i+","+j);
  }
}
var x=0;
while(x<3){
  console.log("While loop iteration "+x);
  x++;
}
for(var k=0;k<2;k++){
  console.log("Extra loop "+k);
}
console.log("Student database simulation complete");
