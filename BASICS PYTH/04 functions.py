## FUNCTION : IT IS A BLOCK OF CODE WHICH PERFOMES A SPECIFIC TASK WHENEVER IT IS CALLED
## BUILT-IN FUNCTION : THESE FUNCTIONS ARE PRECODED IN PYTHON, EX. len(), range(), type() etc.
## USER-DEFINED FUNCTIONS : THESE AR ETHE FUNCTIONS THAT USER DEFINES AS PER THEIR NEED.

# def greaterthan(a,b):                  # we defined a function named greaterthan
#     if(a>b):
#         print(a,"is greater than",b)
#     else:
#         print(b,"is greater than",a)

# greaterthan(1000,-1.1)

# def test_01(a,b):
#     pass                            # pass statement wil not do anything and the code will move foward , it is used so that no error is displayed while excueting programme and we can write code in future


def avg(a,b,c):
    return (a+b+c)/3                 # return statement returns the value of the function to a variable [here average] , whereas print just print the value when function is called for a specific argument

average = avg(12,23,43)
print(average)                       # if insted of return we write this code with print statement i would not return the value of fcn to variable, so the output would be "none " in that case
