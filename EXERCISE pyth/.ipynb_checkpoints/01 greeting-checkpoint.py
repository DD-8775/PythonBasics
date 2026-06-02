import time as t
# a=t.strftime("%H:%M:%S") the value of a will be string that's why we are using int() fcn
tym = int( t.strftime("%H"))
if(tym>5 and tym<12):
    print("GOOD MORNING SIR THE TIME IS ",end="")
elif(tym>=12 and tym<=15):
    print("GOOD AFTERNOON SIR THE TIME IS ",end="")
else :
    print("GOOD EVENING SIR THE TIME IS ",end="")        
timestamp = t.strftime("%H:%M:%S")
print(timestamp)

# t.strftime("%H") tells hour , similarly "%M" tells minutes and "%S" tells seconds 