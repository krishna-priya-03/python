vowels ="a,e,i,o,u, A,E,I,O,U"
w =input("enter the word:")
print("vowels present in the word are:")
for i in w:
    if i in vowels:
        print(i)