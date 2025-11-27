import csv
#input dictionary using user input method
data={ }
n=int(input("enter the limit"))
for i in range(n):
       key=input("enter the key")
       val=input("enter the value")
       data[key]=val
       

#csv writing
f=open("dictdata1.csv","w", newline='')
content=csv.writer(f)
content.writerow(data.keys())
content.writerow(data.values())
f.close()
