f= open('BASICS PYTH/myfile.txt','r')  # Before performing any action we must open the file by using open() function 
# open("Path of the file to be opend","mode in which we want to open the file")
# here 'r' is the default mode in which we have opened the file. IT means we have opened the file the file in read mode. Since 'r' is the default mode its not necessary to write it in open() function, we can simply write f = open('path')

print(f) # f is not the contents of the file. It is a file object, which represents an open connection to the file.
# this will print the type of file, path of the file , mode in which the file is opend and text encoding used by python to read the file.

t= f.read() # reads the content in the file 
print(t)   # prints the content in the file 
f.close()  # closes the file

# we can aslo do this by a better apporach , which is by using "with" statement

#with creates a managed block where a resource is acquired at the beginning and automatically cleaned up at the end, even if an exception occurs.

with open('BASICS PYTH/myfile.txt','r') as f :
    print(f.read())
# here we dont need to close the file manually, with does that for us even when any error occurs.