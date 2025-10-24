#total number of characters in a string
str=input("enter the string")
dict={}
for i in str:
       if i in dict:
              dict[i]+=1
       else:
              dict[i]=1
print (dict)
for k,v in dict.items():
       print(k,"-",v)
            
            
