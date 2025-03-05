import random
def fetch_url(url):
 return "Content of "+url
def parse_content(content):
 words=content.split()
 return len(words)
urls=["http://site1.com","http://site2.com","http://site3.com","http://site4.com"]
results=[]
for url in urls:
 c=fetch_url(url)
 w=parse_content(c)
 results.append((url,w))
print("Scraping results:")
for r in results:
 print(r)
sum_words=0
for r in results:
 sum_words+=r[1]
avg_words=sum_words/len(results)
print("Average word count:",avg_words)
for i in range(3):
 for j in range(3):
  print("Loop",i,j)
x=random.randint(1,10)
y=random.randint(1,10)
print("Random numbers:",x,y)
if x>y:
 print("x is greater")
elif x<y:
 print("y is greater")
else:
 print("x equals y")
for k in range(2):
 print("Extra loop",k)
for m in range(2):
 for n in range(2):
  print("Nested loop",m,n)
print("Web scraping simulation complete")
def additional_operation(a,b):
 if a>b:
  return a-b
 else:
  return b-a
res=additional_operation(x,y)
print("Additional operation result:",res)
for p in range(2):
 print("Final loop",p)
print("Program finished")
print("Extra final message")
print("End of simulation")
