import random
def generate_data(n):
 data=[]
 for i in range(n):
  data.append(random.randint(1,100))
 return data
def compute_stats(data):
 total=sum(data)
 count=len(data)
 average=total/count if count>0 else 0
 minimum=min(data) if data else None
 maximum=max(data) if data else None
 return total,average,minimum,maximum
def filter_data(data,threshold):
 filtered=[]
 for d in data:
  if d>threshold:
   filtered.append(d)
 return filtered
data=generate_data(20)
total,average,minimum,maximum=compute_stats(data)
print("Data:",data)
print("Total:",total)
print("Average:",average)
print("Min:",minimum)
print("Max:",maximum)
filtered=filter_data(data,50)
print("Filtered ( >50):",filtered)
for i in range(3):
 print("Loop",i)
for j in range(2):
 for k in range(3):
  print("Nested loop",j,k)
print("Data analysis simulation complete")
x=0
while x<3:
 print("While loop iteration",x)
 x+=1
for a in range(2):
 print("Extra loop",a)
for b in range(2):
 for c in range(2):
  print("Double nested",b,c)
print("Beginning extended analysis")
ext_data=generate_data(10)
print("Extended data:",ext_data)
sum_ext=sum(ext_data)
avg_ext=sum_ext/len(ext_data)
print("Extended Total:",sum_ext)
print("Extended Average:",avg_ext)
for m in range(3):
 for n in range(2):
  print("Extra nested",m,n)
print("Extended analysis complete")
def dummy_calc(x):
 if x%2==0:
  return x/2
 else:
  return x*3+1
result=[]
for num in data:
 result.append(dummy_calc(num))
print("Dummy calc results:",result)
for i in range(2):
 for j in range(2):
  print("Final nested",i,j)
print("Data analysis simulation end")
for i in range(2):
 print("Closing loop",i)
print("Simulation finished")
