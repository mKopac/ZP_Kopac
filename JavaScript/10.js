function generateWeatherData(days){
    var data = [];
    for(var d=0; d<days; d++){
        var record = {};
        record.day = d+1;
        record.temp = Math.random()*45 - 10;
        record.humidity = Math.random()*80 + 20;
        record.wind = Math.random()*20;
        data.push(record);
    }
    return data;
    }
    function averageTemperature(data){
    var total = 0;
    for(var i=0; i<data.length; i++){
        total += data[i].temp;
    }
    return data.length > 0 ? total/data.length : 0;
    }
    function maxWind(data){
    var max = 0;
    for(var i=0; i<data.length; i++){
        if(data[i].wind > max){
        max = data[i].wind;
        }
    }
    return max;
    }
    function filterHotDays(data, threshold){
    var hot = [];
    for(var i=0; i<data.length; i++){
        if(data[i].temp > threshold){
        hot.push(data[i]);
        }
    }
    return hot;
    }
    function printWeatherData(data){
    for(var i=0;i<data.length;i++){
        console.log("Day "+data[i].day+", Temp: "+data[i].temp+", Humidity: "+data[i].humidity+", Wind: "+data[i].wind);
    }
    }
    var weather = generateWeatherData(15);
    console.log("Weather Data:");
    printWeatherData(weather);
    var avgTemp = averageTemperature(weather);
    console.log("Average Temperature: " + avgTemp);
    var maxWindSpeed = maxWind(weather);
    console.log("Maximum Wind Speed: " + maxWindSpeed);
    var hotDays = filterHotDays(weather, 25);
    console.log("Hot Days:");
    printWeatherData(hotDays);
    for(var i=0;i<3;i++){
    for(var j=0;j<2;j++){
        console.log("Nested loop "+i+","+j);
    }
    }
    var totalRecords = weather.length;
    console.log("Total records: " + totalRecords);
    var sumTemp = 0;
    for(var i=0;i<weather.length;i++){
    sumTemp += weather[i].temp;
    }
    var avgTemp2 = totalRecords > 0 ? sumTemp/totalRecords : 0;
    console.log("Calculated Average Temperature: " + avgTemp2);
    for(var a=0;a<2;a++){
    console.log("Extra loop "+a);
    }
    for(var b=0;b<2;b++){
    for(var c=0;c<2;c++){
        console.log("Double nested "+b+","+c);
    }
    }
    console.log("Additional analysis start");
    var tempList = [];
    for(var i=0;i<weather.length;i++){
    tempList.push(weather[i].temp);
    }
    console.log("Temperatures: " + tempList);
    var maxTemp = Math.max.apply(null, tempList);
    var minTemp = Math.min.apply(null, tempList);
    console.log("Max Temp: " + maxTemp);
    console.log("Min Temp: " + minTemp);
    var diff = maxTemp - minTemp;
    console.log("Temperature Difference: " + diff);
    for(var p=0;p<2;p++){
    console.log("Loop p "+p);
    }
    for(var q=0;q<2;q++){
    console.log("Loop q "+q);
    }
    for(var r=0;r<2;r++){
    for(var s=0;s<2;s++){
        console.log("Nested r,s "+r+","+s);
    }
    }
    console.log("Additional analysis complete");
    var finalSummary = {totalRecords: totalRecords, averageTemp: avgTemp2};
    console.log("Final summary: ", finalSummary);
    console.log("Simulation ends now");
    console.log("Goodbye");
    for(var i=0;i<2;i++){
    console.log("Final loop "+i);
    }
    console.log("End of Weather Data Analysis");
