''' For multiple cursor use left ALT '''
##               PRINT FCN                                           --------------------------------------------------------------------------------
print(7)                  # pyhton treat it as integer
print("hello world ")     # python treat it as string as ("") is present
print(3.14)               # python will treat it as floating  point number
'''
we can 
use 3 single/double quote   # use alt + down arrow key to move the line on which coursor is , to down
also to comment line
'''
print("hey \nhow are you")  # \n is use to print in new line and no need of giving space after \n unless required
print("hey what's up",7,2.4, sep= " ~ ")    # sep="" is seperator and used to seperate multiple items within print, by default space is sep.
print("hey",1,2,3,end="200\n" )    # end="" is used to specify what to print in the end and by using \n is end it will print the next operation in the nest line . Default is \n
print(7)


#            VARIABLES AND DATA TYPES                                         --------------------------------------------------------------------------------

# VARIABLES : they store data for ex. a = 10 or b = "hello"
# DATA TYPE : it is different types of value a variable holds like string, integers, boolen etc.

a = 1.202
print(type(a))          # type() is used to print the type of data type
print(complex(2,5))     # complex(a,b) is used to define complex data type of a+bj form
b= True                 # this is a boolean data type (it consits of values TRUE or FALSE)
print(type(b))
list=[1,2.3,[-1,complex(1,2)],"hi","how are you"]   # list: it is an ordered collection of data with each elements seperated by comma and enclosed within square braket. It is an mutable datatype.
# print(list)
# tuple = (("parrot", "sparrow"), ("Lion", "Tiger"))  # tuple: it is an ordered collection of data with elements seperated by comma and enclosed within parentheses. They are immutable datatypes.
# print(tuple)

''' OPERATORS : [* : MULTIPLY] , [/ : DIVIDE] , [// : ONLY PRINT THE INTEGER VALUE NOT THE DECIMAL] , [% : PRINTS REMIANDER]  , [** : PRINTS EXPONENTIAL] , [+= : a += 3 is same as , a = a+3]'''
# TYPECASTING : Conversion of one datatype to other data type is called typecasting in python. {str() , float() , int() , set() , dict() etc.}
a = input()            # python will treat input as a string
print(a)


##                          STRINGS                                      ----------------------------------------------------------------------------

# It is a secquence or array of textual data . In python , anything enclosed in "" or ' is considered as string
name = "shashwat"
print(name[0])           # this is indexing, square brackets are used to access the elements of string. In python indexing start from 0 , here it will print s .
print(name[3])           # here the output is a . 

para = '''Hi how are you
I'm fine thank you 
how are you doing?
I'm doing good , thanks for asking . '''       # ''' or """ is used to print multiline string
print(para)
for i in para :            # this is used to print every charater in the string
    print(i)
print(name,"is a",len(name), "letter word")       # len() is used to print length of a string 
# print(name[:5])            # this can be also written to print(name[0:5]) , it will print first 5 charaters of string, i.e, from index 0 to 5-1 = 4
# print(name[3:8])           # this will print charater fron index 3 to 8-1
# print(name[-6:-2])           # this means print(name[len(name)-6 : len(name)-2]) i.e, print(name[2:6]) , so it will print charater from index 2 to 5
# print(name[-3:-6])           # this will not print anything as [5:2] doesn't make any scense

''' # Strings are immutable that means we can't do any changes in it , for example: if we try to modify a charater at a specific index it raise  a TypeError indicating that the 'str' object does not support item assignment. The only way to change it is by creating a new string .
# This also means that operations like sclicing or reassembling parts of a string cerats a new string . '''

# a = " Coding is>good > "
# print(len(a))                  # starts from 0 and count total no. of item present 
# print(a.upper())               # converets a string to uppercase
# print(a.lower())               # converets a string to llower case 
# print(a.split())               # it is used to converet string to list 
# print(a.rstrip(">"))           # remove the specific charater from the end of the string
# print(a.strip)                 # removes any whitespaces before and after the string

# str1 = "hi my name is shashwat"
# print(str1.replace('hi','Hello'))   # replace the occurences pf a string with other string . [CASE OF STRING MATTERS]

# b = "hi I am a bOY"
# print(b.capitalize())             # turns 1st charster of a string to upper case and rest to lower
# print(b.center(50))               # aligns the string to center as per the parameters given by the user; here its 50 so it makes total lenght of the string 50 i.e., for increasing the length it added spaces before string  
# print(b.center(50,"$"))           # insted of spaces it will print the padding charater provided 
# print(b.count("a"))               # counts the number of times the given value occured in the given string
# print(b.title())                  # capitalizes first letter of each word

c = "hi how are you?"
print(c.endswith("?"))             # checks if string ends with the given and returns true or false. [spaces also matters]
print(c.index("ar"))               # tells the index of the first occurence of the given value , if not present it return an exception
print(c.find("ar"))                # tells the index of the first occurence of the given value , if not present it return -1 
