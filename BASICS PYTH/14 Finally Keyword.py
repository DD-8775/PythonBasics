def is_integer():
 try :
    a = int(input("ENTER THE INTEGER : "))
 except:                                      # if any error is occured then except is executed 
    print( 'That is not a valid integer')
    return 0 
 else :                                        # if no error is occured then else is executed
    print(a,'is accepted as an integer')
    return 1
 finally :                                    # finally is always executed 
    print("THE END")  

 print('THE END BY PRINT')      

x = is_integer()
print(x)

# As we are using return the fcn will be returned at the given condition and further the code will not be executed. But as we are using finally keyword the code inside finally will be executed event after using return.
