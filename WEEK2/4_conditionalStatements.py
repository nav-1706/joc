print("We are learnig conditional statements in Python");

num1 = int(input("Enter a number between 1 to 5: "));

if(num1 == 1): # indentation is important in python 
    print("You have entered number 1");

elif(num1 == 2):
    print("You have entered number 2");

elif(num1 == 3): print("You have entered number 3");
    
elif(num1 == 4):
    print("You have entered number 4");

elif(num1 == 5):
    print("You have entered number 5");
    
else:
    print("Only number from 1 to 5 is allowed")
