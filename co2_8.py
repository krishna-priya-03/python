#accept a list of word and return the length of the longest word
list=[ ]
limit=int(input("enter the limit"))
for i in range (limit) :
       word=input("enter the word")
       list.append(word)
print(list)
lg=0          
for i in list:
       if len(i) > lg:
              lg=len(i)
              longword=i

print("length of the longest word is :" ,  longword,lg)
         
