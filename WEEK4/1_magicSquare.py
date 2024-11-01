# for any magic square of nxn, the magic number is M = n(n^2+1)/2

def generate_magic_square(n):
    # Create an n x n matrix filled with 0s
    magic_square = [[0] * n for _ in range(n)]

    # Initialize position for 1
    i = 0
    j = n // 2

    # Place numbers 1 to n^2 in the magic square
    for num in range(1, n * n + 1):
        magic_square[i][j] = num

        # Move to the next position
        new_i = (i - 1) % n
        new_j = (j + 1) % n

        # If the new position is already filled, move down
        if magic_square[new_i][new_j] != 0:
            i = (i + 1) % n
        else:
            i = new_i
            j = new_j

    # Print the magic square
    for row in magic_square:
        print(row)

# Size of the magic square
n = 3
generate_magic_square(n)
