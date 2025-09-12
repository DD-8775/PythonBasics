# It is a process of responding to unwanted or unexpected events when a computer program runs.
# Exception handling deals with these to avoid the program to crash.

# Pyhton has many build-in exceptions that are raised when program encounters an error.
# When these exception occour, the python interpreter stops the current process and passes it to the calling processes untill it is handled . If not handled , the program will crash.

# To overcome this we use try and except block .
# The code code runs normally in try box when there is no error.
# If error is dected then except block is executed.


try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:                              # This is a named except clause ,i.e, this except block will only be executed if there is a value error
    print("Number entered is not an integer.")
    
except MemoryError:                             # This except block will only be executed if there is a memory error 
   print("it's a memory error")
    
except IndexError:                             # This except block is only executed if there is a index error
  print("Index Error")

# We can use multiple named except clause to print the specific things when that particular type of error is occured.

# But for catch all except clause we will have to use single except clause.

try:
   value = int(input("Enter the price : "))
   print(f"Thanks for shopping! Your total price is : {value}")
except:                                 # Here for every type of error only this will be executed
   print("Some error occured!!...")   