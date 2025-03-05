function generateData(n){
    var data = [];
    for(var i=0;i<n;i++){
      data.push(Math.floor(Math.random()*100)+1);
    }
    return data;
  }
  function computeStats(data){
    var sum = 0;
    for(var i=0;i<data.length;i++){
      sum += data[i];
    }
    var avg = data.length > 0 ? sum/data.length : 0;
    var min = Math.min.apply(null, data);
    var max = Math.max.apply(null, data);
    return {sum: sum, average: avg, min: min, max: max};
  }
  function filterData(data, threshold){
    var filtered = [];
    for(var i=0;i<data.length;i++){
      if(data[i] > threshold){
        filtered.push(data[i]);
      }
    }
    return filtered;
  }
  var data = generateData(30);
  console.log("Data: " + data);
  var stats = computeStats(data);
  console.log("Sum: " + stats.sum);
  console.log("Average: " + stats.average);
  console.log("Min: " + stats.min);
  console.log("Max: " + stats.max);
  var filtered = filterData(data, 50);
  console.log("Filtered (>50): " + filtered);
  for(var i=0;i<5;i++){
    console.log("Loop "+i);
  }
  for(var j=0;j<3;j++){
    for(var k=0;k<4;k++){
      console.log("Nested loop "+j+","+k);
    }
  }
  console.log("Data analysis simulation complete");
  var x = 0;
  while(x<4){
    console.log("While loop iteration "+x);
    x++;
  }
  for(var a=0;a<3;a++){
    console.log("Extra loop "+a);
  }
  for(var b=0;b<3;b++){
    for(var c=0;c<3;c++){
      console.log("Double nested "+b+","+c);
    }
  }
  console.log("Extended analysis start");
  var extData = generateData(15);
  console.log("Extended Data: " + extData);
  var extStats = computeStats(extData);
  console.log("Extended Sum: " + extStats.sum);
  console.log("Extended Average: " + extStats.average);
  console.log("Extended Min: " + extStats.min);
  console.log("Extended Max: " + extStats.max);
  console.log("Extra analysis details:");
  for(var m=0;m<4;m++){
    for(var n=0;n<3;n++){
      console.log("Extra nested "+m+","+n);
    }
  }
  console.log("Extended analysis complete");
  for(var i=0;i<3;i++){
    for(var j=0;j<3;j++){
      console.log("Final nested "+i+","+j);
    }
  }
  console.log("Data analysis simulation end");
  for(var p=0;p<3;p++){
    console.log("Closing loop "+p);
  }
  console.log("Simulation finished");
  for(var t=0;t<2;t++){
    console.log("Last loop "+t);
  }
  console.log("Goodbye from Data Analysis Simulation");
  console.log("Final end");
  