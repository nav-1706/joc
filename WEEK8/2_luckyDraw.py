import random
import matplotlib.pylab as plt

balance = 0
playing_fee = 100
x = []
y = []

for i in range(1000):
    x.append(i+1)
    bet = random.randint(1,10)
    balance = balance-playing_fee;
    lucky_num = random.randint(1,10)

    if(bet == lucky_num):
        print("You won!")
        balance = balance+1000
        
    else: print("You lost! lucky number is:", lucky_num)
    
    y.append(balance)

print("Your current balance is: ", balance)

plt.plot(x,y)
plt.show()