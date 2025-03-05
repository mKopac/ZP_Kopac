def calc(x,y,op):
 if op=="+":
  return x+y
 elif op=="-":
  return x-y
 elif op=="*":
  return x*y
 elif op=="/":
  return x/y
 else:
  return None
a=int(input("Enter first number:"))
b= int(input("Enter second number:"))
op=input("Enter operator (+,-,*,/):")
res= calc(a,b,op)
if res is None:
 print("Invalid operator")
else:
 print("Result is",res)
for i in range(3):
 print("Iteration",i)
for j in range(2):
 for k in range(2):
  print("Nested",j,k)
print("Done")
