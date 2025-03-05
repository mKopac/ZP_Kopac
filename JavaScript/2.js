function fibonacci(n){
  if(n<=0){
   return [];
  } else if(n===1){
    return [0];
  } else {
  var seq = [0,1];
  for(var i=2;i<n;i++){
   seq.push(seq[i-1]+seq[i-2]);
  }
  return seq;
  }
}
var n = parseInt(prompt("Enter number of terms:"));
var result = fibonacci(n);
for(var i=0;i<result.length;i++){
 console.log("Term "+i+": "+ result[i]);
}
var sum=0;
for(var j=0;j<result.length;j++){
 sum+= result[j];
}
console.log("Sum: "+sum);
for(var i=0;i<2;i++){
  console.log("Loop "+i);
}
console.log("Fibonacci complete");
