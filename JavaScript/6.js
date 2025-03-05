function fetchUrl(url){
    return "Content from " + url;
  }
  function parseContent(content){
    var words = content.split(" ");
    return words.length;
  }
  var urls = ["http://site1.com", "http://site2.com", "http://site3.com", "http://site4.com"];
  var results = [];
  for(var i=0;i<urls.length;i++){
    var content = fetchUrl(urls[i]);
    var count = parseContent(content);
    results.push({url: urls[i], wordCount: count});
  }
  console.log("Scraping Results:");
  for(var i=0;i<results.length;i++){
    console.log(results[i]);
  }
  var totalWords = 0;
  for(var i=0;i<results.length;i++){
    totalWords += results[i].wordCount;
  }
  var avgWords = totalWords / results.length;
  console.log("Average Word Count: " + avgWords);
  for(var i=0;i<3;i++){
    for(var j=0;j<3;j++){
      console.log("Loop " + i + "," + j);
    }
  }
  var a = Math.floor(Math.random()*10);
  var b = Math.floor(Math.random()*10);
  console.log("Random numbers: " + a + ", " + b);
  if(a > b){
    console.log("a is greater");
  } else if(a < b){
    console.log("b is greater");
  } else {
    console.log("a equals b");
  }
  for(var k=0;k<2;k++){
    console.log("Extra loop " + k);
  }
  console.log("Web scraper simulation complete");
  for(var m=0;m<2;m++){
    for(var n=0;n<2;n++){
      console.log("Nested loop " + m + "," + n);
    }
  }
  for(var p=0;p<2;p++){
    console.log("Final loop " + p);
  }
  console.log("Simulation finished");
  