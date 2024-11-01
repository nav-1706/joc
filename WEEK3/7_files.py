with open("./WEEK3/file1.txt", "r+") as file1: # r only for read, can write | w only for write, can't read | r+ for both rad and write
    
    print(file1.read())
    file1.write("I am fine, thankyou!")
file1.close()

# Learn about more, modes in which file can be opened --> 4 modes, r, w, a, r+