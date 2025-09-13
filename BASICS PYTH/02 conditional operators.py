
## Conditional operators :  > , < , >= , <= , == , !=

##                           if() - else() STATEMENT:

# a = int(input("ENTER YOUR AGE : "))
# if(a>=18) :                            # if condition inside if is true then if is executed else, else is executed
#     print("YOU ARE AN ADULT")
# else:
#     print("YOU ARE A MINOR")    



##                            ELIF STATEMENT :
## As else is the final block in a sequence of if-elif-else conditions, once else block is reached there is no more conditions to check , so that's why elif is always comes after if and before else.

# a = int(input("ENTER YOUR AGE : "))
# if(a>18) :                              # AFTER COLON IF WE PRESS ENTER WE ENTER INSIDE IF 
#     print("YOU ARE AN ADULT")           # THE SPACE BEFORE PRINT HERE IS CALLED INDENTATION IT TELLS INTERPRETER THAT A GROUP OF STATEMENT BELONG TO A SPECIFIC BLOCK , HERE if .
# elif(13 < a < 18) :
#     print("YOU ARE A TEEN")  
# elif(a == 18) :
#     print("YOU ARE SPECIAL")      
# else:
#     print("YOU ARE A MINOR")
# if(a==1) :
#     print("special child")   



##                       NESTED IF-ELIF-ELSE STATEMENT :

# a = int(input("ENTER YOUR AGE : "))
# if(a>0 and a < 5) :                # we can't do if a == 1 or 5 as pyhton will only check for 1 and for 5 , as its boolean value is always true(5 is non empty) so else will never be executed. 
#     print("You are a toddler")
# elif(a>=5 and a<18 ):
#     if(a<14):
#         print("You are a child")
#     else :
#         print("You are a teen")
# elif(a>=18):
#     print("You are a adult")
# else :
#     print ("ENTER A VALID AGE")            



##                      MATCH CASE STATEMENTS :

## it compares a given variable  values to different shapes, also referred to as the patterns. It keeps on comparing the variable with all present patterns untill fits into one.
## it can be used as an alternative to using many 'elif' statement

x = int(input("ENTR THE NUMBER : "))
match x :                   # x is the variable to match
    case 0 :                # it can also be written as , if(x == 0):
        print(x,"zero")
    case 10 :
        print(x,"TEN")
        print("its a positive number") 
## case with if-condition
    case _ if x>0:
        print("its a positive number") 
    case _:                   # this is eqivalant to 'else' condition if none of the above condition is satisfied then the code inside it will be executed
        print("ENTER A VALID NUMBER")               







