function bubbleSort(arr){
    var n = arr.length;
    for(var i=0;i<n;i++){
     for(var j=0;j<n-i-1;j++){
      if(arr[j] > arr[j+1]){
       var temp = arr[j];
       arr[j]= arr[j+1];
       arr[j+1]= temp;
      }
     }
    }
    return arr;
  }
  var array = [64,34,25,12,22,11,90,88,76,55];
  var sorted = bubbleSort(array);
  console.log("Sorted array:");
  for(var i=0;i<sorted.length;i++){
   console.log(sorted[i]);
  }
  for(var i=0;i<2;i++){
   console.log("Loop "+i);
  }
  for(var a=0;a<2;a++){
   for(var b=0;b<2;b++){
    console.log("Nested "+a+","+b);
   }
  }
  console.log("Bubble Sort complete");
  