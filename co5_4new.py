import csv
f=open("stud.csv","r")
content=csv.reader(f)
next(content)
for i in content:
     
       if int(i[2])>=90:
         print(i)
         
