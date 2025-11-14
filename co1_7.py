#enter two list of integer check whether the two list sum are same value or any value occur in both
n1=int (input("enter the limit:"))
list1=[]
for i in range(n1):
       num = int(input("enter number:"))
       list1.append(num)

n2 = int(input("enter the limit 2:"))
list2 = []
for i in range(n2):
       num = int(input("enter number:"))
       list2.append(num)
if len(list1) == len(list2):
               print("both list have same length:")
else:
               print("list have different length:")

if sum(list1) == sum(list2):
                 print("both list have same sum:")
else:
                 print("both have different sum :")
status=False
c=0
for j in list1:
       if j in list2:
              status=True
              c=c+1
     
if status==True:
       print("both list  have common value:",c,"VALUES")
else:
       print("both list  havenot   common value:")
       
               
        
