import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4]) # python automatically genrate x-coord is not provided
plt.ylabel('Some numbers')
plt.title('My First Plot')
plt.show()  # This line is important to display the plot

plt.plot([1,2,3,4],[1,4,9,16])
#[1,2,3,4] --> x-coords
#[1,4,9,16] --> y-coords
plt.ylabel('Some numbers squared')
plt.title('My First Plot with Squared Numbers')
plt.show()  # This line is important to display the plot

plt.plot([1,2,3,4],[1,4,9,16], 'ro') # red dots
plt.ylabel('Some numbers squared')
plt.title('My First Plot with Squared Numbers')
plt.show() 

plt.plot([1,2,3,4],[1,4,9,16], 'r--') # red dahes lines
plt.ylabel('Some numbers squared')
plt.title('My First Plot with Squared Numbers')
plt.show() 

plt.plot([1,2,3,4],[1,4,9,16], 'rs') # red squares
plt.ylabel('Some numbers squared')
plt.title('My First Plot with Squared Numbers')
plt.show() 

plt.plot([1,2,3,4],[1,4,9,16], 'bs') # blue squares
plt.ylabel('Some numbers squared')
plt.title('My First Plot with Squared Numbers')
plt.show()

plt.plot([1,2,3,4],[1,4,9,16], 'g^') # green triangles
plt.ylabel('Some numbers squared')
plt.title('My First Plot with Squared Numbers')
plt.show()