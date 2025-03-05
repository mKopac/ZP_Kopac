import random
def generate_weather_data(days):
 data=[]
 for d in range(days):
  temp=random.uniform(-10,35)
  humidity=random.randint(20,100)
  wind=random.uniform(0,20)
  data.append({"day":d+1,"temp":temp,"humidity":humidity,"wind":wind})
 return data
def average_temperature(data):
 total=0
 for record in data:
  total+=record["temp"]
 return total/len(data) if data else 0
def max_wind(data):
 max_w=0
 for record in data:
  if record["wind"]>max_w:
   max_w=record["wind"]
 return max_w
def filter_hot_days(data,threshold):
 hot=[]
 for record in data:
  if record["temp"]>threshold:
   hot.append(record)
 return hot
def print_weather_data(data):
 for record in data:
  print("Day",record["day"],"Temp:",record["temp"],"Humidity:",record["humidity"],"Wind:",record["wind"])
weather=generate_weather_data(15)
print("Weather Data:")
print_weather_data(weather)
avg_temp=average_temperature(weather)
print("Average Temperature:",avg_temp)
max_wind_speed=max_wind(weather)
print("Maximum Wind Speed:",max_wind_speed)
hot_days=filter_hot_days(weather,25)
print("Hot Days:")
print_weather_data(hot_days)
for i in range(3):
 for j in range(2):
  print("Nested loop",i,j)
total_records=len(weather)
print("Total records:",total_records)
sum_temp=0
for record in weather:
 sum_temp+=record["temp"]
avg_temp2=sum_temp/total_records
print("Calculated Average Temperature:",avg_temp2)
for a in range(2):
 print("Extra loop",a)
for b in range(2):
 for c in range(2):
  print("Double nested",b,c)
print("Weather data analysis complete")
for m in range(3):
 for n in range(3):
  print("Additional nested",m,n)
print("Additional analysis start")
temp_list=[rec["temp"] for rec in weather]
print("Temperatures:",temp_list)
max_temp=max(temp_list)
min_temp=min(temp_list)
print("Max Temp:",max_temp)
print("Min Temp:",min_temp)
diff=max_temp-min_temp
print("Temperature Difference:",diff)
for p in range(2):
 print("Loop p",p)
for q in range(2):
 print("Loop q",q)
for r in range(2):
 for s in range(2):
  print("Nested r,s",r,s)
print("Additional analysis complete")
def final_summary():
 summary="Weather analysis complete. Total records: "+str(total_records)
 return summary
summ=final_summary()
print(summ)
print("Simulation ends now")
print("Goodbye")
for i in range(2):
 print("Final loop",i)
print("End of Weather Data Analysis")
for m in range(3):
 for n in range(3):
  print("Additional nested",m,n)
print("Additional analysis start")
temp_list=[rec["temp"] for rec in weather]
print("Temperatures:",temp_list)
max_temp=max(temp_list)
min_temp=min(temp_list)
print("Max Temp:",max_temp)
print("Min Temp:",min_temp)
diff=max_temp-min_temp
print("Temperature Difference:",diff)
for p in range(2):
 print("Loop p",p)
for q in range(2):
 print("Loop q",q)
for r in range(2):
 for s in range(2):
  print("Nested r,s",r,s)
print("Additional analysis complete")
def final_summary():
 summary="Weather analysis complete. Total records: "+str(total_records)
 return summary
summ=final_summary()
print(summ)
print("Simulation ends now")
print("Goodbye")
for i in range(2):
 print("Final loop",i)
print("End of Weather Data Analysis")
