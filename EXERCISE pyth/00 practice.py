# term = int(input("Enter the no of terms in the list: "))
# a = []
# for i in range (term):
#     value = int(input("Enter the value: "))

#     a.append(value)

# print(a)

a="abcdefghijklmnopqrstuvwxyz"
v = "aeiou"
l=[]
for i in a:
    for j in v:
        if i == j:
            l.append(i)
for k in l:
    print(k,end=",")