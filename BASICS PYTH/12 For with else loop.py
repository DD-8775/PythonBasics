# Along with if , we can also use else with 'for' and 'while' loop . 

for i in range(5):
    print(i)
    if i == 4:
        break              # As we have used break the loop will br breaked as soon as the condition is met , so else will not be executed 
else :
    print("Over")          # if break is removed from above it will print over at last 



for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")