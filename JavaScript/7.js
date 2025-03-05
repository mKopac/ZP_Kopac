function matrixMultiply(A,B){
    var m = A.length;
    var n = A[0].length;
    var p = B[0].length;
    var result = [];
    for(var i=0;i<m;i++){
      result[i]=[];
      for(var j=0;j<p;j++){
        result[i][j]=0;
        for(var k=0;k<n;k++){
           result[i][j]+= A[i][k]*B[k][j];
        }
      }
    }
    return result;
  }
  var A = [[1,2,3],[4,5,6]];
  var B = [[7,8],[9,10],[11,12]];
  var res = matrixMultiply(A,B);
  console.log("Matrix A:");
  for(var i=0;i<A.length;i++){
    var row="";
    for(var j=0;j<A[i].length;j++){
      row += A[i][j] + " ";
    }
    console.log(row);
  }
  console.log("Matrix B:");
  for(var i=0;i<B.length;i++){
    var row="";
    for(var j=0;j<B[i].length;j++){
      row += B[i][j] + " ";
    }
    console.log(row);
  }
  console.log("Result:");
  for(var i=0;i<res.length;i++){
    var row="";
    for(var j=0;j<res[i].length;j++){
      row += res[i][j] + " ";
    }
    console.log(row);
  }
  for(var i=0;i<2;i++){
    for(var j=0;j<2;j++){
      console.log("Loop "+i+","+j);
    }
  }
  var x=0;
  while(x<3){
    console.log("While loop "+x);
    x++;
  }
  console.log("Matrix multiplication complete");
  