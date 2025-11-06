#display future leap years from current year to fianl year
from datetime import date
current=date.today().year
final=int(input("enter the final year:"))
for i in range (current ,final +1):
  
       if(i%4==0 and i%100!=0 or i%400==0):
              print(i)
      
