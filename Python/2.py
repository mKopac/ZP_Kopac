def fib(n):
 if n<=0:
  return []
 elif n==1:
  return [0]
 else:
  seq=[0,1]
  for i in range(2,n):
   seq.append(seq[i-1]+seq[i-2])
  return seq
n=int(input("Enter n:"))
seq=fib(n)
for i in range(len(seq)):
 print("Fibonacci number",i,":",seq[i])
sumFib=0
for num in seq:
 sumFib += num
print("Sum:",sumFib)
for i in range(2):
 print("Extra loop",i)
print("Program finished")
