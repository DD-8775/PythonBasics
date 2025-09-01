## Tuples are ordered collection of data items like lists they also store multiple items in a single variable
## They are immutable i.e., they can't be changed after creation

tup = (1, 2, 32,76, 342, 32, "green", True)
# tup[0] = 90                        # will print error as tuples can't be changed
# print(type(tup), tup)
# print(len(tup))
# print(tup[0])
# print(tup[-1])
# print(tup[2])
# # print(tup[34])

# if  3421 in tup:
#   print("Yes 342 is present in this tuple")
# else:
#   print("not in tuple")
    
# tup2 = tup[1:4]
# print(tup2)



## AS TUPLES ARE IMMUTABLE SO WE CAN'T CHANGE THEM DIRECTLY
## SO TO DO MODIFICATIONS IN IT WE CHANGE IT TO LIST FIRST, AND THEN WE CAN DO CHANGES TO IT AND AGAIN CONVERET BACK TO TUPLES ONCE THE CHANGES ARE COMPLETED

change1= list(tup)                         # This changes "tup" Tuples to list type
change1.pop(3)                             # Removes the item at the given index
change1.append(100)
tup = tuple(change1)                       # This changes back the list to tuple
print(tup)

print(tup.index("green"))
print(tup.index(32,3,6))                   # tuple.index(element, start, end) tells the first occurence of element only from start to end-1 

