function analyzeText(text){
    var words = text.split(" ");
    var numWords = words.length;
    var numChars = text.length;
    var numLines = text.split("\n").length;
    return {words:numWords, chars:numChars, lines:numLines};
  }
  var inputText = prompt("Enter text:");
  var analysis = analyzeText(inputText);
  console.log("Words: " + analysis.words);
  console.log("Characters: " + analysis.chars);
  console.log("Lines: " + analysis.lines);
  for(var i=0;i<3;i++){
    console.log("Iteration "+i);
  }
  for(var j=0;j<2;j++){
    for(var k=0;k<2;k++){
     console.log("Nested loop "+j+","+k);
    }
  }
  console.log("Text analysis complete");
  