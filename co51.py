
file=open("lekshmi.txt","r")
content=file.readlines()
linelist=[]
for i in content:
       print(i)
       line=i.strip()
       linelist.append(line)
print(linelist)
file.close()
