import string
import random

symbols = []
# print(type(string.ascii_letters))
# print(string.ascii_letters);
symbols = list(string.ascii_letters) # type casting string to list

card1 = [0]*6 # list of size 5, initialized with 0
card2 = [0]*6
pos1 = random.randint(0,5);
pos2 = random.randint(0,5);
# pos1 and pos2 are the same symbol position in card1 and card2 respectively

sameSymbol = random.choice(symbols);
symbols.remove(sameSymbol)

if(pos1 == pos2):
    card2[pos1] = sameSymbol
    card1[pos2] = sameSymbol
else:
    card1[pos1] = sameSymbol
    card2[pos2] = sameSymbol
    card1[pos2] = random.choices(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])
    
i = 0;
while(i<5):
    if(i != pos1 and i != pos2):
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        
        card1[i] = alphabet1
        card2[i] = alphabet2
    i = i+1;

print(card1)
print(card2)