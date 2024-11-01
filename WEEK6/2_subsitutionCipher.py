import string
dict = {}

data = ""
file = open("./WEEK6/cipherTrans.txt", "w")

print(string.ascii_letters)

for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]] = string.ascii_letters[i-5]
    
print(dict)

with open("./WEEK6/cipher.txt") as f:
    
    while True:
        c = f.read(1)
        if not c:
            print("End of file")
            break 
        if c in dict:
            data = dict[c]
            
        else:
            data = c
        
        file.write(data)
        # print(data) 

file.close()