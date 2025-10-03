# lst1 = [False,1,2,3,4,"harry",True,0.213]
# l = ["shashwat"]
# l.append(lst1)
# print(l)

# num = int(input("enter number : "))
# a = 1
# for i in range(1,num +1) :
#     a = a * i
#     print(a)

# a = {12,"ram", 6,1.1,0}
# b = {4,10,1.001,88,12}    
# print(a.isdisjoint(b))
# c=b.pop()
# print(c)
# print(b)



# a= 'ho mo go'
# b=a.split()
# print(b)

# for i in b :
#     if len(i) <= 2 :
#       print(i[::-1])


# name = 'shahswat'
# print(name[2:])      
# print(name[:2:-1])
# print(name[:-1])
# # print("hey",1,2,3,end="200\n" )   

h = int(input("enter the hight of triangle: "))
for i in range(1,h+1):
    print(" "*(h-i),"*"*(2*i-1),sep='')


n = int(input("Enter the number of rows: "))
for i in range(1, n + 1): 
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()   