#prompt the user for a list of integers.For all values greater than 100 store 'write over instead of that number'
limit=int(input("enter the limit:"))
list=[]
for i in range(limit):
       num=int(input("enter the number:"))
       if (num>100):
            list.append( 'over' )
       else:
               list.append(num)
print(list)
