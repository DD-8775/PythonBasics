# ------   f-string is used for string formatting 

a = int(input("ENTER THE NUM "))
print(f"THE DOUBLE OF THE NUMBER IS {a+a}")
print(f"THE DOUBLE OF THE NUMBER IS {{a+a}}")           # {{}} the value inside will be treated as string and wil be printed as it is .

price = 219.019992
print(f"The payable price is {price:.2f}")               # {price:.2f} this will print the value of price upto 2 decimal place because of .2f , f here is float


#   --------------------      Earlier string formatting was done with the help of fromat method 
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

print("{1} is better than {0}".format("lilly","jane"))