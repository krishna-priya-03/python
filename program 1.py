string1=input("enter a string:")
counts=dict()  
words =string1.split()
for i in words:     
    if i in counts:
        counts[i]+=1
    else:
        counts[i]=1
        
print(counts.items())

for k,v in counts.items():
    print(k,v)
