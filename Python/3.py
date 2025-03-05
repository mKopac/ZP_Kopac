def bubble_sort(arr):
 n=len(arr)
 for i in range(n):
  for j in range(0,n-i-1):
   if arr[j]>arr[j+1]:
    arr[j],arr[j+1]=arr[j+1],arr[j]
 return arr
arr=[64,34,25,12,22,11,90,88,76,55]
sorted_arr=bubble_sort(arr)
print("Sorted array:")
for num in sorted_arr:
 print(num)
for i in range(3):
 print("Loop",i)
for a in range(2):
 for b in range(2):
  print("Double loop",a,b)
print("Bubble sort complete")
for x in range(2):
 print("Extra loop",x)
for y in range(2):
 print("Another loop",y)
print("End of program")
for z in range(1):
 print("Final loop",z)
