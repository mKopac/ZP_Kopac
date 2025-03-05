def matrix_multiply(A,B):
 m=len(A)
 n=len(A[0])
 p=len(B[0])
 result=[[0 for j in range(p)] for i in range(m)]
 for i in range(m):
  for j in range(p):
   for k in range(n):
    result[i][j]+=A[i][k]*B[k][j]
 return result
A=[[1,2,3],[4,5,6]]
B=[[7,8],[9,10],[11,12]]
res=matrix_multiply(A,B)
print("Matrix A:")
for row in A:
 print(row)
print("Matrix B:")
for row in B:
 print(row)
print("Result:")
for row in res:
 print(row)
for i in range(2):
 for j in range(2):
  print("Loop",i,j)
x=0
while x<3:
 print("While loop",x)
 x+=1
for i in range(2):
 print("Extra loop",i)
print("Bubble sort complete")
for z in range(1):
 print("Final loop",z)
