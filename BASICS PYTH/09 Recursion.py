# ------- Calling a function in itshelf is called resursion 

def factorial(n):
    if n==0 or n ==1 :
        return 1
    else:
        return n*factorial(n-1)                  # Here we are calling the function inside itself

print(factorial(5))        

# ------  This is how it is executed
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1


# ---------    Fibonacci sequence 
# To print x'th fibonacci number

def fibonacci(x):
    if x == 0 :
        return 0
    elif x == 1 :
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
print(fibonacci(10))    