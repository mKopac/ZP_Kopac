def analyze_text(text):
 words=text.split()
 num_words=len(words)
 num_chars=len(text)
 num_lines=text.count("\n")+1
 return num_words,num_chars,num_lines
text=input("Enter text:")
result=analyze_text(text)
print("Words:",result[0])
print("Characters:",result[1])
print("Lines:",result[2])
for i in range(2):
 print("Iteration",i)
for j in range(3):
 print("Loop",j)
s=text.upper()
t=text.lower()
u=text.title()
print("Uppercase:",s)
print("Lowercase:",t)
print("Titlecase:",u)
for k in range(2):
 for l in range(2):
  print("Nested",k,l)
print("Analysis complete")
