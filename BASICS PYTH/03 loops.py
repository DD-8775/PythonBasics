##                                   FOR LOOP

# a= ["red","green","blue","yellow","orange"]
# for colours in a:
#     print(colours)
#     for colour in colours:
#          print(colour)
#          if(colour == "o") :
#             print("NNNNIIIICCCCCEEEE")

# for i in range(3,31,3):
#     print(i)


 

   ##                                 WHILE LOOP

# x = 10
# while(x>0) :                       # it check condition for 1st value [here 10] ,if the contition is true the interpreter goes in while loop
#     print(x)                       # print function will be excuted printing 1st value [10]
#     x=x-1                          # then interpreter comes out of print and performs this code giving 'x' a new value [here 9] and again going to while and doing the same stated above 
# else:                              # when condition in while becomes false interpreter comes out of while and else statement is executed     
#     print("THAT'S the end")  



##                                  BREAK AND CONTINUE STATEMENTS

## BREAK: it is used to break out of the loop after the given condition is true
## FOR EX. WRITING A CODE TO PRINT THE TABLE OF 7 AND USING BREAK IN IT:
# for i in range(15):   
#     print((i+1)*7)
#     if(i==9):                  # IF THE 'if' condition would be above print then it would had not printed for i = 9 
#         break              # BREAK will break the function out of the for loop
# print("THAT'S THE TABLE OF 7 ")

# ## CONTINIUE: it just skips the loop for the given condition and causes the next iteration
# for i in range(10):
#     if(i==4):                    # continue just skips the rest of the code below it in that iteration.
#         continue                 # It does not affect the lines of code before it in that loop cycle.
#     print((i+1)*7)

# while True:                       # while true is a infinite loop (to stop code in vscode use ctrl+c)
#     print("hi")
   
# while True:
#     i = int(input("enter the number : "))
#     if i>100:
#         break
#     print(i)
      
 ## DO WHILE LOOP : it's a loop which execute set of instrustions atleast 1 time irrespective of the condition and then it checks if the condition is true or false
# a = int(input("enter the number "))
# print(a)
# while(a<100):
#     a = int(input("enter the number "))
#     print(a)

## USING BREAK AND CONTINIUE STATEMENT:
# while True:
#     n = int(input("ENTER THE NUMBER "))
#     print(n)
#     if(n>100):
#         break


            

