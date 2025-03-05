function calc(a,b,op){
    if(op==="+"){
     return a+b;
    } else if(op==="-" ){
    return a-b;
    } else if(op==="*"){
      return a*b;
    } else if(op==="/"){return a/b;
    } else { return NaN; }
  }
  var a= parseFloat(prompt("Enter first number:"));
  var b= parseFloat(prompt("Enter second number:"));
  var op= prompt("Enter operator (+,-,*,/):");
  var result= calc(a,b,op);
  if(isNaN(result)){
    console.log("Invalid operator");
  }else { console.log("Result is "+ result); }
  for(var i=0;i<3;i++){
  console.log("Iteration "+i);
  }
  for(var j=0;j<2;j++){
    for(var k=0;k<2;k++){
    console.log("Nested "+j+","+k);
  }
  }
  console.log("Done");
  