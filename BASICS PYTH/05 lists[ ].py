## Lists are ordered collection of data items , they store multiple values in a singles variables 
## It is mutable data-type so it can be changed after creation
 
lst1 = [False,1,2,3,4,"harry",True,0.213]
# print(lst1)
# print(type(lst1))
# print(len(lst1))
# print(lst1[0])                # Prints the valve in list at 0 index
# print(lst1[-3])               # Prints the value at len(lst1)-3 index i.e., at 5 index 

# if 0.213 in lst1 :            # Checks if the given item is present in list. It is done with the help of "in" keyword 
#     print("yes") 
# else:
#     print("no")



## We can also print range of list items : listName[ start : end : jumpindex] 

# lst1[1::2]                   # Prints items starting from index 1 till last and jumping to every next 2nd one


# lst2 = [2,4,5,6,8,9,10]
# lst3 = [i*i for i in lst2 if (i%2==0)]         # here i is the item in the list this will take all items from lst2 and check if its divisible with 2 if yes then square of that number will be added to lst3
# print(lst3)

# for x in lst3 :
#     print(x)                                 # This will print every items of lst3


##                             ----------- LIST METHODS-----------                 
                      
l = [13,11,21,1,4,3,6,8,10,11] 
# l.sort()                           # Sort the original list in accending order
# print(l)

# l.sort(reverse=True)               # Sort the original list in decending order
# print(l)

l.pop(0)                             # Removes the item from the list at the given index

# print(l.index(1))                  # prints the index of the first occurence of the given item

# print(l.count(11))                 # Returns the count of the number of times the given item repeted in the list

# new_l = l.copy()                   # Return the copy of the list, it is used to perform operation on the list without modifying the original one
# new_l[1] = 7                       # Changes the item at index 1 to 7
# print(new_l)

# l.append(1000)                   # Adds 1 item at the end of the list, if we try to append a list variable the it will add that list as single item     
# print(l)

# l.insert(0,100)                  # Adds 100 at 0 index 
# print(l)

# n=["hi",2020,"ok",True]
# l.extend(n)       # This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
 
# print(l+n)         # adds items of n at the last of l
print(l)



