# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.

ques = ["QUES 1 : What is the capital of India ?","QUES 2 : How many bones does human body have ?","QUES 3 : How many colours does rainbow have ?","QUES 4 : Which is the largest state of India ?","QUES 5 : Which is the largest animal in the world ?"]
opt1 = ["1. Mumbai", "2. Delhi","3. Chennai","4. Lucknow"]
opt2 = ["1. 204","2. 205","3. 206","4. 207"]
opt3 = ["1. 8","2. 10","3. 9","4. 7"]
opt4 = ["1. Rajasthan","2. Uttar Pradesh","3. Madhya Pradesh","4. Maharastra"]
opt5 = ["1. Elephant","2. Giraffe","3. Blue Whale","4. Bull"]


print(ques[0])
print("YOUR OPTIONS ARE :")
for i in opt1:
    print(i)
ans1 = int(input("ENTER YOU ANSWER : "))
if(ans1 == 2):
    money= 10000
    print("CORRECT ANSWER , YOU WON",money,"RUPEES")    
else :
    print("SORRY YOUR ANSWER IS INCORRECT/INVALID, PLEASE TRY AGAIN")
    money = 0
    print("QUIZ IS COMPLETED YOU WON :",money,"RUPEES")
    exit()


print(ques[1])
print("YOUR OPTIONS ARE :")
for j in opt2:
    print(j)
ans2 = int(input("ENTER YOU ANSWER : "))
if(ans2 == 3):
    money= 100000
    print("CORRECT ANSWER , YOU WON",money,"RUPEES")    
else :
    print("SORRY YOUR ANSWER IS INCORRECT/INVALID, PLEASE TRY AGAIN")
    money = 0
    print("QUIZ IS COMPLETED YOU WON :",money,"RUPEES")
    exit()


print(ques[2])
print("YOUR OPTIONS ARE :")
for k in opt3:
    print(k)
ans3 = int(input("ENTER YOU ANSWER : "))
if(ans3 == 4):
    money= 1000000
    print("CORRECT ANSWER , YOU WON",money,"RUPEES")    
else :
    print("SORRY YOUR ANSWER IS INCORRECT/INVALID, PLEASE TRY AGAIN")
    money = 0
    print("QUIZ IS COMPLETED YOU WON :",money,"RUPEES")
    exit()


print(ques[3])
print("YOUR OPTIONS ARE :")
for l in opt4:
    print(l)
ans4 = int(input("ENTER YOU ANSWER : "))
if(ans4 == 1):
    money= 10000000
    print("CORRECT ANSWER , YOU WON",money,"RUPEES")    
else :
    print("SORRY YOUR ANSWER IS INCORRECT/INVALID, PLEASE TRY AGAIN") 
    money = 0
    print("QUIZ IS COMPLETED YOU WON :",money,"RUPEES")
    exit()   


print(ques[4])
print("YOUR OPTIONS ARE :")
for m in opt5:
    print(m)
ans5 = int(input("ENTER YOU ANSWER : "))
if(ans5 == 3):
    money= 100000000
    print("CORRECT ANSWER , YOU WON",money,"RUPEES")    
else :
    print("SORRY YOUR ANSWER IS INCORRECT/INVALID, PLEASE TRY AGAIN")  
    money = 0 
    print("QUIZ IS COMPLETED YOU WON :",money,"RUPEES") 
    exit()

print("QUIZ IS COMPLETED YOU WON :",money,"RUPEES")    