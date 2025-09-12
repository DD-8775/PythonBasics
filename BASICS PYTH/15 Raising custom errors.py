# In python we can raise coustom errors by using 'raise' keyword .
 

salary = int(input("Enter your salary : "))
if not 2000<salary<100000 :
    raise ("Not a valid salary")
print('Your salary is', salary)



a = int(input("Enter any value between 5 and 9 : "))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")
 
