n=int(input("enter the number of items"))
list=[]
for i in range(n):
    element=int(input("enter the element:"))
    list.append(element)
print(list)
sum=0
for i in list:
    sum=sum+i
print(sum)
