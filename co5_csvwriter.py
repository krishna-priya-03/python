import csv
f=open("stud1.csv","w",newline="")
content=csv.writer(f)
for i in range(3):
       name=input("enter the name")
       age=int(input("enter the age"))
       mark=float(input("enter the mark"))
       l=[name,age,mark]
       content.writerow(l)
f.close()       
f1=open("stud1.csv","r")
content=csv.reader(f1)
next(content)
for i in content:
       print(i)
