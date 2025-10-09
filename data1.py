import csv
file=open("data.csv","r")
content=csv.reader(file)
f=int(input("enter the number:"))
for i in content:
      print(i[f])
