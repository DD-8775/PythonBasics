# --------    Dictionaries are ordered collection of data items .
# Dictionary items are key-value pair that are seperated by commas and enclosed within curly brackets{}.

info = {"name":"Shashwat singh", "age" : 19, "eligible" : True}               # age is key, 19 is value same for name and eligible .
print(info)

# ------------  Accessing Dictionary items ------------
# Accessing single values

print(info['name'])             # Value can be accessed either by square bracket. if key not found this raise an key error
print(info.get('age'))         # Or by get command . if key not found this will simply return none
 
# Accessing multiple values 

print(info.values())           # Prints all the values 

# -----------  Accessing keys -------

print(info.keys())

# ------------- Accessing key-value pairs --------

print(info.items())

# Other ways to access dict_

for i in info.values() :
    print(i)

for i in info.keys() :
    print(i)     

for key,value in info.items() :
    print(key, ":", value)


#---------- Dict_ methods -----------------

info.update({"hi":22, 'music':'yes'})    
d2 = {'money':'yes'}
info.update(d2)
print(info)


# info.clear()                 # Clears all items in dict and return {} empty dict
# print(info)

info.pop('hi')                 # The pop() method removes the key-value pair whose key is passed as a parameter
print(info)

info.popitem()                 # The popitem() method removes the last key-value pair from the dictionary.
print(info)


# we can also use del kayword to remove a dict item 

del info['music']
print(info)

# if no key is provided then whole dict will be deleted 

del info
# print(info)