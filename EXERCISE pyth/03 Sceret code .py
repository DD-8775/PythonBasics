word = input("Enter the word you want to code/decode : ")
user = input("Enter 'code' to code the word , and 'decode' to decode the word : ")
lst1 = word.split()
for word2 in lst1 :

 if user.lower() == 'code' :   
    if len(word2)<=2 :
        rev= word2[::-1]
        print('asd',rev,end="zxc ",sep='')

    else:
        r1 = word2[1:]
        w1 = word2[0]
        halfc = r1 + w1 
        print('asd',halfc,end="zxc ",sep='')

 elif user.lower() == 'decode' :
    dcd1 = word2[3:-3]

    if len(dcd1)<= 2 :
       rev2 = dcd1[::-1]
       print(rev2,end=' ')
    
    else :
       dcd2 = dcd1[-1] + dcd1[:-1]
       print(dcd2,end=' ')


 else :
    raise ValueError('Enter the correct word')

