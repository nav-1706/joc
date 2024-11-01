from random import randint

import turtle

# Turtle canva background colour
turtle.bgcolor("black")

# Creating turtle
tur = turtle.Turtle()

# Creating the dot dimeansion to represent/replace the matrix element
width = 5
height = 7

# after printing the dot moving the desired distance:
dot_distance = 25


tur.penup()
list_color = ["white", "yellow", "brown", "red", "blue", "green", "orange", "pink", "violet", "grey", "cyan"]


# Setting the initial position of the turtle:
tur.setpos(-250, 250)



def spiral (m, n):
    k = 0
    l = 0
    '''
        m = ending row index
        n = ending column index
        k = index of starting row
        l = index of starting column
        i = iterator
    '''
    
    # for turtle's angle movements:
    f = 0
    
    # Color of the dot to be white as the bg is black:
    tur.color("white")

    col = randint(0, 10)
    tur.color(list_color[col])
    while(k<m and l<n):
        
        if(f==1):
            tur.right(90)
        
        # Printing the first row from the remaining rows
        for i in range(l, n):
            tur.dot()
            tur.forward(dot_distance)
            # print(arr[k][i], end=" ")
        k += 1
        f = 1
        
        # reaching downward, so changing the angle again:
        tur.right(90)
        col = randint(0, 10)
        tur.color(list_color[col])
        # Printing the last column from the remaining column
        for i in range(k,m):
            tur.dot()
            tur.forward(dot_distance)
            # print(arr[i][n-1], end=" ")
        n -= 1
        
        
        tur.right(90)
        col = randint(0, 10)
        tur.color(list_color[col])
        if(k<m):
            # printing the last row from remaining rows
            for i in range(n-1, l-1, -1):
                tur.dot()
                tur.forward(dot_distance)
                # print(arr[m-1][i], end=" ")
            m -= 1

        tur.right(90)
        col = randint(0, 10)
        tur.color(list_color[col])
        if(l<n):
            # printing the first column from the remaining columns
            for i in range(m-1, k-1, -1):
                tur.dot()
                tur.forward(dot_distance)
                # print(arr[i][l], end=" ")
            l += 1
                            
                            
# arr = []
# count = 1
# for i in range(4):
#     l = []
#     for j in range(4):
#         l.append (count)
#         count+=1
#     arr.append(l)                           
    
# spiral(4, 4, arr)
  
spiral(20, 20)