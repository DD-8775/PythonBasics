# --------- Set is unoedered collection of data items . 
# As they are unordered so we can't change them
# Also sets don't contain duplicate items

# s = {1,2,2,3,4,5,6,7,"Dance"}    
# print(s)                        # As it's a set so the duplicate 2 will be rmoved from the result
# print(type(s))

# s_new = set()            #This is an empty set, {} can't be use as it is dictnory
# print(s_new)
# print(type(s_new))            

# s2 = {12.5 ,3 , 10, "dance", 55 , "funny", 9}         
# print(s2)                                     # As sets are unordered collection so result might be in different order 


# ---------     SET METHODS      ----------------------

cities1 = {"DELHI", "MUMBAI","CHENNAI","PUNE"}
cities2 = {"DELHI", "BALLIA", "CHAIBASA", "CHOPAN", "NASIK"}
print(cities1.union(cities2))               # Prints cities1 union cities2
cities1.update(cities2)                     # value of cities1 becomes cities1 union cities2
print (cities1)                             

print(cities1.intersection(cities2))         # prints intersection
cities2.intersection_update(cities1)         # makes cities2 = cities1 intersection cities2
print(cities2) 

print(cities1.symmetric_difference(cities2))  # Prints the items not similar in both sets

print(cities2.difference(cities1))            # Prints the items in cities2 that aren't in cities1

print(cities1.isdisjoint(cities2))            #  checks if items of given set are present in another set. This method returns "False" if items are present, else it returns "True".

print(cities1.issuperset(cities2))            #  checks if all the items of a cities2 set are present in the cities1 set. It returns True if all the items are present, else it returns False.

print(cities2.issubset(cities1))    

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}      #This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable
item = cities.pop()
print(cities)
print(item)

#cities.remove("j")     # The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error
cities.discard("j")

cities.clear()          # This method clears all items in the set and prints an empty set
print(cities)

cities.add("NOIDA")     #If you want to add a single item to the set use the add() method
print(cities)
 
del cities              # del is not a method, rather it is a keyword which deletes the set entirely.
#print(cities)            # raises erroe if we try to print the set as it is deleted completely

